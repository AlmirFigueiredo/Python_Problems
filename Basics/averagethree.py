a, b, c, d = map(float, input().split())
a *= 2
b *= 3
c *= 4
media = (a+b+c+d)/10
print(f'Media: {media:.1f}')
if media <= 4.9:
    print('Aluno reprovado.')
elif media < 7:
    print('Aluno em exame.')
    final = float(input())
    print(f'Nota do exame: {final:.1f}')
    media_final = (final + media)/2
    if media_final >= 5:
        print(f'Aluno aprovado.')
    else: 
        print(f'Aluno reprovado.')
    print(f'Media final: {media_final:.1f}')
else:
    print('Aluno aprovado.')