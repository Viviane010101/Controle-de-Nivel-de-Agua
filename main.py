
from colorama import Fore, Style, init

# Inicializa o Colorama para que as cores também funcionem adequadamente

init(autoreset=False)

# Lista com os dados dos cinco níveis, do mais baixo ao mais alto.

NIVEIS_RESERVATORIO = [
    {
        "nivel": 1,
        "situacao": "Muito baixo (crítico)",
        "cor": Fore.RED,
        "mensagem": "ALERTA CRÍTICO: nível de água muito baixo! Verifique o abastecimento.",
    },
    {
        "nivel": 2,
        "situacao": "Baixo",
        "cor": Fore.YELLOW,
        "mensagem": "Atenção: o nível de água está baixo. Monitore o reservatório.",
    },
    {
        "nivel": 3,
        "situacao": "Médio",
        "cor": Fore.GREEN,
        "mensagem": "Nível médio: situação dentro da faixa intermediária.",
    },
    {
        "nivel": 4,
        "situacao": "Alto",
        "cor": Fore.CYAN,
        "mensagem": "Nível alto: reservatório com boa quantidade de água.",
    },
    {
        "nivel": 5,
        "situacao": "Muito alto (alerta)",
        "cor": Fore.BLUE,
        "mensagem": "ALERTA: nível muito alto! Verifique a capacidade do reservatório.",
    },
]


def obter_nivel(nivel_informado):
    """Localiza e retorna os dados correspondentes ao nível informado."""
    for dados_nivel in NIVEIS_RESERVATORIO:
        if dados_nivel["nivel"] == nivel_informado:
            return dados_nivel
    return None


def exibir_nivel(nivel_informado):
    """
    Exibe a situação atual com a cor correspondente.
    Retorna False se o nível não existir; caso contrário, retorna True.
    """
    dados_nivel = obter_nivel(nivel_informado)

    if dados_nivel is None:
        print(Fore.MAGENTA + "Erro: nível de reservatório inválido.")
        return False

    print()
    print(dados_nivel["cor"] + "=" * 58)
    print(dados_nivel["cor"] + f" NÍVEL {dados_nivel['nivel']} — {dados_nivel['situacao']}")
    print(dados_nivel["cor"] + dados_nivel["mensagem"])
    print(dados_nivel["cor"] + "=" * 58)
    return True


def restaurar_estilo_terminal():
    """Restaura o estilo padrão do terminal após a exibição das mensagens."""
    print(Style.RESET_ALL, end="")


def exibir_todos_os_niveis():
    """Mostra os cinco níveis para facilitar a compreensão da simulação."""
    print("NÍVEIS DISPONÍVEIS")
    for dados_nivel in NIVEIS_RESERVATORIO:
        print(f"{dados_nivel['nivel']} - {dados_nivel['situacao']}")


def executar_monitoramento():
    """Executa a simulação usando valores definidos no próprio código."""
    print("=" * 58)
    print(" SISTEMA DE MONITORAMENTO DE NÍVEIS DE ÁGUA")
    print("=" * 58)
    print("Simulação acadêmica: os níveis são definidos no código.")
    print("A atividade não exige entrada de dados pelo usuário.")
    print()

    exibir_todos_os_niveis()

    # Valores predefinidos para simular a leitura do reservatório.
    # Altere esta lista para testar diferentes sequências de níveis.
    leituras_simuladas = [1, 2, 3, 4, 5]

    print("\nINICIANDO MONITORAMENTO...")
    for nivel_atual in leituras_simuladas:
        exibir_nivel(nivel_atual)
        restaurar_estilo_terminal()

    print("\nMonitoramento concluído.")
    print("Obrigado por acompanhar a simulação!")
    print("Sugestões de melhoria são bem-vindas.")


# Executa o programa somente quando este arquivo é iniciado diretamente.
if __name__ == "__main__":
    executar_monitoramento()
