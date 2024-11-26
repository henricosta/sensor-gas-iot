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

### 3. Execute o código na placa

Todos os componentes necessários estão no arquivo `esp32/diagram.json`

#### Opção 1 - Testando na placa

1. Compile o código `sketch.ino` usando a IDE do Arduino ou a plataforma de sua escolha.
2. Substitua a URL da API no código `sketch.ino` pela URL fornecida pelo Localtunnel.
3. Carregue o código na placa ESP32.
4. Abra o monitor serial para verificar a saída e garantir que a ESP32 está se comunicando corretamente com a API.

#### Opção 2 - Testando no Wokwi
Os arquivos estão na pasta `esp32/`. O projeto também pode ser testado no Wokwi usando o `diagram.json`.

---
Slides do Projeto
https://www.canva.com/design/DAGW62dvBjg/e0mM13dBjsf_yhbYCe_jqA/edit?utm_content=DAGW62dvBjg&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
