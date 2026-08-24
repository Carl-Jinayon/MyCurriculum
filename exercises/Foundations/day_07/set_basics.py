nums = {2,3,4,2,2,2,5,3}

unique_nums = set(nums)

unique_nums.add(7)
unique_nums.add(9)

unique_nums.discard(2)
unique_nums.discard(1)

print("3 in nums:", 3 in nums)
print("10 in nums:", 10 in nums)
