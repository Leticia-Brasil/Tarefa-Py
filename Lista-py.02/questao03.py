# Questão 03 - Análise de Frequência de Palavras


def contar_palavras(frase):
    """Retorna um dicionário com a quantidade de vezes que cada palavra aparece."""
    frase = frase.lower()       # 1. converte para minúsculas
    palavras = frase.split()    # 2. separa as palavras pelos espaços
    contagem = {}

    i = 0
    while i < len(palavras):
        # remove pontuação grudada na palavra (ex: "python," -> "python")
        palavra = palavras[i].strip(".,!?;:\"'()")
        if palavra != "":
            # 3. se já existe, soma 1; se não, começa com 1
            if palavra in contagem:
                contagem[palavra] += 1
            else:
                contagem[palavra] = 1
        i += 1

    return contagem  # 4. retorna o dicionário


def main():
    frase = input("Digite uma frase: ")
    resultado = contar_palavras(frase)

    print("\nFrequência das palavras:")
    for palavra, quantidade in resultado.items():
        print(f"{palavra}: {quantidade}")


main()
