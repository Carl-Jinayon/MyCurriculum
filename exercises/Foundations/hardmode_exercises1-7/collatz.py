def collatz_steps(n):
    steps = 0
    while n != 1:
        steps += 1
        if n % 2 == 0:
            n //= 2
        else:
            n = (n * 3) + 1
        print(n)
    return steps

print(collatz_steps(6))