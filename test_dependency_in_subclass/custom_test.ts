import { CustomNode, CustomOrder } from './custom'

export function test_custom() {
    const testSet: string[] = ['eeee', 'eqw', 'esy', 'xgi', 'mxg', 'syi']
    // need to be ordered as ['eeee', 'eqw', 'esy', 'mxg', 'xgi', 'syi']

    const customOrder = new CustomOrder();

    testSet.forEach(t => {
        const node = new CustomNode(t);
        customOrder.addNode(node);
    });

    /**
     * customOrder.showNodes(); will show detailed information of CustomNode objects
     * because it uses console.log(), which take 'any' type.
     * But usually, methods which have never been overriden need to be act as the nodes
     * are not customized.
     */
    customOrder.showNodes();
    // custom method.
    customOrder.showMetadata();
}