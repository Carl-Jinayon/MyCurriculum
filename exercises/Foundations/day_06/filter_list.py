nums = [1,2,3,4,5,6,7,8,9,10]

even_nums = [x for x in nums if x % 2 == 0]

# Print even numbers
print("Even numbers: ", end="")
for even in even_nums:
    print(even, end=" ")

evens = []

for even in nums:
    if even % 2 == 0:
        evens.append(even)

print("\nEven numbers: ", end="")
for even in evens:
    print(even, end=" ")