print("BEM VINDO A CALCULADORA")
print()
print("para começar escolha um modo da calculadora:")
print(" 1: soma"
    "   2: subtração"
    "   3: multiplicação"
"       4: divisão"
"       0: sair")
comeco = int(input("Digite o numero que coresponda aos modos: "))
print()

while True:
    if comeco == 1:
        print("voce escolheu o moda soma")
        x = int(input("Digite o primeiro numero: "))
        y = int(input("Agora o outro numero: "))
        soma = x + y
        print()
        print(f"{x} + {y} = {soma}")
        print()
        print("(1)SOMA / (2)SUBTRAÇÃo / (3)MULTIPLICAÇÃO / (4)DIVISÃo / (0)SAIR ")
        
    elif comeco == 2:
        print("Voce escolheu o moto subtração")
        x = int(input("Digite o primeiro numero: "))
        y = int(input("Agora o outro numero: "))
        sub = x - y
        print()
        print(f"O RESULTADO DEU: {x} - {y} = {sub}")
        print()
        print("(1)SOMA / (2)SUBTRAÇÃo / (3)MULTIPLICAÇÃO / (4)DIVISÃo / (0)SAIR ")
        comeco = int(input("Digite um novo modo, ou o mesmo modo ou se gostaria de sair: "))
    
    elif comeco == 3:
        print("MODO MULTIPLICAÇÃO")
        x = int(input("Digite o primeiro numero: "))
        y = int(input("Agora o outro numero: "))
        multi = x * y
        print()
        print(f"O RESULTADO DEU: {x} x {y} = {multi}")
        print()
        print("(1)SOMA / (2)SUBTRAÇÃo / (3)MULTIPLICAÇÃO / (4)DIVISÃo / (0)SAIR ")
        comeco = int(input("Digite um novo modo, ou o mesmo modo ou se gostaria de sair: "))
    
    elif comeco == 4:
        print("MODO DIVISÃO")
        x = int(input("Digite o primeiro numero: "))
        y = int(input("Agora o outro numero: "))
        div = x / y
        print()
        print(f"O RESULTADO DEU: {x} / {y} = {div}")
        print()
        print("(1)SOMA / (2)SUBTRAÇÃo / (3)MULTIPLICAÇÃO / (4)DIVISÃo / (5)RESTO DE DIVISÃO / (0)SAIR ")
        comeco = int(input("Digite um novo modo, ou o mesmo modo ou se gostaria de sair: "))

    elif comeco == 4:
        print("MODO DIVISÃO")
        x = int(input("Digite o primeiro numero: "))
        y = int(input("Agora o outro numero: "))
        div = x / y
        print()
        print(f"O RESULTADO DEU: {x} / {y} = {div}")
        print()
        print("(1)SOMA / (2)SUBTRAÇÃo / (3)MULTIPLICAÇÃO / (4)DIVISÃo / (5)RESTO DE DIVISÃO / (0)SAIR ")
        comeco = int(input("Digite um novo modo, ou o mesmo modo ou se gostaria de sair: "))

    elif comeco == 4:
        print("MODO DIVISÃO")
        x = int(input("Digite o primeiro numero: "))
        y = int(input("Agora o outro numero: "))
        div = x / y
        print()
        print(f"O RESULTADO DEU: {x} / {y} = {div}")
        print()
        print("(1)SOMA / (2)SUBTRAÇÃo / (3)MULTIPLICAÇÃO / (4)DIVISÃo / (5)RESTO DE DIVISÃO / (0)SAIR ")
        comeco = int(input("Digite um novo modo, ou o mesmo modo ou se gostaria de sair: "))

    elif comeco == 4:
        print("MODO DIVISÃO")
        x = int(input("Digite o primeiro numero: "))
        y = int(input("Agora o outro numero: "))
        div = x / y
        print()
        print(f"O RESULTADO DEU: {x} / {y} = {div}")
        print()
        print("(1)SOMA / (2)SUBTRAÇÃo / (3)MULTIPLICAÇÃO / (4)DIVISÃo / (5)RESTO DE DIVISÃO / (0)SAIR ")
        comeco = int(input("Digite um novo modo, ou o mesmo modo ou se gostaria de sair: "))

    elif comeco == 5:
        print("MODO RESTO DE DIVISÃO")
        x = int(input("Digite o primeiro numero: "))
        y = int(input("Agora o outro numero: "))
        resto = x % y
        print()
        print(f"O RESTO DA DIVISÃO DE {x} E {y} É {resto}")
        print()
        print("(1)SOMA / (2)SUBTRAÇÃo / (3)MULTIPLICAÇÃO / (4)DIVISÃo / (5)RESTO DE DIVISÃO / (0)SAIR ")
        comeco = int(input("Digite um novo modo, ou o mesmo modo ou se gostaria de sair: "))
    
    elif comeco == 0:
        print("SAINDO DA CALCULADORA...")
        break

    else:
        print("VOCÊ DIGITOU MODOS QUE NÃO EXISTE, PFV TENTE NOVAMENTE")
        print()
        print("(1)SOMA / (2)SUBTRAÇÃo / (3)MULTIPLICAÇÃO / (4)DIVISÃo / (5)RESTO DE DIVISÃO / (0)SAIR ")
        print()
        comeco = int(input("Digite um novo modo, ou o mesmo modo ou se gostaria de sair: "))


    