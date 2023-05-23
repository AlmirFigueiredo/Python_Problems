a = []
b = []
results = []

while True:
    try:
        numbers = input()
        if len(numbers.split()) < 2:
            break
        a_num, b_num = numbers.split()
        a.append(int(a_num))
        b.append(int(b_num))
    except EOFError:
        break

def factorial_calculator(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_calculator(n - 1)

for i in range(len(a)):
    result = factorial_calculator(a[i]) + factorial_calculator(b[i])
    results.append(result)

for index in range(len(results)):
    print(results[index])
