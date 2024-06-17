# Design of TRIE

## TRIE class
A TRIE object is reponsible for holding root nodes and managing string based simple TRIE data structure. To clarify, it shouldn't be influenced by Node's Metadata or Materials.

## Node class
A Node object is responsible for forming TRIE with its own character. Additionally, the Node class holds NodeMetadata, NodeMaterial properties. Node class's responsibility is to call each properties method, not manipulating them directly.

## NodeMetadata
A NodeMetadata object represents a Node object's descendants information, which can be used to search TRIE with addtitional purpose such as show frequently used first.

## NodeMaterial
A NodeMaterial object is what is connected to the string formed by TRIE route. Since multiple NodeMaterial objects can be connected to a single string, a Node class has multiple NodeMaterial objects.

## Thoughts
NodeMetadata and NodeMaterial classes are closely connected. For example, NodeMetadata need to query NodeMaterial object's `count` property to calculate importance of the NodeMaterial object.