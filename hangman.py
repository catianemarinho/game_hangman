from visual import visual_dict
import random

def escolha_palavra():

    with open("palavras.txt", encoding="utf-8") as file:
        lista_palavras = file.readlines()
        lista_palavras = [palavra.strip().upper() for palavra in lista_palavras]

    return random.choice(lista_palavras)

def iniciar_jogo():
    palavra_secreta = escolha_palavra()
    letras_palavra = set(palavra_secreta)
    palpites = set()
    acertos = set()
    tentativas = 7

    print("Descubra a palavra secreta!\n")
    
    while len(letras_palavra) > 0 and tentativas > 0:

        painel = [letra if letra in acertos else "_" for letra in palavra_secreta]
        print(" ".join(painel))

        if len(palpites) > 0:
            print(f"\nLetras já escolhidas: {' '.join(palpites)}")

        print(f"Tentativas: {tentativas}")

        palpite = input(f"Escolha uma letra: ").upper()

        if len(palpite) > 2:
            print("Só pode escolher uma letra!")
        else:
            if palpite in palpites:
                print("Você já escolheu essa letra! Escolha outra!")
            elif palpite in letras_palavra:
                acertos.add(palpite)
                letras_palavra.remove(palpite)
            else:
                print(f"A palavra secreta não contém a letra '{palpite}'!")
                tentativas -= 1
                print(visual_dict[tentativas])

        palpites.add(palpite)

    if tentativas == 0:
        print(f"Você perdeu! A palavra secreta era: '{palavra_secreta}'")
    else:
        print(f"Parabéns! Você acertou a palavra secreta: '{palavra_secreta}'")




iniciar_jogo()