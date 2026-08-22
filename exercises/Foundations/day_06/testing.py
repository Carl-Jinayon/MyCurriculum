scores = [2,3,4,5]
print(scores)

print("\nAppend function")
scores.append(6)
print(scores)

print("\nExtend function")
another_scores = [7,8,9,10]
scores.extend(another_scores)
print(scores)

print("\nInsert function")
scores.insert(2, 0)
print(scores)

print("\nPop function (default last, but has parameter for index)")
print("Pops last item")
pop_item = scores.pop()
print(scores)
print(f"Pop item: {pop_item}")
print("Pop item at index 1")
pop_item = scores.pop(1)
print(scores)
print(f"Pop item:", pop_item)

print("\nRemove first occurence of the parameter in the list")
scores.remove(0)
print(f"Remove zero:", scores)

print("\nIndex returns the index of first occurence of x")
scores.append(2)
print(scores.index(2))

print("\nReturns the number of occurences of the argument")
print("Number of occurences of '2':", scores.count(2))

print("\nUsing sorted function (returns a new list)")
sorted_scores = sorted(scores)
print("Scores:", scores)
print("Sorted scores:", sorted_scores)

print("\nSort the list (changing the actual object)")
print("Before:", scores)
scores.sort()
print("After:", scores)

print("\nReverse in place")
print("Before:", scores)
scores.reverse()
print("After:", scores)

print("\nNew copy")
scores_copy = scores.copy()
print("Scores:",scores)
print("Scores copy:", scores_copy)

