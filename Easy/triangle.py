a,b,c = map(float, input().split())
if a >= b+c or b >= a+c or c >= a+b:
    print(f'Area = {((a+b)*c/2):.1f}')
else:
    print(f'Perimetro = {(a+b+c):.1f}')