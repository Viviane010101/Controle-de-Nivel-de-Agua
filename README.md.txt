# 💧 Controle de Níveis de Água

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen)
![Projeto acadêmico](https://img.shields.io/badge/projeto-acad%C3%AAmico-blue)
![Licença](https://img.shields.io/badge/licen%C3%A7a-MIT-lightgrey)

Projeto acadêmico em Python para simular o monitoramento do nível de água de um reservatório diretamente no terminal. O programa apresenta alertas coloridos conforme o nível identificado.

## 📋 Requisitos da atividade atendidos

- [x] Utiliza uma lista para armazenar os níveis e suas informações.
- [x] Importa e utiliza a biblioteca `colorama`.
- [x] Possui uma função que define/exibe a mensagem e a cor conforme o nível.
- [x] Exibe a situação do reservatório no terminal com a cor correspondente.
- [x] Restaura o estilo padrão do terminal após cada mensagem.
- [x] Trabalha com cinco níveis, do mais baixo ao mais alto.
- [x] Utiliza dados de simulação definidos no código, sem solicitar entrada do usuário.

## 🚦 Níveis do reservatório

| Nível | Situação | Cor | Tipo de mensagem |
|---|---|---|---|
| 1 | Muito baixo (crítico) | Vermelho | Alerta crítico de nível baixo |
| 2 | Baixo | Amarelo | Atenção e monitoramento |
| 3 | Médio | Verde | Situação intermediária |
| 4 | Alto | Ciano | Boa quantidade de água |
| 5 | Muito alto (alerta) | Azul | Alerta para verificar a capacidade |

## 🗂️ Estrutura dos arquivos

```text
controle-niveis-agua/
├── main.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## ▶️ Como executar

É necessário ter Python 3.10 ou superior instalado.

1. Baixe ou clone este repositório.
2. Abra o terminal na pasta do projeto.
3. (Opcional, recomendado) Crie e ative um ambiente virtual.
4. Instale a dependência:

   ```bash
   pip install -r requirements.txt
   ```

5. Execute:

   ```bash
   python main.py
   ```

## 🧪 Como testar

Por padrão, o programa executa uma leitura simulada de cada nível:

```python
leituras_simuladas = [1, 2, 3, 4, 5]
```

Para testar outros cenários, altere a lista no arquivo `main.py`. Por exemplo:

```python
leituras_simuladas = [1, 1, 2, 5, 4, 3]
```

Assim, é possível verificar a apresentação dos alertas em diferentes sequências.

## 🧠 Conceitos praticados

- Listas e dicionários
- Funções
- Laço de repetição `for`
- Condicionais
- Importação e uso de biblioteca externa
- Organização e comentários no código
- Simulação de monitoramento

## 💡 Possíveis melhorias

- Ler o nível a partir de um sensor real.
- Registrar data e hora de cada leitura.
- Salvar o histórico em arquivo CSV.
- Criar uma interface gráfica ou painel web.
- Emitir notificações quando o nível estiver crítico.

## 🎓 Sobre o projeto

Atividade acadêmica da Agenda 11 – Desenvolvimento de Sistemas. O projeto tem finalidade didática e simula leituras; ele não está conectado a um reservatório ou sensor real.

## 📄 Licença

Este projeto é disponibilizado sob a licença MIT. Consulte o arquivo `LICENSE`.
