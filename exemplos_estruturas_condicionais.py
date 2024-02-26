#Para entrar na festa você tem que ser maior de idade, ter um codinome com menos de 5 letras e saber a palavra-chave da festa!

idade = int(input("Digite a sua idade: "))

if idade < 18:
    print("Você é menor de idade!")
else:
    print("Você é maior de idade!")

codinome = input("Digite o seu codinome: ")
if len(codinome) > 5:
    print("Seu codinome é muito grande!")
else:
    print("Seu codinome é aceito!")

palavra_chave = input("Digite a palavra-chave: ")
if palavra_chave == "abacaxi":
    print("Você acertou a palavra-chave!")
else:
    print("Você errou a palavra-chave!")

if idade >= 18 and len(codinome) <= 5 and palavra_chave == "abacaxi":
    print("Parabéns! Você pode entrar na festa!")
else:
    print("Você não pode entrar na festa!")
# The code above is a simple example of how to use conditional structures.
