# Projeto Cloud/IoT

Este projeto contém uma API em Python e utiliza o **localtunnel** para expor o servidor localmente. 

## Pré-requisitos

- Python 3.8 ou superior
- Node.js e npm
- Virtualenv (ou outra ferramenta de ambientes virtuais para Python)

## Configuração

### 1. Clonar o repositório

```bash
git clone https://github.com/henricosta/sensor-gas-iot
cd sensor-gas-iot
```

### 2. Configurar o ambiente virtual Python

1. No diretório do projeto, crie um ambiente virtual:
   ```bash
   python3 -m venv venv
   ```

2. Ative o ambiente virtual:

     ```bash
     .\venv\Scripts\activate
     ```

3. Instale as dependências do Python:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Iniciar a API

Após a instalação das dependências, inicie a API executando o arquivo `app.py`, que está localizado em `api/`:
   ```bash
   python api/app.py
   ```

### 4. Instalar o Localtunnel

**Em outro terminal**. Instale o Localtunnel localmente usando npm:
```bash
npm install localtunnel
```

### 5. Configurar o Tunnel com Localtunnel

Em uma nova janela do terminal, execute o Localtunnel para expor a API:

```bash
npx localtunnel --port 8080
```

Depois disso acesse a url do projeto que é fornecido no terminal no navegador. Ou substituia a url no arquivo `sketch.ino` para testar ela pelo ESP32.

---

Os arquivos do Wokwi estão na pasta `wokwi/` que incluem `diagram.json` e `sketch.ino`.