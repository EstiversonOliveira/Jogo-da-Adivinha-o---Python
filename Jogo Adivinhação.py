from random import randint
tent=0
c=randint(1, 1000)
print('=-'*30)
print('Jogo da Adivinhação')
print('-='*30)
while True:
    j=int(input('Escolhi um número. Tente adivinhar:  '))
    if j>c:
        print('É um número menor. Tente de novo !')
        tent+=1
        continue
    if j<c:
        print('É um número maior! Tente novamente')
        tent+=1
        continue
    if j==c:
        tent+=1
        print('Acertou ! Você precisou de {} tentativas.'.format(tent))
        break
print ('Jogo encerrado')

