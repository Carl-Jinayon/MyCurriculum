table = [[i * j for j in range(1, 4)] for i in range(1, 4)]

print("Grid Table:")
for t in table:
    for val in t:
        print(val, end=" ")
    print()

# Center element:
print(f"Center element: {table[1][1]}")