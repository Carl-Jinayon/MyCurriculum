# Math Day 3 — Logic, Sets, and Combinatorics Basics

## Objective
- Understand propositional logic: propositions, connectives, truth tables, logical equivalences
- Master set operations: union, intersection, complement, difference, symmetric difference
- Learn combinatorics fundamentals: multiplication principle, permutations, combinations
- Connect all three to programming: boolean expressions, set operations, counting algorithms

## Prerequisites
- Math Day 2: function notation f(x), evaluation, and reversal
- Day 3: conditionals, boolean logic (and, or, not)
- Day 6: sets in Python (creation, union, intersection, difference)

## Why This Matters
Logic is the language of reasoning and the foundation of all computation. Set theory is the language of collections and the foundation of data structures. Combinatorics is the mathematics of counting — essential for algorithm analysis, probability, and understanding how many possible states a system can have. Together, they form the mathematical backbone of computer science.

## Mental Models

### 1. Propositions Are Truth-Bearing Statements
A proposition is a statement that is either **true** or **false** — never both, never neither.
- "2 + 2 = 4" → true (proposition)
- "The sky is green" → false (proposition)
- "x > 5" → not a proposition (depends on x)
- "Close the door" → not a proposition (command)

### 2. Logical Connectives Build Compound Propositions
| Connective | Symbol | Meaning | Python |
|---|---|---|---|
| NOT (negation) | ¬p | not p | `not p` |
| AND (conjunction) | p ∧ q | p and q | `p and q` |
| OR (disjunction) | p ∨ q | p or q | `p or q` |
| IMPLIES | p → q | if p then q | `not p or q` |
| IFF (biconditional) | p ↔ q | p if and only if q | `p == q` |

### 3. Truth Tables Reveal All Possible Cases
A truth table lists every possible combination of truth values for the component propositions and the resulting truth value of the compound proposition.

### 4. Sets Are Collections Defined by Membership
A set is a well-defined collection of distinct objects. The fundamental question: **is x in the set?**
- ∪ (union): A ∪ B = elements in A or B (or both)
- ∩ (intersection): A ∩ B = elements in both A and B
- \ (difference): A \ B = elements in A but not in B
- Δ (symmetric difference): A Δ B = elements in exactly one of A, B
- Aᶜ (complement): elements not in A (relative to a universal set U)

### 5. Combinatorics = The Mathematics of Counting
Two fundamental principles:
- **Multiplication Principle**: If there are m ways to do step 1 and n ways to do step 2, there are m × n ways to do both.
- **Addition Principle**: If there are m ways to do task A and n ways to do task B (and they're mutually exclusive), there are m + n ways to do one or the other.

### 6. Permutations vs Combinations
- **Permutation**: ordered arrangement — order matters. P(n, r) = n! / (n-r)!
- **Combination**: unordered selection — order doesn't matter. C(n, r) = n! / (r! (n-r)!)

## Propositional Logic

### Truth Tables

**Negation (¬p):**
| p | ¬p |
|---|---|
| T | F |
| F | T |

**Conjunction (p ∧ q):**
| p | q | p ∧ q |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

**Disjunction (p ∨ q):**
| p | q | p ∨ q |
|---|---|---|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

**Implication (p → q):** "If p then q"
| p | q | p → q |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

*Note: False implies anything (vacuous truth).*

**Biconditional (p ↔ q):** p if and only if q
| p | q | p ↔ q |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | T |

### Logical Equivalences (your algebraic toolkit)
- **De Morgan's Laws**: ¬(p ∧ q) ≡ ¬p ∨ ¬q ; ¬(p ∨ q) ≡ ¬p ∧ ¬q
- **Double Negation**: ¬¬p ≡ p
- **Implication as disjunction**: p → q ≡ ¬p ∨ q
- **Contrapositive**: p → q ≡ ¬q → ¬p (contrapositive is logically equivalent!)
- **Distribution**: p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r); p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r)
- **Absorption**: p ∧ (p ∨ q) ≡ p ; p ∨ (p ∧ q) ≡ p
- **Idempotent**: p ∧ p ≡ p ; p ∨ p ≡ p
- **Identity**: p ∧ T ≡ p ; p ∨ F ≡ p
- **Domination**: p ∨ T ≡ T ; p ∧ F ≡ F
- **Complement**: p ∨ ¬p ≡ T ; p ∧ ¬p ≡ F

### Python Connection: Boolean Expressions
Python's `and`, `or`, `not` are **short-circuiting**:
```python
# Short-circuit: right side not evaluated if result already determined
p and q  # if p is False, q never evaluated
p or q   # if p is True, q never evaluated
```
This is not just optimization — it's a semantic guarantee used for safety:
```python
x != 0 and y / x > 2  # safe: x != 0 checked first
```

## Set Theory

### Basic Operations (visualize with Venn diagrams)
| Operation | Symbol | Definition | Python |
|---|---|---|---|
| Union | A ∪ B | {x : x ∈ A ∨ x ∈ B} | `A | B` |
| Intersection | A ∩ B | {x : x ∈ A ∧ x ∈ B} | `A & B` |
| Difference | A \ B | {x : x ∈ A ∧ x ∉ B} | `A - B` |
| Symm. Diff | A Δ B | (A \ B) ∪ (B \ A) | `A ^ B` |
| Complement | Aᶜ | U \ A (relative to U) | `U - A` |

### Set Identities (algebra of sets — mirrors logic!)
| Name | Identity |
|---|---|
| Commutative | A ∪ B = B ∪ A ; A ∩ B = B ∩ A |
| Associative | (A ∪ B) ∪ C = A ∪ (B ∪ C) |
| Distributive | A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C) ; A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C) |
| De Morgan | (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ ; (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ |
| Identity | A ∪ ∅ = A ; A ∩ U = A |
| Domination | A ∪ U = U ; A ∩ ∅ = ∅ |
| Idempotent | A ∪ A = A ; A ∩ A = A |
| Complement | A ∪ Aᶜ = U ; A ∩ Aᶜ = ∅ |
| Absorption | A ∪ (A ∩ B) = A ; A ∩ (A ∪ B) = A |

### Cardinality and the Inclusion-Exclusion Principle
|A ∪ B| = |A| + |B| − |A ∩ B|

For three sets:
|A ∪ B ∪ C| = |A| + |B| + |C| − |A∩B| − |A∩C| − |B∩C| + |A∩B∩C|

### Power Set
The power set P(A) is the set of all subsets of A. |P(A)| = 2^|A|.

## Combinatorics Basics

### Multiplication Principle
If task 1 has m ways and task 2 has n ways, total ways = m × n.
**Example**: 3 shirts × 4 pants = 12 outfits.

### Addition Principle (mutually exclusive cases)
If you can do task A in m ways OR task B in n ways (mutually exclusive), total = m + n.
**Example**: Choose a dessert: 3 ice cream flavors OR 2 cakes = 5 choices.

### Permutations — Ordered Arrangements
**P(n, r) = n! / (n-r)!** = number of ways to arrange r items chosen from n distinct items, **order matters**.

Examples:
- 3! = 6 ways to arrange 3 distinct items
- P(5, 3) = 5! / 2! = 120 / 2 = 60 ways to award 1st/2nd/3rd prize among 5 people

### Combinations — Unordered Selections
**C(n, r) = n! / (r! (n-r)!)** = n choose r = number of ways to choose r items from n, **order doesn't matter**.

Examples:
- C(5, 2) = 5! / (2! 3!) = 10 ways to choose 2 people from 5 for a team
- C(52, 5) = 2,598,960 possible poker hands

### Key Relationship
P(n, r) = C(n, r) × r!
*Permutations = Combinations × (arrangements of the chosen items)*

### Binomial Theorem Connection (preview)
(x + y)ⁿ = Σ C(n, k) x^{n-k} y^k
The coefficients are exactly the binomial coefficients C(n, k).

### Pascal's Triangle (recursive way to compute C(n, k))
C(n, k) = C(n-1, k-1) + C(n-1, k) with base C(n, 0) = C(n, n) = 1

## Python Connections

### Logic in Code
```python
# Truth table enumeration
from itertools import product
for p, q in product([False, True], repeat=2):
    print(p, q, not p, p and q, p or q, (not p) or q)

# Set operations
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)   # union
print(A & B)   # intersection
print(A - B)   # difference
print(A ^ B)   # symmetric difference
```

### Combinatorics in Python
```python
import math
from itertools import permutations, combinations

math.comb(5, 2)      # C(5, 2) = 10
math.perm(5, 3)      # P(5, 3) = 60
list(permutations('abc', 2))  # [('a','b'), ('a','c'), ('b','a'), ('b','c'), ('c','a'), ('c','b')]
list(combinations('abc', 2))  # [('a','b'), ('a','c'), ('b','c')]
```

## Common Mistakes
- Confusing p → q with q → p (converse is NOT equivalent!)
- Confusing ∨ (inclusive OR) with XOR (exclusive or)
- Forgetting that p → q is vacuously true when p is false
- Double-counting in combinatorics (forgetting to divide by r! when order doesn't matter)
- Forgetting to check if events are mutually exclusive before adding
- Confusing permutations (order matters) with combinations (order doesn't)

## Verification Checklist
- [ ] I can build truth tables for ¬, ∧, ∨, →, ↔
- [ ] I can simplify expressions using De Morgan, distribution, absorption
- [ ] I can compute A ∪ B, A ∩ B, A \ B, A Δ B, Aᶜ for given sets
- [ ] I can apply inclusion-exclusion for |A ∪ B| and |A ∪ B ∪ C|
- [ ] I can compute P(n, r) and C(n, r) by hand and in Python
- [ ] I can distinguish when to use permutation vs combination
- [ ] I can trace short-circuit evaluation in Python boolean expressions

## Exercises (exercises/Math/math_03/)
1. `logic_01.py` — Build truth tables for: (a) p ∧ (q ∨ r), (b) ¬(p ∧ q) → r, (c) (p → q) ∧ (q → p). Print all 8 rows for 3 variables.
2. `logic_02.py` — Use Python to verify De Morgan: for all p,q in {T,F}, check ¬(p∧q) == (¬p ∨ ¬q) and ¬(p∨q) == (¬p ∧ ¬q). Print truth table with a "match" column.
3. `sets_01.py` — Given A={1,2,3,4}, B={3,4,5,6}, C={4,5,6,7}: compute union, intersection, difference, symmetric difference, cardinalities. Verify |A ∪ B| = |A| + |B| − |A ∩ B|.
4. `sets_02.py` — Survey problem: 100 students: 60 take CS, 40 take Math, 15 take both. How many take neither? Use inclusion-exclusion. Verify with Python sets.
5. `counting_01.py` — (a) How many ways to arrange 5 books on a shelf? (b) How many ways to choose 3 books from 8 for a trip? (c) A 4-digit PIN: digits 0-9, no repetition. How many? (d) Same, with repetition allowed.
5. `counting_02.py` — Password rules: 8 chars, uppercase + lowercase + digits (62 chars). (a) Total possible? (b) Must contain at least one digit? (use complement: total − no digits). (c) Must contain at least one of each type? (inclusion-exclusion over 3 types).
6. `bridge.py` — Python functions implementing: truth table generator for 2 variables, set operations union/intersection/difference, nCr and nPr functions using math.comb/math.perm. Test against hand answers.

## HARD MODE (optional, after core)
1. `logic_hard.py` — Implement a tautology checker: given a boolean expression string with variables p,q,r (like "p and (q or not r)"), check if it's a tautology by evaluating all 2^n assignments.
2. `sets_hard.py` — Given a family of 5 sets of integers (each size 3-6), find: (a) the element in the most sets, (b) the symmetric difference of all 5 sets, (c) the power set of the union (warning: size grows fast!).
3. `counting_hard.py` — Derangements: number of permutations of n elements where no element is in its original position. D(n) = n! Σ_{k=0}^{n} (-1)^k / k!. Compute D(4), D(5) by formula and verify by generating all permutations in Python.

## Mastery Check (from memory)
1. Truth table for p → q? p ↔ q?
2. Simplify ¬(p ∧ (q ∨ ¬r)) using De Morgan and distribution.
3. If A={1,2,3}, B={2,3,4}, C={3,4,5}: A ∩ (B ∪ C) = ?
4. |A|=10, |B|=15, |A∩B|=5 → |A ∪ B| = ?
3. C(10, 3) = ? P(10, 3) = ?
4. How many 4-letter strings from "ABCD" with no repeats? With repeats allowed?
5. Explain why P(n, r) = C(n, r) × r!

## Reflection
- Which equivalence felt least intuitive? Why?
- How does short-circuit evaluation in Python relate to truth tables?
- When would you use a set vs a dict vs a list in a real program?

## Key Takeaways
- Logic is algebra with truth values — same algebraic intuition applies
- Sets and logic are isomorphic: ∧ ↔ ∩, ∨ ↔ ∪, ¬ ↔ complement
- Counting is multiplication and division — avoid double-counting
- Permutations = ordered (multiply); Combinations = unordered (divide by r!)
- Python's short-circuit evaluation = truth table optimization