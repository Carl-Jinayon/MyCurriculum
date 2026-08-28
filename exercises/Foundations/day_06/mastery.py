"""
What does a = [1,2,3];
b = a; 
b[0] = 9 do to a? 
How do you fix it?
it does also the value of index 0 of the list of a becaues they 
only points at the same thing 1 -> 9
- To fix this we need to do slicing to copy the original and not modifying it
using b = a[:] or b = a.copy()

a[1:4] is 2,3,4 
a[:3] is 1,2,3
a[::-1] reverses the whole list

list.sort() sorts the list without returning something.
sorted(list) returns a new list that is sorted. It does not change the values of 
the original list
"""
 
# Write a loop that prints each item of items with its 1-based index.
items = ["Soap", "Shampoo", "Toothbrush"]

for i, item in enumerate(items, start=1):
    print(f"Item {i}: {item}")

# Write a list comprehension that keeps only positive numbers from [-2, -1, 0, 1, 2].
nums = [-2, -1, 0, 1, 2]

pos_nums = [x for x in nums if x > 0]

print(pos_nums)