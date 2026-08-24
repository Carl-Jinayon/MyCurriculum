from itertools import product

W = 9                                   # one width for ALL columns
col = lambda s: f'{s:^{W}}'             # center-pad anything to width W
t = lambda v: 'T' if v else 'F'

print(col('p') + col('q') + col('¬(p∧q)') + col('¬p∨¬q') + col('¬(p∨q)') + col('¬p∧¬q') + col('match'))
print('-' * (W * 7))
for p, q in product([True, False], repeat=2):
    a = not (p and q)
    b = (not p) or (not q)
    c = not (p or q)
    d = (not p) and (not q)
    m = (a == b) and (c == d)
    print(col(t(p)) + col(t(q)) + col(t(a)) + col(t(b)) + col(t(c)) + col(t(d)) + col(t(m)))
