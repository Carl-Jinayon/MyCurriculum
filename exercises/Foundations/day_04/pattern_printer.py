height = int(input("Enter height for the triangle: "))
stars = 1

for height in range(height, 0, -1):
    # This is for readability
    spaces = height - 1 
    # Handles number of spaces for each line
    for _ in range(spaces):
        print(" ", end="")
    # Handles number of stars for each line
    for _ in range(stars):
        print("*", end="")
    # Increases number of stars everytime it runs down
    stars += 1
    # New line
    print()