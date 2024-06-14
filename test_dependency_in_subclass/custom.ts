import { TestOrder, Node } from "./base";

function getRandomInt(max: number) {
    return Math.floor(Math.random() * max);
}

// Just custom random number.
class PlatformDependentComponent {
    comp: number;

    constructor() {
        this.comp = getRandomInt(10);
    }
}

export class CustomNode extends Node {
    pdc: PlatformDependentComponent;

    constructor(content: string) {
        super(content);
        this.pdc = new PlatformDependentComponent();
    }
}

export class CustomOrder extends TestOrder {
    nodesSize: number;
    netpdc: number;

    constructor() {
        super();
        this.nodesSize = 0;
        this.netpdc = 0;
    }

    addNode(node: CustomNode) {
        super.addNode(node);
        this.nodesSize++;
        this.netpdc += node.pdc.comp;
    }

    showMetadata() {
        console.log("nodeSize: ", this.nodesSize);
        console.log("netpdc: ", this.netpdc);
    }
}

