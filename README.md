# Quiz Interativo com gRPC — Python & Node.js

## 📚 Descrição Geral

Este projeto é um sistema de **Quiz interativo** que utiliza o protocolo **gRPC** para comunicação eficiente entre um **servidor em Node.js (JavaScript)** e um **cliente em Python**. O objetivo é demonstrar, por meio de um estudo de caso, a transmissão de dados entre duas linguagens distintas utilizando gRPC, conforme requisitos acadêmicos de interoperabilidade, arquitetura e facilidade de teste.

---

## 🏗️ Arquitetura do Sistema

- **gRPC**: Protocolo de comunicação de alta performance baseado em HTTP/2 e Protocol Buffers, permitindo RPC (Remote Procedure Call) entre diferentes linguagens.
- **Servidor**: Implementado em **Node.js (JavaScript)**, responsável por gerenciar sessões, perguntas e respostas do quiz.
- **Cliente**: Implementado em **Python**, responsável por interagir com o usuário, enviar respostas e exibir resultados.
- **Arquivo .proto**: Define o contrato de comunicação (serviços e mensagens) e garante compatibilidade entre as linguagens.

### Diagrama Resumido

```mermaid
graph TD;
  subgraph Cliente (Python)
    CP[quiz_client.py]
  end
  subgraph Servidor (Node.js)
    SN[quiz_server.js]
  end
  subgraph Proto
    P[quiz.proto]
  end
  CP -- gRPC --> SN
  CP -- usa --> P
  SN -- usa --> P
```

---

## 📂 Estrutura de Pastas

```
gRPC-Quiz/
├── proto/
│   └── quiz.proto           # Contrato gRPC (Protocol Buffers)
├── server-javascript/
│   ├── package.json         # Dependências Node.js
│   ├── quiz_server.js       # Servidor gRPC em Node.js
│   └── ...
└── client-python-grpc/
    ├── quiz_client.py       # Cliente gRPC em Python
    ├── quiz_pb2.py          # Código gerado do .proto
    ├── quiz_pb2_grpc.py     # Código gerado do .proto
    └── ...
```

---

## 🛠️ Tecnologias e Linguagens Utilizadas

- **Node.js (JavaScript)**
  - Framework: [@grpc/grpc-js](https://www.npmjs.com/package/@grpc/grpc-js)
  - Protocolo: gRPC
- **Python 3.10 ou 3.11**
  - Bibliotecas: `grpcio`, `grpcio-tools`, `colorama`
  - Protocolo: gRPC
- **Protocol Buffers (.proto)**
  - Define o serviço, métodos e mensagens do quiz

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
- **Node.js** instalado ([download](https://nodejs.org/))
- **Python 3.10 ou 3.11** instalado ([download](https://www.python.org/))
- **pip** (gerenciador de pacotes Python)

### 1. Inicie o Servidor Node.js (JavaScript)

```bash
cd server-javascript
npm install
node quiz_server.js
```
O servidor ficará ouvindo na porta `50051`.

---

### 2. Prepare e Execute o Cliente Python (gRPC)

Abra outro terminal:

```bash
cd client-python-grpc
python -m venv venv
# Ative o ambiente virtual:
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

pip install grpcio grpcio-tools colorama

# Gere os arquivos Python a partir do .proto:
python -m grpc_tools.protoc --proto_path=../proto --python_out=. --grpc_python_out=. ../proto/quiz.proto

# Execute o cliente:
python quiz_client.py
```

---

## 🧩 Como Funciona

- O **cliente Python** conecta-se ao **servidor Node.js** via gRPC, usando o contrato definido em `proto/quiz.proto`.
- O **servidor** gerencia sessões, perguntas e respostas do quiz, mantendo o estado em memória.
- O **cliente** apresenta perguntas ao usuário, envia respostas e exibe o resultado final.
- Toda a comunicação é binária, eficiente e multiplataforma graças ao gRPC.

---

## 📑 Detalhes do Arquivo .proto

O arquivo `proto/quiz.proto` define:
- O serviço `QuizService` com métodos:
  - `StartQuiz`, `GetQuestion`, `SubmitAnswer`, `FinishQuiz`
- As mensagens trocadas entre cliente e servidor (requisições e respostas)
- Isso garante que ambos os lados "falam a mesma língua", mesmo em linguagens diferentes.

---

## ✅ Por que este sistema atende a todos os requisitos?

- **Transmissão de dados com gRPC:**
  - Toda a comunicação entre cliente e servidor é feita exclusivamente via gRPC, usando um arquivo `.proto` compartilhado.
- **Duas linguagens diferentes:**
  - O servidor é implementado em **JavaScript (Node.js)** e o cliente em **Python**.
- **Arquitetura clara e demonstrável:**
  - Projeto organizado, diagrama, explicação do fluxo e separação de responsabilidades.
- **Fácil de rodar e testar:**
  - Passos simples, dependências mínimas, multiplataforma.
- **Pronto para Github e apresentação:**
  - Estrutura limpa, documentação clara e dependências mínimas.
- **Estudo de caso:**
  - Implementação de um quiz interativo, facilmente adaptável para outros cenários sugeridos (transmissão de arquivos, jogos, etc).

---

## 💡 Observações

- A pasta `server-python-rest/` não é utilizada no sistema gRPC e pode ser removida.
- O script em `scripts/` é opcional e não é necessário para rodar o sistema gRPC.
- O projeto pode ser facilmente expandido para outros estudos de caso apenas alterando o arquivo `.proto` e a lógica do servidor/cliente.

---

## 👨‍💻 Autor e Licença

- Projeto para fins acadêmicos.
- Desenvolvido para demonstração de interoperabilidade e RPC entre linguagens. 