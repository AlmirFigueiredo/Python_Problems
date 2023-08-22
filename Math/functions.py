res = []
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    rafael = lambda x, y: (3*x)**2 + y**2
    beto = lambda x, y: 2*x**2 + (5*y)**2
    carlos = lambda x, y: -100*x + y**3
    r = rafael(x, y)
    b = beto(x, y)
    c = carlos(x, y)
    if r > b and r > c:
        res.append('Rafael ganhou')
    elif b > r and b > c:
        res.append('Beto ganhou')
    else:
        res.append('Carlos ganhou')
for result in res:
    print(result)
