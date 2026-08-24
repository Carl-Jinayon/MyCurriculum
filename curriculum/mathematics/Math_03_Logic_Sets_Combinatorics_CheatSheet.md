# Math Day 3 Cheat Sheet — Logic, Sets, Combinatorics

## Propositional Logic

### Truth Tables
| p | q | ¬p | p∧q | p∨q | p→q | p↔q |
|---|---|---|---|---|---|---|
| T | T | F | T | T | T | T |
| T | F | F | F | T | F | F |
| F | T | T | F | T | T | F |
| F | F | T | F | F | T | T |

### Key Equivalences
- **De Morgan**: ¬(p∧q) ≡ ¬p ∨ ¬q ; ¬(p∨q) ≡ ¬p ∧ ¬q
- **Implication**: p→q ≡ ¬p ∨ q
- **Contrapositive**: p→q ≡ ¬q→¬p  (EQUIVALENT!)
- **Distribution**: p∧(q∨r) ≡ (p∧q)∨(p∧r); p∨(q∧r) ≡ (p∨q)∧(p∨r)
- **Absorption**: p∧(p∨q) ≡ p ; p∨(p∧q) ≡ p
- **Idempotent**: p∧p ≡ p ; p∨p ≡ p
- **Double negation**: ¬¬p ≡ p

### Python Booleans
```python
p and q   # short-circuits: if p is False, q not evaluated
p or q    # short-circuits: if p is True, q not evaluated
not p     # negation
```

## Set Theory

### Operations
| Operation | Symbol | Definition | Python |
|---|---|---|---|
| Union | A ∪ B | x ∈ A ∨ x ∈ B | `A | B` |
| Intersection | A ∩ B | x ∈ A ∧ x ∈ B | `A & B` |
| Difference | A \ B | x ∈ A ∧ x ∉ B | `A - B` |
| Symm Diff | A Δ B | (A\B) ∪ (B\A) | `A ^ B` |
| Complement | Aᶜ | U \ A | `U - A` |

### Set Identities
- **De Morgan**: (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ ; (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ
- **Distributive**: A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)
- **Absorption**: A ∪ (A ∩ B) = A ; A ∩ (A ∪ B) = A

### Cardinality
- |A ∪ B| = |A| + |B| − |A ∩ B| (Inclusion-Exclusion)
- |A ∪ B ∪ C| = Σ|A| − Σ|A∩B| + |A∩B∩C|

### Power Set
|P(A)| = 2^|A|

## Combinatorics

### Principles
- **Multiplication**: m ways × n ways = m×n ways (sequential)
- **Addition**: m ways + n ways (mutually exclusive) = m+n ways

### Permutations (ordered)
P(n, r) = n! / (n-r)!
```python
math.perm(n, r)
```

### Combinations (unordered)
C(n, r) = n! / (r! (n-r)!)
```python
math.comb(n, r)
```
C(n, r) = C(n, n-r)  (symmetry)

### Relationship
P(n, r) = C(n, r) × r!

### Common Counts
| Scenario | Formula | Example |
|---|---|---|
| Permutations of n | n! | 5! = 120 |
| Permutations of r from n | P(n,r) | P(5,3) = 60 |
| Combinations of r from n | C(n,r) | C(5,3) = 10 |
| Strings length k, no repeats | P(n, k) | P(26, 4) = 358,800 |
| Strings length k, repeats OK | n^k | 26^4 = 456,976 |
| Subsets of n-element set | 2^n | 2^3 = 8 |

## Must-Know Checklist
- [ ] Build truth table for ¬, ∧, ∨, →, ↔
- [ ] Simplify with De Morgan, distribution, absorption
- [ ] Compute A∪B, A∩B, A\B, AΔB, Aᶜ
- [ ] Apply |A∪B| = |A|+|B|−|A∩B|
- [ ] Compute C(n,r) and P(n,r) by hand and Python
- [ ] Distinguish permutation vs combination scenarios

## Active Recall
1. Truth table for p→q? p↔q?
2. ¬(p ∧ (q ∨ ¬r)) = ?
3. A={1,2,3}, B={2,3,4}, C={3,4,5} → A ∩ (B ∪ C) = ?
4. |A|=10, |B|=15, |A∩B|=5 → |A ∪ B| = ?
5. C(10,3) = ? P(10,3) = ?
6. 4-letter strings from "ABCD" no repeats? With repeats?