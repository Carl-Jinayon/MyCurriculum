# Day 4 Cheat Sheet — Loops

## while Loop
```python
i = 0
while i < 5:
    print(i)
    i += 1          # MUST update or infinite loop
```
Three parts: init → condition → update (inside body)

## for Loop + range()
```python
for i in range(5):         # 0,1,2,3,4
for i in range(1, 6):      # 1,2,3,4,5
for i in range(0, 10, 2):  # 0,2,4,6,8
for i in range(5, 0, -1):  # 5,4,3,2,1
```
`range(start, stop, step)` — stop is EXCLUSIVE

## Loop Control
```python
break          # exit loop immediately
continue       # skip to next iteration
```
```python
for i in range(10):
    if i == 5: break
    if i % 2 == 0: continue
    print(i)
```

## Loop else
```python
for item in items:
    if item == target:
        print("Found")
        break
else:
    print("Not found")   # runs ONLY if no break
```

## Nested Loops
```python
for i in range(3):
    for j in range(3):
        print(i, j)
```
Inner loop completes fully each outer iteration.

## Common Patterns
**Accumulator:**
```python
total = 0
for i in range(1, n+1):
    total += i
```

**Validation retry:**
```python
raw = input("> ")
while not raw.isdigit():
    raw = input("> ")
n = int(raw)
```

**Countdown:**
```python
for i in range(n, 0, -1):
    print(i)
```

## Must-Know Checklist
- [ ] I can write while that counts 1..10
- [ ] I can write for with range that counts 10..1
- [ ] I know break / continue / loop-else
- [ ] I ran all 6 exercises and verified
- [ ] I can trace nested loops

## Active Recall
1. `range(5)` → what values?
2. `range(1, 6)` → what values?
3. `range(10, 0, -1)` → what values?
3. `while True:` — when does it stop?
4. When does `for` `else` run?