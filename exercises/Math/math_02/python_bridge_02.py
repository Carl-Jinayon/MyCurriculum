def func(x):
    return 3 * x - 1

print(func(0))
print(func(2))
print(func(-3))

# Verified: results are same as the results I provided in the exercise 1

def g(x):
    return 4 * x - 2

"""
g(x) = 4x - 2
g(x) = 18

4x - 2 = 18
4x - 2 + 2 = 18 + 2
4x = 20
4x/4 = 20/4
x = 5 
"""
my_algebra_answer = 5

i = 0
while True:
    if g(i) == 18:
        print(f"Value: {i}")
        break
    i += 1

if i == my_algebra_answer:
    print("My answer is correct!")
else:
    print("My answer is wrong.")