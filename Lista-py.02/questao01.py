# Questão 01 - Sistema de Autenticação

USUARIO_CORRETO = "admin"
SENHA_CORRETA = "Python@2026"
MAX_TENTATIVAS = 3


def autenticar(usuario, senha):
    """Retorna True se usuário e senha estiverem corretos, senão False."""
    return usuario == USUARIO_CORRETO and senha == SENHA_CORRETA


def main():
    tentativas = 0
    autorizado = False

    # Repete enquanto ainda houver tentativas e o usuário não tiver acertado
    while tentativas < MAX_TENTATIVAS and not autorizado:
        usuario = input("Usuário: ")
        senha = input("Senha: ")
        tentativas += 1  # contador de tentativas

        if autenticar(usuario, senha):
            autorizado = True
        else:
            restantes = MAX_TENTATIVAS - tentativas
            if restantes > 0:
                print(f"Usuário ou senha incorretos. Tentativas restantes: {restantes}\n")

    if autorizado:
        print("\nAcesso autorizado! Bem-vindo(a).")
    else:
        print("\nAcesso bloqueado! Número máximo de tentativas excedido.")


main()
