def txt_to_bin(texto):
    binario = ''
    for caractere in texto:
        valor_ascii = ord(caractere)
        binario += format(valor_ascii, '08b') + ' '
    return binario


def bin_to_txt(binario):
    caracteres = binario.split()
    texto = ''
    for caractere_binario in caracteres:
        valor_decimal = int(caractere_binario, 2)
        caractere = chr(valor_decimal)
        texto += caractere
    return texto


def num_to_bin(numero):
    numero = int(numero)
    binary = bin(abs(numero))
    return binary[2:]


def retornar():
    print("Do you want to confirm what you just wrote")
    confirm = int(input("0 = Y / 1 = N"))
    if confirm == 0:
        in_put = input("Write what you got")
        print("Your printed text: " , bin_to_txt(in_put))


# print a chose
print("What do you want to do")
a = int(input("1 to write ===== 2 to read ===== or 3 just convert numbers to bin"))

if a == 1:
    texto = input("Write what you want to convert to Binary")
    resultado = txt_to_bin(texto)
    print("Binary says: ", resultado)
    retornar()

elif a == 2:
    binario = input("Write what you want to convert to Text")
    resultado = bin_to_txt(binario)
    print("Text: " , resultado)

elif a == 3:
    numero = input("Write THE NUMBER you want convert")
    resultado = num_to_bin(numero)
    print(numero,"in Binary is: ", resultado)
else:
    print("something gets wrong")

