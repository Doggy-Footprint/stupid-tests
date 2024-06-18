export class Trie {
    // TODO: don't allow duplicate
    roots: Map<string, Node>;

    constructor(roots?: Map<string, Node>) {
        this.roots = roots?? new Map<string, Node>();
    }

    addNode(fullstr: string, material: NodeMaterial) {
        const firstChar = fullstr.charAt(0);
        let root = this.roots.get(firstChar);
        if (!root) {
            root = new Node();
            this.roots.set(firstChar, root);
        }

        root.addNode(fullstr, material);
    }

    findNode(query: string): Node | null {
        let nodeSet = this.roots;

        for (const char of query.slice(0, -1)) {
            const children = nodeSet.get(char)?.children;
            if (!children) return null;
            nodeSet = children;
        }

        return nodeSet.get(query.slice(-1)) ?? null;
    }
}

export class Node {
    children: Map<string, Node>; // not-null // TODO: make children a Set object.
    parent: Node | null;
    metadata: NodeMetaData; // not-null
    materials: NodeMaterial[];

    constructor(materials?: NodeMaterial[] | null, parent: Node | null = null) {
        this.parent = parent;
        this.children = new Map<string, Node>();
        // additional information such as metadata and materials set via other methods.
        this.metadata = new NodeMetaData();
        this.materials = materials ?? [];
    }

    addChild(key: string, child: Node) {
        // TODO: duplicate nodeChar check.
        this.children.set(key, child);
        child.parent = this;
    }

    /**
     * Key function - form TRIE tree, Node with material is additional feature
     * @param root 
     * @param fullstr full string includig this node's key
     * @param material 
     */
    addNode(fullstr: string, material?: NodeMaterial) {
        let newNode = new Node();
        let cursor: Node = this;
        for (const key of fullstr.slice(1, -1)) {
            cursor = cursor.getChildOfKey(key);
        }
        cursor.addChild(fullstr.slice(-1), newNode);
        if (material) newNode.addMaterial(material, true);
    }

    getChildOfKey(key: string): Node {
        let child = this.children.get(key);
        if (!child) {
            child = new Node(null, this);
            this.children.set(key, child);
        }        
        return child;
    }

    addMaterial(material: NodeMaterial, updateAncestorMetadata: boolean) {
        this.materials.push(material);
        material.updateNode(this);

        if (updateAncestorMetadata && this.parent)
            this.parent.updateParentMetadataUptoRoot(material);
    }

    updateParentMetadataUptoRoot(material: NodeMaterial) {
        var cursor: typeof this.parent = this;
        while (cursor?.metadata.updatePromisingMaterial(material)) {
            cursor = cursor.parent;
        }
    }
}

export class NodeMetaData {
    private static readonly cutoff = 5;

    promisingMaterials: NodeMaterial[];

    constructor() {
        this.promisingMaterials = [];
    }

    /**
     * Update promisingMaterials by two step, sorting and cutting off.
     * @param material new materials to be updated
     * @returns true if updated, false if not updated
     */
    updatePromisingMaterial(material: NodeMaterial): boolean {
        const index = this.promisingMaterials.findIndex(m => this.calculateImportance(m) < this.calculateImportance(material));
        if (index == -1) return false;

        this.promisingMaterials = [...this.promisingMaterials.slice(0, index), material, ...this.promisingMaterials.slice(index, -1)];
        return true;
    }

    /**
     * calculate suggesting perference of material.
     * @param material 
     * @returns 
     */
    calculateImportance(material: NodeMaterial): number {
        return material.useCount;
    }
}

export class NodeMaterial {
    content: string;
    node: Node | null;

    useCount: number;

    constructor(content: string, node: Node | null = null) {
        this.content = content;
        this.node = node;
        this.useCount = 0;
    }

    updateNode(node: Node) {
        this.node = node;
    }

    updateUsage() {
        this.useCount++;
        this.node?.metadata.updatePromisingMaterial(this);
    }
}
