# Questão 06 - Carrinho de Compras


def calcular_total(carrinho):
    """Percorre os produtos e retorna o valor total da compra."""
    total = 0  # acumulador
    for produto in carrinho:
        total += produto["quantidade"] * produto["preco"]
    return total


def ler_inteiro_positivo(mensagem):
    """Pede um número inteiro maior que zero."""
    while True:
        try:
            valor = int(input(mensagem))
            if valor > 0:
                return valor
            print("O valor deve ser maior que zero!")
        except ValueError:
            print("Valor inválido! Digite um número inteiro.")


def ler_preco(mensagem):
    """Pede um preço maior que zero."""
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if valor > 0:
                return valor
            print("O preço deve ser maior que zero!")
        except ValueError:
            print("Valor inválido! Digite um número.")


def exibir_carrinho(carrinho):
    print("\n=== CARRINHO ===")
    for produto in carrinho:
        subtotal = produto["quantidade"] * produto["preco"]
        print(f"{produto['nome']} - {produto['quantidade']} x R$ {produto['preco']:.2f} = R$ {subtotal:.2f}")


def main():
    carrinho = []  # lista de dicionários
    continuar = "s"

    while continuar == "s":
        nome = input("Nome do produto: ").strip()
        if nome == "":
            print("O nome não pode ficar vazio!\n")
            continue

        produto = {
            "nome": nome,
            "quantidade": ler_inteiro_positivo("Quantidade: "),
            "preco": ler_preco("Preço unitário: R$ "),
        }
        carrinho.append(produto)

        continuar = input("Adicionar outro produto? (s/n): ").strip().lower()
        print()

    exibir_carrinho(carrinho)
    print(f"\nTotal da compra: R$ {calcular_total(carrinho):.2f}")


main()
