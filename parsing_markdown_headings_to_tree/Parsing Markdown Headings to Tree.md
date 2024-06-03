# Summary

> ! Not Concluded test.

I parsed markdown headings and meet a conundrum about necessity for temporally storing passed data.

In other term, I couldn't decide whether trash the heading I'm processing or keep it at the point of processing the heading. That can happen when you want to store headings which includes headings with dedicated name.

## Example

We want to find `Z` headings with their parents.

```
# A

## B

### Z

## C

## D

### E

#### H

## Z
```

Parsing from the front, we can't decide to keep `# A` and `## B` until we meet `### Z`. But if you parse backward, you can immediately decide whether to keep or not. `#### H`, `### E`, `## D`, `## C` won't be stored.

## Usage

### 1D example

you can check code in **1D_example.py**

**Summary**: If you can decide whether to store a element from array by the following elements, backward traversal is better answer.

# Conclusion

Actually I thought I found something important in DS and algorithm, because in more complicated system, knoning that decision is determined based on future, we can find efficient way to deal with it. But I can't come up with example. I'll cover this later.