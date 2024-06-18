import { Trie, Node, NodeMetaData, NodeMaterial } from './trie'

const trie = new Trie();

trie.addNode("abc", new NodeMaterial("abc"));
trie.addNode("abb", new NodeMaterial("abb"));
const ab = trie.findNode("ab");
const abc = trie.findNode("abc");
const abb = trie.findNode("abb");

console.log('done');