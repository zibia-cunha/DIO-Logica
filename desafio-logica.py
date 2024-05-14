#variáveis

heroi = ''
xp_heroi = ''
nivel = ''

# Laços de Repetição e Estruturas de decisão 
while True:
    heroi = input('Digite seu nome, grande herói: ')
    xp_heroi = input('diga-me, qual é seu XP? ')
    
    if heroi == '' or xp_heroi == '' or xp_heroi == 0: 
        print('Revise suas informações!')
        continue
    elif heroi != '' or xp_heroi != 0:
        break

xp_heroi = int(xp_heroi)

#condição para verificação de nivel 
if xp_heroi <= 1000:
   nivel = 'Ferro'
elif xp_heroi >= 1001 and xp_heroi <= 2000:
    nivel = 'Bronze'
elif xp_heroi >= 2001 and xp_heroi <= 5000:
    nivel = 'Prata'
elif xp_heroi >= 5001 and xp_heroi <= 7000:
    nivel = 'Ouro'
elif xp_heroi >= 7001 and xp_heroi <= 8000:
    nivel = 'Platina'
elif xp_heroi >= 8001 and xp_heroi <= 9000:
    nivel = 'Ascendente'
elif xp_heroi >= 9001 and xp_heroi <= 10000:
    nivel = 'Imortal'
elif xp_heroi >= 10001:
    nivel = 'Radiante'

#Saída
if heroi != '' and xp_heroi != '':
    print('Então, o (a) grande herói(na) de nome {} está no nível de {}'.format(heroi, nivel))
