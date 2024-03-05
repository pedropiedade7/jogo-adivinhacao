def jogo_adivinhacao():
    numero_secreto = 50
    tentativas = 5

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100.")
    print(f"Você tem {tentativas} tentativas.")

    while tentativas > 0:
        chute = int(input("Digite seu chute: "))

        if chute < numero_secreto:
            print("O número secreto é maior.")
        elif chute > numero_secreto:
            print("O número secreto é menor.")
        else:
            print("Parabéns! Você acertou!")
            return

        tentativas -= 1
        if tentativas > 0:
            print(f"Você tem mais {tentativas} tentativas.")

    print("Suas tentativas acabaram. O número secreto era:", numero_secreto)


jogo_adivinhacao()
