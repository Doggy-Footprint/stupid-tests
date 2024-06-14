// This class support add method according to order defined by MyOrder.myOrder
export class TestOrder {
    static myOrder: string[] = ['e', 'q', 'w', 'm', 'x', 'g', 'i', 'y', 's', 'k', 'j', 'o', 'h', 'b', 'r', 't', 'v', 'z', 'd', 'f', 'l', 'a', 'n', 'c', 'p', 'u'];
    
    nodes: Node[];

    constructor() {
        this.nodes = [];
    }

    addNode(node: Node) {
        const length = this.nodes.length;

        if (length == 0) {
            this.nodes.push(node);
            return;
        }

        for (let i = 0; i < length; i++) {
            if (!this.compareNodes(this.nodes[i], node)) {
                this.nodes = [...this.nodes.slice(0, i), node, ...this.nodes.slice(i)];
                return;
            }
        }

        this.nodes.push(node);
    }

    // return true if a comes first
    compareNodes(a: Node, b: Node): boolean {
        const length = Math.min(a.content.length, b.content.length);
        
        for (let i = 0; i < length; i++) {
            const a_ = TestOrder.myOrder.indexOf(a.content.charAt(i));
            const b_ = TestOrder.myOrder.indexOf(b.content.charAt(i));
            if (a_ === b_) continue;
            if (a_ < b_) return true;
            else if (a_ > b_) return false;
        }

        return a.content.length < b.content.length;
    }

    showNodes() {
        this.nodes.forEach(n => console.log(n));
    }
}

export class Node {
    content: string;

    constructor(content: string) {
        this.content = content;
    }
}