export class Node {
    nodeChar: string;
    content: string | null; // null means empty placeholder
    children: Node[]; // not null
    parent: Node | null;
    data: NodeData;
    materials: NodeMaterial[]
    // TODO: distinguish tree structure Node and data Node. which is same but need to be distinguished.

    constructor()
    constructor(nodeChar: string, materials: NodeMaterial[] = [], data?: NodeData, children: Node[] = []) {
        this.nodeChar = nodeChar;
        this.children = children;
        data ? this.data = data : this.data = new NodeData();
        this.materials = materials;
    }

    /**
     * add a new node
     * @param root: a node to which the new node is appended
     * @param fullstr: fullstr's first chararcter should match with @param root's nodeChar.
     * @param data: data of the new node
     * @returns true if node is added. false if failed
     */
    static addNode(root: Node, fullstr: string, material: NodeMaterial): boolean {
        if (fullstr.charAt(0) !== root.nodeChar) return false;
        let newNode = new Node(fullstr.slice(-1), [material]);
        let cursor: Node = root;
        for (const char of fullstr.slice(1, -1)) {
            const next = cursor.getNextNode(char)!;
            cursor.data.updateDataOnAdd(material);
            cursor = next;
        }
        cursor.addChild(newNode);
        return true;
    }

    /**
     * find or create a node for given char under current node.
     * @param char: MUST be a single character
     * @returns: child node of current node with matching nodeChar, null means fail.
     */
    getNextNode(char: string): Node | null {
        if (char.length !== 1) return null;
        return this.children.find(c => c.nodeChar == char) ?? this.getNewPlaceholderChild(char);
    }

    /**
     * Add new placeholder child and return the new placeholder
     * @param char node char of placeholder
     * @returns new placeholder
     */
    getNewPlaceholderChild(char:string) {
        const child = new Node(char);
        this.children.push(child);
        return child;
    }

    addChild(node: Node) {
        let targetNode: Node | undefined;
        if (targetNode = this.children.find(c => c.nodeChar == node.nodeChar)) {
            // duplicate node exists
            target
        } else {
            this.children.push(node);
        }
    }
}

export class NodeData {
    static readonly trimCut: number = 5;


    // data about node's descendant
    promisingDescendant: NodeMaterial[];

    constructor(promisingDescendant: NodeMaterial[] = []) {
        this.promisingDescendant = promisingDescendant;
    }

    /**
     * update this data's information about descendants (not recursive)
     * @param newNode 
     */
    updateDataOnAdd(newNodeMaterial: NodeMaterial) {
        this.updatePromisingDesdant([newNodeMaterial]);
    }

    /**
     * 
     * @param nodes: candidates
     */
    updatePromisingDesdant(materials: NodeMaterial[]) {
        this.promisingDescendant = this.trimPromisingDescendant([...this.promisingDescendant, ...materials]);
    }

    /**
     * trim promisingDescendant by NodeData.trimCut ordered by its importance
     */
    trimPromisingDescendant(candidate: NodeMaterial[]): NodeMaterial[] {
        // TODO fix to use material as unit not node itself.
        return candidate.sort((a, b) => {
            const A = this.calculateImportance(a)
            const B = this.calculateImportance(b)
            return B - A;
        }).slice(0, NodeData.trimCut);
    }

    /**
     * Calculate importance of node to optimize tree management and search
     * @param node: a node of interest
     * @returns: importance. higher importance means it's important
     */
    calculateImportance(data: NodeMaterial | null): number {
        return data ? data.useCount : 0;
    }
}

export class NodeMaterial {
    // data about node itself
    useCount: number;
    lastUse: Date | null;

    // TRIE Node it is included in
    node: Node;
}

export class Keywords {
    roots: Node[]

    constructor (roots: Node[]) {
        
    }

    /**
     * findNode
     */
    public findNode() {
        
    }
}