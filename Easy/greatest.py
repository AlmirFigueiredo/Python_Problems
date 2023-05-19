a,b,c = map(int, input().split())
def get_greatest(i, j):
    return int((i+j+abs(i-j))/2)
print(f'{get_greatest(get_greatest(a,b), c)} eh o maior')
 