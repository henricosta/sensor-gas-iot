# Projeto Cloud/IoT

Este projeto contém uma API em Python e utiliza o **localtunnel** para expor o servidor localmente. 

## Pré-requisitos

- [Python 3.8 ou superior](https://www.python.org/downloads/)
- [Node.js](https://nodejs.org/)
- [Visual Studio Code](https://code.visualstudio.com/) (ou outro editor de código)

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

### 3. Configurar banco de dados

1. Executar script para criar banco de dados:
   ```bash
   python api/create_database.py
   ```

2. (Opcional) Inserir dados de teste.
   ```bash
   python api/inserir_mock_data.py
   ```

### 3. Iniciar a API

Após a instalação das dependências, inicie a API executando o arquivo `app.py`, que está localizado em `api/`:
   ```bash
   python api/app.py
   ```

Após iniciar a API, você pode acessar a interface web no seu navegador através do endereço [http://localhost:8080](http://localhost:8080).

# Testando a API usando a ESP32
### 1. Instalar o Localtunnel

Após configurar o ambiente. **Em outro terminal**, instale o Localtunnel localmente usando npm:
```bash
npm install localtunnel
```

### 2. Configurar o Tunnel com Localtunnel

Em uma nova janela do terminal, execute o Localtunnel para expor a API:

```bash
npx localtunnel --port 8080
```

Depois disso acesse a url do projeto que é fornecido no terminal no navegador. Ou substituia a url no arquivo `sketch.ino` para testar ela pelo ESP32.

### 3. Executando o códiguo utilizando a plataforma [Wokwi](https://wokwi.com/)

Substituia o código padrão pelo localizado no diretório `esp32/sketch.ino` e substitua o conteúdo do `diagram.json` pelos contidos no diretório `esp32/diagram.json`.

A url dentro de `sketch.ino` deve ser substituída pela fornecida pelo localtunnel.

---
Slides do Projeto
https://www.canva.com/design/DAGW62dvBjg/e0mM13dBjsf_yhbYCe_jqA/edit?utm_content=DAGW62dvBjg&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
