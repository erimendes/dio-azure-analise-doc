# 💳 Azure AI & Streamlit: Detector de Fraudes em Cartões de Crédito

Este projeto foi desenvolvido como parte de um desafio da **DIO (Digital Innovation One)**. A aplicação utiliza o **Azure Document Intelligence** para analisar imagens de cartões de crédito, extrair informações relevantes (Número, Nome e Validade) e validar documentos.

## 🚀 Funcionalidades

* **Upload Seguro:** Envio de imagens diretamente para o Azure Blob Storage.
* **Análise Inteligente:** Uso do modelo `prebuilt-read` do Azure AI para extração de texto bruto.
* **Regex Engine:** Lógica customizada para identificar Números de Cartão e Nomes de Titulares.
* **Interface Streamlit:** UI moderna e responsiva.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.10+**
* **Streamlit**
* **Azure AI Document Intelligence**
* **Azure Blob Storage**
* **Poetry** (Gerenciamento de dependências)

---

## ⚙️ Configuração e Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/dio-azure-analise-doc.git](https://github.com/seu-usuario/dio-azure-analise-doc.git)
    cd dio-azure-analise-doc
    ```

2.  **Instale as dependências:**
    ```bash
    poetry install
    ```

3.  **Configuração de Segurança (.env):**
    O projeto utiliza um arquivo `.env` para armazenar chaves sensíveis. **Nunca envie este arquivo para o repositório.** Ele já está incluído no `.gitignore`.
    Crie o arquivo na raiz do projeto:
    ```env
    ENDPOINT=[https://seu-recurso.cognitiveservices.azure.com/](https://seu-recurso.cognitiveservices.azure.com/)
    SUBSCRIPTION_KEY=sua_chave_aqui
    AZURE_STORAGE_CONNECTION_STRING=sua_connection_string_completa
    CONTAINER_NAME=cartoes
    ```

---

## 🖥️ Como Executar

Inicie a aplicação:
```bash
poetry run streamlit run src/app.py
```

Gerando Dependências (Requirements)
Caso precise gerar o arquivo requirements.txt para deploy:

```Bash
poetry run pip freeze > requirements.txt
```

---

## 🏗️ Estrutura do Projeto
```Bash
.
├── src/
│   ├── app.py                 # Interface Streamlit
│   ├── services/
│   │   ├── blob_service.py    # Integração Storage
│   │   └── credit_card_service.py # Lógica de IA e Regex
│   └── utils/
│       └── Config.py          # Leitura do .env
├── .env                       # Chaves privadas (Ignorado pelo git)
├── .gitignore                 # Filtro de arquivos para o Git
├── pyproject.toml             # Configurações Poetry
└── requirements.txt           # Dependências exportadas
```

---

## ✍️ Autor
Desenvolvido por Francisco - Desafio DIO: Analisando documentos antivulneráveis com Azure AI.

---