import argparse
import sys


def cripto_sub(key, v_modo, v_manter_char, v_bloco):
    criptotexto = ""
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    with open('nome_arquivo.txt', 'r') as file:
        text = file.readline()

  # passar pelo texto do arquivo
    for velho_char in text:
        novo_char = ""

        # se for character for alphabético cifra
        if(velho_char in alfabeto):
            index = alfabeto.index(velho_char)

            if(v_modo):  # se selecionara Encriptar
                new_index = (index + key) % len(alfabeto)

            else:  # se selecionar Decriptar
                new_index = (index - key) % len(alfabeto)

            novo_char = alfabeto[new_index]

        # se for character não for alphabético mantém ou não
        else:
            if(not v_manter_char):
                continue
            else:
                if(v_bloco and v_modo):
                    if(velho_char != " "):
                        novo_char = velho_char
                    else:
                        continue
                else:
                    novo_char = velho_char

        criptotexto = criptotexto + novo_char

        # se bloco for verdadeiro, da espaço a cada 5 characters
        if(v_bloco and v_modo):
            if(len(criptotexto.replace(" ", "")) % 5 == 0):
                criptotexto = criptotexto + " "

        # salvar novo texto no arquivo
    with open('nome_arquivo.txt', 'w') as arquivo_cripto:
        arquivo_cripto.write(criptotexto)

# mostra quando concluída ação na tela


print('Programa concluído')


if __name__ == "__main__":

    # adicionando argumentos na linha de comando
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-k", "--key", help="Chave para encriptar / decriptar", type=int)
    parser.add_argument("-e", "--encriptar", dest="modo", action="store_true")
    parser.add_argument("-d", "--decriptar", dest="modo", action="store_false")
    parser.add_argument("-b", "--bloco",
                        dest="bloco", action="store_true")
    parser.add_argument("-ma", "--manter-char", help="manter char não alfabético",
                        dest="manter_char", action="store_true")

    if len(sys.argv) == 1:
        sys.exit(1)

    args = parser.parse_args()

    cripto_sub(args.key, args.modo, args.manter_char, args.bloco)
