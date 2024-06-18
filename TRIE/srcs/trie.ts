export class Trie {
    // TODO: don't allow duplicate
    roots: Node[];

    constructor(roots: Node[] = []) {
        this.roots = roots;
    }

    addNode(fullstr: string, material?: NodeMaterial) {
        const firstChar = fullstr.charAt(0);
        let root = this.roots.find(r => r.nodeChar == firstChar);
        if (!root) {
            root = new Node(firstChar);
            this.roots.push(root);
        }
        Node.addNode(root, fullstr, material);
    }

    findNode(query: string): Node | null {
        let nodeSet = this.roots;

        for (const char of query.slice(0, -1)) {
            const children = nodeSet.find(n => n.nodeChar == char)?.children;
            if (!children) return null;
            nodeSet = children;
        }

        return nodeSet.find(n => n.nodeChar == query.slice(-1)) ?? null;
    }
}

/**
 * A Node object is responsible for forming TRIE with its own character.
 * Additionally, the Node class holds NodeMetadata, NodeMaterial properties. 
 * Node class's responsibility is to call each properties method, 
 * not manipulating them directly.
 */
export class Node {
    nodeChar: string;
    children: Node[]; // not-null // TODO: make children a Set object.
    parent: Node | null;
    metadata: NodeMetaData;
    materials: NodeMaterial[];

    constructor(nodeChar: string, parent: Node | null = null, children: Node[] = []) {
        this.nodeChar = nodeChar;
        this.parent = parent;
        this.children = children;
        // additional information such as metadata and materials set via other methods.
        this.metadata = new NodeMetaData();
        this.materials = [];

        if (parent) parent.addChild(this);
    }

    addChild(child: Node) {
        // TODO: duplicate nodeChar check.
        this.children.push(child);
        child.parent = this;
    }

    /**
     * Key function - form TRIE tree, Node with material is additional feature
     * @param root 
     * @param fullstr 
     * @param material 
     */
    static addNode(root: Node, fullstr: string, material?: NodeMaterial) {
        if (fullstr.charAt(0) !== root.nodeChar) return false;
        let newNode = new Node(fullstr.slice(-1));
        let cursor: Node = root;
        for (const char of fullstr.slice(1, -1)) {
            cursor = cursor.getNextNode(char)!; //gexNextNode is assured to return Node, not-null
        }
        cursor.addChild(newNode);
        if (material) newNode.addMaterial(material, true);
        

        //newNode.addMaterial (after parent route set)
    }

    getNextNode(char: string): Node | null {
        if (char.length !== 1) return null;
        return this.children.find(c => c.nodeChar == char) ?? this.getNewPlaceholderChild(char);
    }

    getNewPlaceholderChild(char: string): Node {
        return new Node(char, this);
    }

    addMaterial(material: NodeMaterial, updateAncestorMetadata: boolean) {
        this.materials.push(material);

        if (updateAncestorMetadata && this.parent)
            this.parent.updateParentMetadataUptoRoot(material);
    }

    updateParentMetadataUptoRoot(material: NodeMaterial) {
        var cursor: typeof this.parent = this;
        while (cursor?.metadata.updatePromisingMaterials([material])) {
            cursor = cursor.parent;
        }
    }
}

export class NodeMetaData {
    private static readonly cutoff = 5;

    promisingMaterials: NodeMaterial[];

    constructor(promisingMaterials: NodeMaterial[] = []) {
        this.promisingMaterials = [];
        this.updatePromisingMaterials(promisingMaterials);
    }

    /**
     * Update promisingMaterials by two step, sorting and cutting off.
     * @param materials new materials to be updated
     * @returns true if updated, false if not updated
     */
    updatePromisingMaterials(materials: NodeMaterial[]): boolean {
        if (this.promisingMaterials.length >= NodeMetaData.cutoff) {
            const leastImportantOrigin = this.promisingMaterials.reduce((least, current) => {
                return this.calculateImportance(least) <= this.calculateImportance(current) ? least : current;
            });
            const mostImportantNew = materials.reduce((biggest, current) => {
                return this.calculateImportance(biggest) >= this.calculateImportance(current) ? biggest : current;
            })
            if (this.calculateImportance(leastImportantOrigin) > this.calculateImportance(mostImportantNew)) return false;    
        }

        this.promisingMaterials = [...this.promisingMaterials, ...materials]
            .sort((a, b) => this.calculateImportance(b) - this.calculateImportance(a)) //descending order
            .slice(0, NodeMetaData.cutoff);
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

    useCount: number;

    constructor(content: string) {
        this.content = content;
        this.useCount = 0;
    }
}
