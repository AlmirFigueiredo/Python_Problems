init_hour, init_min, final_hour, final_min = map(int, input().split())
minutes = 0
init_time = init_hour * 60 + init_min
final_time = final_hour * 60 + final_min

if final_time > init_time:
    minutes = final_time - init_time
elif final_time < init_time:
    minutes = (24 * 60 - init_time) + final_time
else:
    minutes = 24 * 60  

hours = minutes // 60
minutes = minutes % 60

print(f'O JOGO DUROU {hours} HORA(S) E {minutes} MINUTO(S)')
