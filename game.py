import random

numero_sorteado = random.randint(1, 100)

print("Bem-vindo ao jogo de adivinhação!")
print("Sorteamos um número entre 1 e 100. Tente adivinhar!")

tentativa = int(input("Digite o seu palpite: "))

#enquanto a tentativa for diferente do número sorteado:
#   se a tentativa for maior que o número sorteado:
#       imprima "O número sorteado é menor!"
#   senão:
#       imprima "O número sorteado é maior!"
#   peça para o usuário digitar um novo palpite

# print(f"Parabéns você acertou! O número sorteado é {numero_sorteado}!")
