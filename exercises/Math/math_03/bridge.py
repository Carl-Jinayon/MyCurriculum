# Python functions implementing: 
# truth table generator for 2 variables, 
# set operations union/intersection/difference, 
# nCr and nPr functions using math.comb/math.perm. 
# Test against hand answers.

import math

# Truth table generator
def truth_table(expr):
    print(f"{'p':<8}{'q':<8}result")     # header row
    print("-" * 22)                      # separator line
    for p in (True, False):
        for q in (True, False):
            print(f"{p!s:<8}{q!s:<8}{expr(p, q)!s}")

def implies(p, q):
    return (not p) or q

def biconditional(p, q):
    return p == q

def and_(p, q):
    return p and q

def or_(p, q):
    return p or q

# call the function truth_table then pass the function that fits your needs.

# Set operations
def union(a, b):
    return a | b

def intersec(a, b):
    return a & b

def diff(a, b):
    return a - b

# Combination and Permutation
first_num = 32
second_num = 11

result = math.perm(first_num, second_num)

math.comb(first_num, second_num)

# Just for fun!!! - I know this is not perfect haha I just did this for fun.
def main():
    while True:
        print("Welcome BRIDGE! This connects Logics, Sets and Combinatorics")
        print("\n1. Truth table generator" \
            "\n2. Set operations" \
            "\n3. Combination and Permutation" \
            "\n4. Exit Bridge.")
        try:
            choice = int(input("\nEnter choice: "))

            if choice == 1:
                while True:
                    print("\nWelcome to Truth Table Generator." \
                        "\nDirection: Choose operation below." \
                        "\n1. AND operation" \
                        "\n2. OR operation" \
                        "\n3. Implies(if, then)" \
                        "\n4. Biconditional" \
                        "\n5. Exit Truth Table Generator." \
                        "\n6. Exit Bridge.")
                    
                    try:
                        choice = int(input("\nEnter operation: "))

                        if choice == 1:
                            truth_table(and_)
                        elif choice == 2:
                            truth_table(or_)
                        elif choice == 3:
                            truth_table(implies)
                        elif choice == 4:
                            truth_table(biconditional)
                        elif choice == 5:
                            print("Truth Table Generator Exited.")
                            break
                        elif choice == 6:
                            print("Bridge exited.")
                            return
                        else:
                            print("Invalid choice.")
                    except Exception as e:
                        print(e) 
            elif choice == 2:
                while True:
                    print("\nWelcome set calculator!")
                    print("Direction: input two sets." \
                    "\nInput asked sets with values seperated with spaces" \
                    "\n1. Union operation" \
                    "\n2. Intersection operation" \
                    "\n3. Difference of two sets" \
                    "\n4. Exit Calculator." \
                    "\n5. Exit Bridge.")

                    try:
                        choice = int(input("\nEnter choice: "))

                        if choice in [1,2,3]:
                            first_set = input("\nEnter first set(separated by spaces): ").split()

                            first_set = set(first_set)

                            second_set = input("Enter second set(separated by spaces): ").split()

                            second_set = set(second_set)

                        if choice == 1:
                            print(f"Union set: {union(first_set, second_set)}")
                        elif choice == 2:
                            print(f"Intersection set: {intersec(first_set, second_set)}")
                        elif choice == 3:
                            print(f"Difference set: {diff(first_set, second_set)}")
                        elif choice == 4:
                            print("Calculator exited.")
                            break
                        elif choice == 5:
                            print("Bridge exited.")
                            return
                        else:
                            print("Invalid choice.")

                    except Exception as e:
                        print(e)
            elif choice == 3:
                while True:
                    print("\nWelcome to Combination and Permutation Calculator!!")
                    print("Direction: select type (combination or permutation)" \
                    "\n1. Combination" \
                    "\n2. Permutation" \
                    "\n3. Exit calculator" \
                    "\n4. Exit bridge")
    
                    try:
                        choice = int(input("Enter choice: "))
    
                        if choice == 1:
                            print("Number of ways to choose k items from n items without repetition and without order.")
                            n = int(input("Enter number for n: "))
                            k = int(input("Enter number for k: "))

                            print(f"Result: {math.comb(n, k)}")
                        elif choice == 2:
                            print("Number of ways to choose k items from n items without repetition and with order.")
                            n = int(input("Enter number for n: "))
                            k = int(input("Enter number for k: "))

                            print(f"Result: {math.perm(n, k)}")
                        elif choice == 3:
                            print("Calculator exited.")
                            break
                        elif choice == 4:
                            print("Bridge exited.")
                            return
                        else:
                            print("Invalid choice.")
                    except Exception as e:
                        print(e)
            elif choice == 4:
                print("Bridge exited.")
                return
            else:
                print("Invalid choice.")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()