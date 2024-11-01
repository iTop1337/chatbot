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

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
