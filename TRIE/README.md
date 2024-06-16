# Goal

Practicing writing TRIE data structure with below needs.
It might be different from typical TRIE.

## Functionalities needed

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

- [ ] figure out add / delete - affecting nodes 