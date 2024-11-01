# Documentação do Chatbot com FAISS

Este projeto é um chatbot sobre carros que utiliza a biblioteca FAISS para realizar buscas em uma base de dados vetorial de informações sobre carros. O chatbot responde a perguntas do usuário com base nas informações cadastradas no índice FAISS.

## Sumário

- [Pré-requisitos](#pré-requisitos)
- [Instalação e Configuração](#instalação-e-configuração)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Execução da Aplicação](#execução-da-aplicação)
- [Exemplos de Uso](#exemplos-de-uso)
- [Configurações Adicionais](#configurações-adicionais)

## Pré-requisitos

Antes de começar, verifique se você tem o seguinte software instalado:

- [Python 3.8+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/) (opcional, se o Docker Compose for usado)

Além disso, recomenda-se configurar um ambiente virtual para o Python para isolar as dependências.

## Instalação e Configuração

1. **Clone o repositório do projeto** (ou baixe os arquivos do projeto):

bash git clone https://github.com/seu-usuario/seu-repositorio.git

## Estrutura do projeto

├── chatbot/
│   ├── __init__.py
│   ├── chatbot_streamlit.py          # Código principal do chatbot com Streamlit
│   ├── vector_database.py            # Código de configuração do FAISS e indexação
│   ├── docker-compose.yml            # Configuração do Docker
│   ├── requirements.txt              # Dependências do Python
│   └── .env                          # Arquivo de ambiente com chaves de API
├── README.md                         # Documentação e instruções do projeto


## Execução da aplicação 


Inicie o docker:

bash: docker-compose up

   -   Certifique-se de que o serviço FAISS ou Weaviate está ativo no Docker.

Execute o chatbot com Streamlit:

Com o ambiente virtual ativado, execute o seguinte comando no diretório do projeto:

bash: streamlit run chatbot/chatbot_streamlit.py


Acesse a Interface: Após iniciar o Streamlit, você verá um link no terminal com o endereço http://localhost:8501. Acesse esse link para interagir com o chatbot na interface web.


## Exemplos de Uso

Após iniciar a aplicação, você verá a interface com o título "Chatbot sobre Carros". Você pode inserir perguntas como:

Pergunta: "Qual é o melhor carro feito no Brasil?"
Resposta do Bot: "O Marea é o melhor carro feito no Brasil."

Pergunta: "Qual é a frequência para troca de óleo?"
Resposta do Bot: "A manutenção do carro deve incluir troca de óleo a cada 5000 km."


Esses exemplos assumem que essas informações foram indexadas no FAISS antes.


## Configurações Adicionais

Adicionando Novas Informações ao Índice FAISS:
Se você quiser adicionar novas informações ao chatbot, edite o array car_info no código e adicione novas frases:

 ____________________________________________________________________________________________________________________
         car_info = [
             "O Marea é o melhor carro feito no Brasil.",
             "O motor 20V do Marea é o mais potente do Brasil.",
             "A manutenção do carro deve incluir troca de óleo a cada 5000 km.",
             "Carros com transmissão automática costumam ser mais confortáveis para dirigir em trânsito pesado."
            ]
______________________________________________________________________________________________________________________           


## Armazene cada nova informação no índice FAISS
car_info:

Após atualizar o índice, reinicie a aplicação.
