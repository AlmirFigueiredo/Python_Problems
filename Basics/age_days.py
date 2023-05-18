n = int(input())
years = months = days = 0
while(n >= 365):
    n -= 365
    years += 1
while(n >= 30):
    n -= 30
    months += 1
days = n
print(f'{years} ano(s)')
print(f'{months} mes(es)')
print(f'{days} dia(s)')
