print("voce esta em uma floresta e precisa escolher se quer direita ou esquerda")
print()
resposta = int(input("Digite (1) se quer ir para esquerda ou (2) para ir para direita"))
if resposta == 1:
    print("Voce encontrou um rio, vc quer atravessar o rio ou volta?")
    print()
    caminho_da_esquerda = int(input('digte (1) se vc quer atravessar o rio ou (2) para voltar'))
    if caminho_da_esquerda == 1:
        print("PARABENS, vc chegou em uma vila segura")
    else:
        print("vc se perdeu na floresta 👎")
elif resposta == 2:
    print("voce encontrou uma motanha!!")
    print()
    caminho_da_direita = int(input("Digite (1) pra subir a montanha e (2) para voltar"))
    if caminho_da_direita == 1:
        print("parabenssss vc encontrou um bau cheio do ouro")
    else:
        print("vc se perdeu na floresta 👎")
else:
    print("renicie o jogo, esse caminho n existe")