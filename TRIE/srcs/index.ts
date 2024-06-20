import { Trie, Node, NodeMetadata, NodeMaterial } from './trie'

const trie = new Trie();

let aba: Node | null;

trie.addNode("abc", new NodeMaterial("abc"));
trie.addNode("abb", new NodeMaterial("abb"));
const ab = trie.findNode("ab");
const abc = trie.findNode("abc");
const abb = trie.findNode("abb");

abb?.materials[0]?.readContent();
trie.addNode("aba", new NodeMaterial("aba"));
aba = trie.findNode("aba");

console.log('done');