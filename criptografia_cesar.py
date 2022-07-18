import sys

ciphertext = ""
alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
key = int(input('Entre com o valor da chave (deslocamento), deve ser um número inteiro: '))
modo = input('Escolha E para encriptar ou D para decriptar o texto: ')
bloco = input('Escolha V se deseja dividir o texto em bloco ou F se não deseja: ')
manter_char = input('Escolha M para manter character especiais ou N para não manter: ')

with open('nome_arquivo.txt', 'r') as file:
    text = file.readline()

# passar pelo texto do arquivo
for old_character in text:
    new_character = ""

    # se for character for alphabético cifra
    if(old_character in alphabet):
        index = alphabet.index(old_character)

        if(modo == 'E'):  # se selecionar Encriptar
            new_index = (index + key) % len(alphabet)

        elif(modo == 'D'):  # se selecionar Decriptar
            new_index = (index - key) % len(alphabet)

        new_character = alphabet[new_index]
    # se for character não for alphabético mantém ou não
    else:
        if(manter_char == 'N'):
            continue
        elif(manter_char == 'M'):            
            if(bloco == 'V' and modo == 'E'):
                if(old_character != " "):
                    new_character = old_character
                else:
                    continue
            else:
                new_character = old_character

    ciphertext = ciphertext + new_character

        # se bloco for verdadeiro, da espaço a cada 5 characters
    if(bloco == 'V' and modo == 'E'):
        if(len(ciphertext.replace(" ", "")) % 5 == 0):
            ciphertext = ciphertext + " "

    # salvar novo texto no arquivo
with open('nome_arquivo.txt', 'w') as arquivo_cripto:
        arquivo_cripto.write(ciphertext)

# mostra quando concluída ação na tela
if (modo == 'E'):
    print('Arquivo encriptado')
elif(modo == 'D'):
    print('Arquivo decriptado')
