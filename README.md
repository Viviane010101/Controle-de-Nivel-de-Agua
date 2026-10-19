<div align="center">

# 💧 Controle de Níveis de Água

**Simulação em Python para monitoramento de um reservatório**

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Colorama](https://img.shields.io/badge/Colorama-cores%20no%20terminal-2E8B57?style=for-the-badge)
![Projeto acadêmico](https://img.shields.io/badge/Projeto-Acad%C3%AAmico-7B61A8?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-informational?style=for-the-badge)

</div>

---

## 📌 Sobre o projeto

Este projeto foi desenvolvido para a atividade **“Controle de Níveis de Água”**, da Agenda 11 de Desenvolvimento de Sistemas.

O programa simula o monitoramento de um reservatório e apresenta uma mensagem de situação para cada nível de água. Para facilitar a identificação dos alertas, as mensagens são exibidas com cores diferentes no terminal usando a biblioteca **Colorama**.

> **Atenção:** esta é uma simulação acadêmica. O programa não está conectado a sensores nem monitora um reservatório real.

## 🎯 Objetivos da atividade

- Utilizar uma lista para armazenar os níveis e as informações do reservatório.
- Importar e utilizar a biblioteca `colorama`.
- Criar uma função que determine a cor conforme o nível informado.
- Exibir no terminal a situação e a mensagem de alerta correspondentes.
- Restaurar o estilo padrão do terminal após a exibição das mensagens.
- Praticar listas, funções, condicionais e estruturas de repetição.

## 🚦 Níveis monitorados

| Nível | Situação | Cor da mensagem | Significado |
|:---:|---|---|---|
| 1 | Muito baixo (crítico) | 🔴 Vermelho | Alerta crítico: verificar o abastecimento |
| 2 | Baixo | 🟡 Amarelo | Atenção: acompanhar o nível |
| 3 | Médio | 🟢 Verde | Situação intermediária |
| 4 | Alto | 🩵 Ciano | Reservatório com boa quantidade de água |
| 5 | Muito alto (alerta) | 🔵 Azul | Verificar a capacidade do reservatório |

## 🧰 Tecnologias utilizadas

- **Python** — lógica, funções, listas e repetição.
- **Colorama** — exibição de cores no terminal.
- **Git e GitHub** — versionamento e publicação do projeto.

## 📁 Estrutura do repositório

```text
controle-niveis-agua/
├── main.py            # Código principal, comentado
├── requirements.txt   # Dependências do projeto
├── README.md          # Documentação
├── .gitignore         # Arquivos que não devem ser versionados
└── LICENSE            # Licença do projeto
```

## ⚙️ Como instalar e executar

### 1. Verifique o Python

Recomenda-se Python 3.10 ou superior.

```bash
python --version
```

### 2. Baixe o projeto

Clone o repositório ou baixe os arquivos pelo GitHub.

```bash
git clone URL_DO_SEU_REPOSITORIO
cd controle-niveis-agua
```

Substitua `URL_DO_SEU_REPOSITORIO` pelo endereço real do repositório.

### 3. Instale a dependência

```bash
pip install -r requirements.txt
```

### 4. Execute o programa

```bash
python main.py
```

O programa exibirá os níveis simulados no terminal, cada um com sua mensagem e cor correspondente.

## 🧪 Como testar outros cenários

No arquivo `main.py`, localize a lista `leituras_simuladas`:

```python
leituras_simuladas = [1, 2, 3, 4, 5]
```

Para testar uma sequência diferente, você pode alterá-la, por exemplo:

```python
leituras_simuladas = [1, 1, 2, 5, 4, 3]
```

Salve o arquivo e execute novamente. A lista representa leituras fictícias usadas para testar o comportamento do programa.

## 🧠 Conceitos de programação praticados

| Conceito | Aplicação no projeto |
|---|---|
| Listas e dicionários | Armazenam os dados dos níveis |
| Funções | Organizam a busca, a definição de cores e a exibição |
| Condicionais | Tratam níveis válidos e inválidos |
| Laço `for` | Percorre os níveis e as leituras simuladas |
| Biblioteca externa | Colorama aplica cores às mensagens |
| Comentários | Explicam as principais partes do código |

## 💡 Possíveis melhorias

- Integrar o programa a um sensor real de nível de água.
- Registrar a data e o horário de cada leitura.
- Salvar o histórico de monitoramento em um arquivo CSV.
- Criar uma interface gráfica ou um painel web.
- Adicionar notificações para níveis críticos.
- Permitir que os níveis sejam recebidos de uma fonte externa.

## 🎓 Contexto acadêmico

Atividade prática da **Agenda 11 — Desenvolvimento de Sistemas**, com foco na aplicação de conceitos de programação estruturada, organização de código e uso de bibliotecas.

## 📄 Licença

Este projeto utiliza a licença MIT. Consulte o arquivo [`LICENSE`](LICENSE) para conhecer os termos.

---

<div align="center">

Feito para fins de estudo e prática em Python 💧

</div>
