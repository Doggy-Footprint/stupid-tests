Strict type system give great deal of assurance on interface (GoF concept)

I didn't implement any methods of each class yet I work like there are methods I need.

---

# Reinventing TRIE

## Motivation

I need to design a datastructure which support quick search of string based on user input. I'm developing an Obsidian Plugin which shows suggestion of internal link based on user input if you are interested in detail. Anyway, with some thoughts, I figured out that I need to make a tree for each node has a single character and a route from root node to a node (not necessarily leaf node) make a string. Later on, I learned that this kinda tree is called TRIE.

I wanted to design TRIE by myself, considering how should I implement add, delete, update, and search. So, I'm trying to reinventing TRIE. But with some customization. 

As I said, this TRIE is used to suggest. For this purpose, I thought of each node including metadata about its all descendants and materials which correspond to a object I want to connect to the string structured by TRIE. I tried developing without noticing that each node in TRIE might indicating several materials. 

TRIE, Node, NodeMetadata, NodeMaterial will do the trick I need. And I think I'd better update detailed interfaces of each classes.