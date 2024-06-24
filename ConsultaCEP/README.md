# Consulta de CEP

Este projeto é uma aplicação de interface gráfica simples para consulta de CEPs utilizando a biblioteca `customtkinter` e a API do `viacep.com.br`.

## Funcionalidades

- Entrada de CEP para consulta.
- Exibição das informações do endereço correspondente ao CEP inserido.
- Mensagem de erro para CEPs inválidos.
- Botão para limpar os campos e resultados.

## Requisitos

- Python 3.6 ou superior
- Bibliotecas Python:
  - `customtkinter`
  - `requests`

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seuusuario/consulta-cep.git
    cd consulta-cep
    ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. Instale as dependências:
    ```sh
    pip install customtkinter requests
    ```

## Uso

Para iniciar a aplicação, execute o script `main.py`:
```sh
python main.py
