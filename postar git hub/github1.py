idade = int(input("Quantos naos vc tem? "))

if idade >= 18:
    ticket = input("E voce tem bilhete? ").lower
    if ticket == "sim" or ticket == "si" or ticket == "s":
        print("pode passar")
    else:
        print("so falto o bilhete")
else:
    print("seus pais sabem oq vc anda fazendo?")
    