# Math Day 2 Cheat Sheet — Functions f(x)

## Notation
```
f(x) = 2x + 3
 │     └─ rule applied to input
 │     └─┬─ x = placeholder for input
 └─ machine's NAME (f of x — NOT "f times x")
```

## Evaluating — substitute EVERYWHERE
```
f(x)  = 2x + 3
f(4)  = 2(4) + 3 = 11
f(-2) = 2(-2)+3  = -1     ← negatives: 2·(-2) = -4!
f(0)  = 2(0) + 3  = 3
```

## Reversing: given output, find input
```
f(x) = 2x + 3, f(x) = 11:
2x + 3 = 11 → 2x = 8 → x = 4
CHECK: f(4) = 11 ✓      ← balance rule again!
```

## Vocabulary
- Domain: allowed inputs ("what can I feed it?")
- Range: possible outputs ("what can come out?")
- Same machine regardless of letter: h(t)=5t ≡ h(x)=5x

## Math ↔ Python
| Math | Python |
|---|---|
| f(x) = 2x + 3 | `def f(x): return 2 * x + 3` |
| f(4) | `f(4)` |
| solve f(x)=k | search/loop for `f(x) == k` |

## Common Traps
- f(4) ≠ 4f; f(x+1) means substitute (x+1), not add after
- f(-2): multiply the WHOLE substitution: 2(-2) = -4
- f(x) = 11 is an equation (solve); f(11) is an evaluation (compute)

## Must-Know Checklist
- [ ] Explain f(x) in one sentence (and what it's NOT)
- [ ] Evaluate at positive/zero/negative inputs
- [ ] Build an input→output table
- [ ] Reverse a machine + check by substitution
- [ ] Python bridge matches hand answers

## Active Recall
1. f(x) = 3x - 1: f(0)? f(2)? f(-3)?
2. f(x) = 4x - 2, f(x) = 18 → x?
3. Does h(t) = 5t differ from h(x) = 5x? Why not?
4. Write the Python version of f(x) = 5x - 2 from memory.