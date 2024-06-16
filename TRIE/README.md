# Goal

Practicing writing TRIE data structure with below needs.
It might be different from typical TRIE.

In short summary, TRIE with metadata about usage.

## Functionalities needed

### IDEA

- search node & get information to suggest user in the middle of search
    - metadata(used count & last used date, etc.)
    - how to accumulate empty placeholders?
    - metadatas
        - number of leaves under this node
        - frequently used leaves under this node
            - use count
            - last use
            - user configured frequently used note tag.
- update metadata of node without moving it
    - propagates towards parents
- moving a node inside tree (string of node is changed)
    - delete & add?
    - TODO
- deleting a node
    - leaf node
        - no effect in tree structure. update metadata of ascendant nodes.
    - non-leaf nodes
        - change a node to empty placeholder
        - traverse its descendant nodes for accumulation of empty placeholder.    
- adding a node
    - ground rule
        - don't make multi-character nodes. always make full tree of empty placeholders.
            - Then adding is either replaceing empty place holder or adding a new child(single line tree to leaf). Neither cases require updating tree.
    - add to existing place holder
        - no changes
    - add to a leaf
        - no effect in tree structure. update metadata of ascendant nodes.
    - add to non-leaf nodes.
        - check adding node's parent. (for example, 'search' node's parent node is 'searc')
            - 

### Tree

#### properties
```ts
roots: Node[]
```

#### methods

1. find a `Node` object with string
2. from given partial string, give hints to possible nodes
    For example, cumulative number of descendants, frequently accessed descendant(history), 
3. add new node
    this needs search in parent's all descendant for better connectivity.
4. delete existing node
    children of deleted node needs new parent

### Node

#### properties

```ts
substr: string
children: Node[]
parent: Node | null(only roots)
metadata: MetadataAboutDescendant
```

#### methods

