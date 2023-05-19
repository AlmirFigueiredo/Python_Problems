value = float(input())
value *= 100  
value = int(value)  

hundreds = fifties = twenties = tens = fives = twos = ones = fifty_cents = quarter = ten_cents = five_cents = one_cents = 0

while(value >= 10000):
    value -= 10000
    hundreds += 1
while(value >= 5000):
    value -= 5000
    fifties += 1
while(value >= 2000):
    value -= 2000
    twenties += 1
while(value >= 1000):
    value -= 1000
    tens += 1
while(value >= 500):
    value -= 500
    fives += 1
while(value >= 200):
    value -= 200
    twos += 1
while(value >= 100):
    value -= 100
    ones += 1
while(value >= 50):
    value -= 50
    fifty_cents += 1
while(value >= 25):
    value -= 25
    quarter += 1
while(value >= 10):
    value -= 10
    ten_cents += 1
while(value >= 5):
    value -= 5
    five_cents += 1
while(value >= 1):
    value -= 1
    one_cents += 1

print('NOTAS:')
print(f'{hundreds} nota(s) de R$ 100.00')
print(f'{fifties} nota(s) de R$ 50.00')
print(f'{twenties} nota(s) de R$ 20.00')
print(f'{tens} nota(s) de R$ 10.00')
print(f'{fives} nota(s) de R$ 5.00')
print(f'{twos} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{ones} moeda(s) de R$ 1.00')
print(f'{fifty_cents} moeda(s) de R$ 0.50')
print(f'{quarter} moeda(s) de R$ 0.25')
print(f'{ten_cents} moeda(s) de R$ 0.10')
print(f'{five_cents} moeda(s) de R$ 0.05')
print(f'{one_cents} moeda(s) de R$ 0.01')
