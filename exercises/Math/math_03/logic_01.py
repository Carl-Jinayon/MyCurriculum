# Build truth tables for: 
# (a) p ∧ (q ∨ r), 
# (b) ¬(p ∧ q) → r, 
# (c) (p → q) ∧ (q → p). 
# Print all 8 rows for 3 variables.

# Truth table enumeration
from itertools import product

print("p q r | a | b | c")
print("-----------------")
for p, q, r in product([True, False], repeat=3):

    a = p and (q or r)
    # ¬(p∧q) → r  ≡  ¬¬(p∧q) ∨ r  ≡  (p∧q) ∨ r   (double negation + implication rule)
    b = (p and q) or r
    # I just recognized here that this logic here can be represented as bidirectional
    # p == q  = True else False
    c = (not p or q) and (not q or p)

    print("T" if p else "F",
          "T" if q else "F",
          "T" if r else "F",
          "|",
          "T" if a else "F",
          "|",
          "T" if b else "F",
          "|",
          "T" if c else "F"
          )