# Boolean Expression Equality Checker

This is just a simple Python script I put together for fun to alleviate the boredom of some of my more advanced programming students.

This program takes 2 simple boolean expressions, builds their *Truth Table* and verifies their *Equivalency*.

## Example

```python
expression1 = "(a and b) or (not a)"
expression2 = "b or not a"

if are_equivalent( expression1, expression2 ):
    print( f"\nThe expressions `{expression1}` and `{expression2}` are equivalent." )
else:
    print( f"\nThe expressions `{expression1}` and `{expression2}` are not equivalent." )
```

| a     | b     | (a and b) or (not a) | b or not a | Equivalent |
| ----- | ----- | -------------------- | ---------- | ---------- |
| True  | True  |                 True |       True |       True |
| True  | False |                False |      False |       True |
| False | True  |                 True |       True |       True |
| False | False |                 True |       True |       True |

The expressions `(a and b) or (not a)` and `b or not a` are equivalent.