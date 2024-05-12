import requests

# Substitua pela sua chave de API
apiKey = "qil5PskQL0ig4elyoQszsQ"

# Substitua pela URL correta da API
url = "https://sai-library.saiapplications.com"

# Solicita ao usuário que insira o código-fonte Java
codigo = input("Por favor, insira o código-fonte Java para análise: ")

# Define os cabeçalhos da requisição
headers = {"X-Api-Key": apiKey}

# Define os dados a serem enviados na requisição
data = {
    "inputs": {
        "codigo": codigo,
    }
}

# Faz a requisição POST para a API
response = requests.post(f"{url}/api/templates/6626987f2b1023d8c19486cd/execute", json=data, headers=headers)

# Verifica o código de status da resposta
if response.status_code == 200:
    # Imprime a resposta da API
    print("Resposta da API:")
    print(response.text)
else:
    # Imprime o código de status e a mensagem de erro
    print(f"Erro: {response.status_code} - {response.text}")
