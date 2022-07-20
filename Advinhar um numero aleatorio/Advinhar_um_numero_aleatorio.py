import random

def gera():
    return random.randint(1,100)

def game():
    palpite = gera()
    tentativa = 0 
    print("-------BORA ADVINHAR QUAL NUMERO FOI GERADO    -------------")
    print("-------               BORA JORGAR                    -------")
    print("Palpite Gerado!!!!!")
    print("Boa Sorte!!!!!")
    print("Após acertar vamos ver quantas tentativas foram realizadas")

    chute = 0
    while chute is not palpite:
        tentativa = (tentativa + 1)
        chute =int(input("Qual o seu Palpite: "))
        if chute > palpite:
            print("ERROU! É um valor menor que ", chute)
        elif chute < palpite:
            print("ERROU! É um valor maior que ", chute)
        else:
            print("PARABENS! O numero esta correto!!! o palpite gerado é:", palpite)
            print("Acertou em ", tentativa, "tentativas!")

while True:
    game()
