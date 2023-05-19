a, b = map(int, input().split())
q, r = divmod(a, b)
if r < 0:
    r += abs(b)
    q = (a - r) // b
print(f'{q} {r}')
