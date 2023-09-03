t, h, w = map(int, input().split())
results = []
for _ in range(t):
    go_work, go_home = input().split()
    if go_work == 'Y' or w == 0:
        results.append('Y')
        h -= 1
        w += 1
    else:
        results.append('N')
    if go_home == 'Y' or h == 0:
        results.append('Y')
        h += 1
        w -= 1        
    else:
        results.append('N')
for i in range(0, t*2-1, 2):
    print(f"{results[i]} {results[i+1]}")
    