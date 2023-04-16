from random import randint
from time import sleep
from playsound import playsound

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
playsound(r'C:\Users\marcu\Downloads\Projetos\Jokenpo\jokenpo.mp3')
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')

print('-=' * 11)
print(f'O COMPUTADOR jogou {itens[computador]}')
print(f'O JOGADOR jogou {itens[jogador]}')
print('-=' * 11)

if computador == 0:  # PEDRA    
    if jogador == 0:
        print('EMPATE')
        playsound(r'C:\Users\marcu\Downloads\Projetos\Jokenpo\empate.mp3')
    elif jogador == 1:
        print('JOGADOR VENCE')
        playsound(r'C:\Users\marcu\Downloads\Projetos\Jokenpo\jogadorvence.mp3')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
        (r'C:\Users\marcu\Downloads\Projetos\Jokenpo\computadorvence.mp3')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:  # PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
        (r'C:\Users\marcu\Downloads\Projetos\Jokenpo\computadorvence.mp3')
    elif jogador == 1:
        print('EMPATE')
        playsound(r'C:\Users\marcu\Downloads\Projetos\Jokenpo\empate.mp3')
    elif jogador == 2:
        print('JOGADOR VENCE')
        playsound(r'C:\Users\marcu\Downloads\Projetos\Jokenpo\jogadorvence.mp3')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:  # TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
        playsound(r'C:\Users\marcu\Downloads\Projetos\Jokenpo\jogadorvence.mp3')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
        (r'C:\Users\marcu\Downloads\Projetos\Jokenpo\computadorvence.mp3')
    elif jogador == 2:
        print('EMPATE')
        playsound(r'C:\Users\marcu\Downloads\Projetos\Jokenpo\empate.mp3')
    else:
        print('JOGADA INVÁLIDA')