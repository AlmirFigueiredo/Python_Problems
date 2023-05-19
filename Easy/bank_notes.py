value = int(input())
hundredes = fifties = twenties = tens = fives = twos = ones = 0
stored = value
while(value != 0):
    while(value >= 100):
        value -= 100
        hundredes += 1
    while(value >= 50):
        value -= 50
        fifties += 1
    while(value >= 20):
        value -= 20
        twenties += 1
    while(value >= 10):
        value -= 10
        tens += 1
    while(value >= 5):
        value -= 5
        fives += 1
    while(value >= 2):
        value -= 2
        twos += 1
    while(value >= 1):
        value -= 1
        ones += 1
print(f'{stored}')
print(f'{hundredes} nota(s) de R$ 100,00')
print(f'{fifties} nota(s) de R$ 50,00')
print(f'{twenties} nota(s) de R$ 20,00')
print(f'{tens} nota(s) de R$ 10,00')
print(f'{fives} nota(s) de R$ 5,00')
print(f'{twos} nota(s) de R$ 2,00')
print(f'{ones} nota(s) de R$ 1,00')