# Day 2 Cheat Sheet — Data Types, Arithmetic, Strings

## The Four Basic Types
| Type | Meaning | Examples |
|---|---|---|
| `int` | whole number | `5`, `-3`, `0` |
| `float` | decimal number | `3.14`, `2.0` |
| `str` | text | `"hello"`, `""` |
| `bool` | truth value | `True`, `False` |

## Arithmetic
```
+ - *  basic
/      true division, ALWAYS float   (7/2 -> 3.5)
//     floor division                 (7//2 -> 3)
%      remainder                      (7%2  -> 1)
**     exponent                       (2**3 -> 8)
```
Order: parentheses > `**` > `* / // %` > `+ -`

## Strings
```python
"a" + "b"      # "ab"  (concatenate)
"ab" * 3       # "ababab"
len("abc")     # 3
"  x  ".strip()  # "x"
s.lower() / s.upper()
s[0]           # first char; s[-1] last char
f"value is {x}"  # f-string: inserts variable, auto-converts to text
f"{x:>10}"     # right-align, width 10   |{x:<10}| left  |{x:^10}| center
f"{n:.2f}"     # 2 decimal places; combine: {n:>8.2f}
```

## Conversions
```python
int("5")      # 5
float("3.5")  # 3.5
str(5)        # "5"
int(3.99)     # 3  (truncates! does NOT round)
```
`input()` ALWAYS returns a string → convert before math.

## Common Errors
- `"5" + 5` → `TypeError` (str + int). Convert: `int("5") + 5`
- `int("abc")` → `ValueError`
- `10 / 2` is `5.0`, not `5`

## Must-Know Checklist
- [ ] I can predict `//`, `%`, `**` results
- [ ] I know why input() needs conversion
- [ ] I can use f-strings
- [ ] I ran all 5 exercises and verified output

## Active Recall Questions
1. `9 // 2`? `9 % 2`? `9 / 2`?
2. `type("True")` vs `type(True)` — same?
3. How do you get the last digit of a number?
4. What does `int(2.9)` return? Why?

## Debugging Checklist
- Got `TypeError`? Check for str+int mixing → convert
- Got `ValueError`? Tried to convert non-number text
- Output wrong? Predict first, run, compare, then use `type()` on suspect values