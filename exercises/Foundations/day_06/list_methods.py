nums = [3, 1, 4, 1, 5]

# Append 9
print("Before appending:", nums)
nums.append(9)
print("After appending:", nums)

# Extended
nums.extend([2,6])
print("Extended nums:", nums)

# Pop last
nums.pop()
print("Pop last number:", nums)

# Remove first
nums.remove(1)
print("Removed first:", nums)

# Count occurences
print("Count 1:", nums.count(1))

# Index of number 4
print("Index of 4:", nums.index(4))

# Sort
print("Before sorting:", nums)
nums.sort()
print("After sorting:", nums)

# Reverse
print("Before reversing:", nums)
nums.reverse()
print("After reversing:", nums)
