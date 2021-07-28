from random import randint
n = randint(0, 5)
adv = int(input('Tente advinhar o número que pensei, uma dica: está entre 0 e 5: '))
if adv == n:
    print('Você acertou, parabéns!')
else:
    print('Você errou, mais sorte da próxima vez!')
