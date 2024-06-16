export class Node {
    substr: string;
    children: Node[]; // not null

    constructor(substr: string, children: Node[] = []) {
        this.substr = substr;
        this.children = children;
    }

    
}