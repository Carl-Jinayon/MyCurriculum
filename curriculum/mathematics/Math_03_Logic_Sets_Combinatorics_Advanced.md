# Math Day 3 Advanced — Logic, Sets, Combinatorics, Deeper

> STATUS: STRICTLY OPTIONAL. Read only if curious. Never gates progress.

## 1. Advanced Technical Content

### The Curry-Howard Correspondence (Logic = Types = Programs)
A profound insight: **Propositions are types. Proofs are programs.**
- A proof of `p → q` is a function taking a proof of `p` and returning a proof of `q`
- `p ∧ q` corresponds to a pair type `(p, q)`
- `p ∨ q` corresponds to a sum type `Either p q`
- `¬p` corresponds to `p → False` (a function that would produce absurdity)
- `True` is the unit type `()`
- `False` is the empty type (no constructors)

This is why functional languages (Haskell, OCaml, Rust) have such powerful type systems — they *are* proof assistants. When you write `def f(x: P) -> Q:`, you're constructing a proof of `P → Q`.

### Resolution and Automated Theorem Proving
- **Resolution rule**: from `p ∨ q` and `¬p ∨ r`, infer `q ∨ r`
- This is the core of Prolog and SAT solvers
- Conjunctive Normal Form (CNF): conjunction of disjunctions (e.g., (p∨¬q) ∧ (¬p∨r∨s))
- Any formula can be converted to CNF
- Modern SAT solvers (CDCL) can handle millions of variables — used in hardware verification, planning, crypto

### Quantifiers and Predicate Logic (preview)
Propositional logic lacks variables. Predicate logic adds:
- **Universal**: ∀x P(x) — "for all x, P(x) holds"
- **Existential**: ∃x P(x) — "there exists x such that P(x)"
- Negation flips quantifiers: ¬∀x P(x) ≡ ∃x ¬P(x); ¬∃x P(x) ≡ ∀x ¬P(x)
- This is what SQL WHERE clauses express: `SELECT * FROM t WHERE P(x)` is ∃x P(x)

### Set Theory — Deeper Waters

#### Russell's Paradox and Axiomatic Set Theory
The "set of all sets that don't contain themselves" leads to contradiction. This forced the development of ZFC (Zermelo-Fraenkel + Choice) axioms — the foundation of modern mathematics. You'll never need ZFC directly, but knowing it exists explains *why* we say "well-defined collection" not "any collection."

#### Cardinality of Infinite Sets
- |ℕ| = |ℤ| = |ℚ| = ℵ₀ (countable infinity)
- |ℝ| = 2^ℵ₀ = 𝔠 (continuum, strictly larger!)
- Cantor's diagonal argument proves |ℝ| > |ℕ|
- There are infinitely many sizes of infinity: ℵ₀ < 𝔠 < 2^𝔠 < ...

#### Well-Ordering and Transfinite Induction
The Well-Ordering Theorem (equivalent to Axiom of Choice): every set can be well-ordered.
This enables **transfinite induction** — induction on infinite well-ordered sets, not just ℕ.

### Combinatorics — The Art of Counting

#### The Twelvefold Way (Rota's classification)
The number of ways to put b balls into u urns, with various restrictions:
| | Distinguishable balls | Indistinguishable balls |
|---|---|---|
| Distinguishable urns, no restriction | u^b | C(u+b-1, b) |
| Distinguishable urns, at most 1/urn | P(u, b) = u!/(u-b)! | 1 if b ≤ u else 0 |
| Distinguishable urns, at least 1/urn | S(b, u) × u! | C(b-1, u-1) |
| Indistinguishable urns, no restriction | Σ S(b, k) (k=1..u) | partition(b, u) |
| Indistinguishable urns, at most 1 | 1 if b ≤ u else 0 | 1 if b ≤ u else 0 |
| Indistinguishable urns, at least 1 | Stirling S(b, u) | partition(b-u, u) |

Where S(n, k) = Stirling numbers of the second kind (number of ways to partition n items into k non-empty subsets).

#### Stirling Numbers of the Second Kind
S(n, k) = k × S(n-1, k) + S(n-1, k-1)
- S(n, 1) = 1, S(n, n) = 1
- S(n, 2) = 2^{n-1} - 1
- These count set partitions — crucial for clustering, hashing

#### Catalan Numbers (appear everywhere!)
C_n = C(2n, n) / (n+1) = (2n)! / (n!(n+1)!)
1, 1, 2, 5, 14, 42, 132, 429...
Count: valid parentheses strings, binary trees, polygon triangulations, monotonic paths not crossing diagonal, non-crossing handshakes...

#### Inclusion-Exclusion for Derangements (revisited)
D(n) = n! Σ_{k=0}^{n} (-1)^k / k! ≈ n! / e
Derangements approach n!/e as n → ∞. The probability a random permutation is a derangement ≈ 1/e ≈ 36.8%.

### The Pigeonhole Principle — the counting world's sharpest knife
If n+1 items go into n boxes, some box holds ≥ 2 items. Trivial to state, astonishing in application:
- Among 13 people, two share a birth-month (13 people, 12 months)
- Among any 5 numbers, two have the same last digit
- In any group of 367 people, two share a full birthday
The skill: recognizing WHICH things are pigeons and which are holes. Hash collisions (Day 7 Advanced) are pigeonhole in action — infinite possible keys, finite drawers.

### Probability Foundations (essential for ML)

#### Probability Space
(Ω, F, P) where:
- Ω = sample space (all outcomes)
- F = events (subsets of Ω, a σ-algebra)
- P: F → [0,1] with P(Ω)=1, countable additivity

#### Conditional Probability and Bayes
P(A|B) = P(A∩B) / P(B)    (if P(B) > 0)
Bayes: P(A|B) = P(B|A)P(A) / P(B)

#### Law of Total Probability
P(A) = Σ P(A|B_i)P(B_i) for a partition {B_i}

#### Random Variables
X: Ω → ℝ maps outcomes to numbers.
- Discrete: PMF P(X=x)
- Continuous: PDF f(x) where P(a<X<b) = ∫_a^b f(x) dx

#### Expectation, Variance, Covariance
E[X] = Σ x·P(X=x) (discrete) or ∫ x f(x) dx (continuous)
Var[X] = E[(X−E[X])²] = E[X²] − E[X]²
Cov[X,Y] = E[XY] − E[X]E[Y]
Correlation ρ = Cov / (σ_X σ_Y) ∈ [−1, 1]

#### Concentration Inequalities (crucial for ML generalization bounds)
- Markov: P(X ≥ a) ≤ E[X]/a for X ≥ 0
- Chebyshev: P(|X−μ| ≥ kσ) ≤ 1/k²
- Chernoff/Hoeffding: P(|X̄−μ| ≥ ε) ≤ 2e^{-2nε²} for bounded variables
- These are the mathematical guarantees behind "this model will generalize"

### Python for Advanced Probability

```python
import random
import math
from collections import Counter

# Monte Carlo estimation
def estimate_pi(n=1000000):
    inside = sum(1 for _ in range(n) if random.random()**2 + random.random()**2 <= 1)
    return 4 * inside / n

# Probability simulation
def birthday_paradox(trials=10000):
    collisions = 0
    for _ in range(trials):
        birthdays = [random.randint(1, 365) for _ in range(23)]
        if len(birthdays) != len(set(birthdays)):
            collisions += 1
    return collisions / trials  # ≈ 0.507

# Bayesian update
def bayes(prior, likelihood, evidence):
    return (likelihood * prior) / evidence

# Example: medical test
# P(disease) = 0.01, P(pos|disease)=0.99, P(pos|healthy)=0.05
# P(disease|pos) = 0.99*0.01 / (0.99*0.01 + 0.05*0.99) ≈ 0.167
```

## 2. Explore-It-Yourself Guide

1. **SAT solver**: Use Python's `pysat` or `python-sat` to solve a Sudoku as SAT. Or implement DPLL for 3-SAT.
2. **Monte Carlo**: Estimate π by throwing darts at unit circle. Then integrate sin(x) from 0 to π.
3. **Birthday paradox**: Run 10,000 trials with 23 people. Confirm ~50% collision rate.
4. **Derangements**: Generate all permutations of 5 elements, count derangements. Compare to D(5) formula.
5. **Catalan**: Generate all valid parentheses strings of length 2n for n=1,2,3,4. Count them — they're Catalan!
5. **Power set lattice**: For set {a,b,c}, draw the Hasse diagram of subsets ordered by inclusion.
6. **Monte Carlo integration**: Estimate ∫₀¹ e^{-x²} dx. Compare to scipy if available.

### Research rabbit holes (pick one):
- "Curry-Howard isomorphism" — the deep logic/programming duality
- "PCP theorem" — why approximation is as hard as exact solutions
- "Zero-knowledge proofs" — proving you know a secret without revealing it
- "Probabilistic method" (Erdős) — proving existence by showing probability > 0

## 3. Where This Leads Later

- **Logic & SAT** → formal verification, program synthesis, SMT solvers (Z3)
- **Sets & Counting** → database query optimization, hash tables, Bloom filters
- **Combinatorics** → algorithm analysis (Big-O is counting!), cryptography
- **Probability** → ML theory, Bayesian inference, A/B testing, RL
- **Information theory** → entropy = expected surprise = Σ -p log p → compression, decision trees

---

## Final Rule
Optional files never gate your progress. Master the main lesson, satisfy curiosity here, and move on.