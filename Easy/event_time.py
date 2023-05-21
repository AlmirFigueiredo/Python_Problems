day1 = int(input().split()[1])
d1 = input()
day2 = int(input().split()[1])
d2 = input()

init_hour = int(d1.split()[0])
init_min = int(d1.split()[2])
init_sec = int(d1.split()[4])

final_hour = int(d2.split()[0])
final_min = int(d2.split()[2])
final_sec = int(d2.split()[4])

init = 86400 * day1 + init_hour*3600 + init_min * 60 + init_sec
final = 86400 * day2 + final_hour*3600 + final_min * 60 + final_sec
difference = final - init
d = h = m = s = 0
while(difference >= 86400):
    d += 1
    difference -= 86400
while(difference >= 3600):
    h += 1
    difference -= 3600
while(difference >= 60):
    m += 1
    difference -= 60
s = difference
print(f'{d} dia(s)')
print(f'{h} hora(s)')
print(f'{m} minuto(s)')
print(f'{s} segundo(s)')

