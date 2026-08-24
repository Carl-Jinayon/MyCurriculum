"""
Given A={1,2,3,4}, B={3,4,5,6}, C={4,5,6,7}: 
compute union, intersection, difference, symmetric difference, cardinalities. 
Verify |A ∪ B| = |A| + |B| − |A ∩ B|.
"""

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = {4, 5, 6, 7} 

# Union
u = a | b | c
print(u)

# Intersection
i = a & b & c
print(i)

# Symmetric difference
s = a ^ b ^ c
print(s)

# Verify union of a and b
u_ab = a | b
print(abs(len(u_ab)) == abs(len(a)) + abs(len(b)) - abs(len(a & b)))

print(abs(len(u)) == (abs(len(a)) + abs(len(b)) + abs(len(c))) - abs(len(a & b)) - abs(len(a & c)) - abs(len(b & c)) + abs(len(a & b & c)))