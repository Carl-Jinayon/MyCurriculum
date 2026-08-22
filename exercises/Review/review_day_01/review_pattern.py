height = input("Enter positive integer: ")

if height.isdigit():
    height = int(height)

    if height > 0:
        for i in range(1, height + 1):
            for _ in range(i):
                print("*", end="")
            print()
    else:
        print("Integer is not positive.")
else:
    print("Input is not valid.")