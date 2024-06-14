// tsc test_base.ts 
// node test_base.js

import { MyOrder, Node } from './base'

export function test() {

    const testSet: string[] = ['eeee', 'eqw', 'esy', 'xgi', 'mxg', 'syi']
    // need to be ordered as ['eeee', 'eqw', 'esy', 'mxg', 'xgi', 'syi']

    const myOrder = new MyOrder();

    testSet.forEach(t => {
        const node = new Node(t);
        myOrder.addNode(node);
    });

    myOrder.showNodes();
    console.log('done');
}
