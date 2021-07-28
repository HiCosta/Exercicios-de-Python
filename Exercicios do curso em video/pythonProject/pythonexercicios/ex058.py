from random import randint
n = randint(0, 5)
adv = int(input('Tente advinhar o número que pensei, uma dica: está entre 0 e 5: '))
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpite += 1
    if jogador == n:
        acertou = True
print('Acertou com {} tentativas! Fim de jogo'.format(palpite))
