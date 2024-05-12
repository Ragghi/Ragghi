import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import requests
import markdown2
from tkinterhtml import HtmlFrame

# Função para enviar a solicitação à API e exibir a resposta em Markdown
def enviar_para_api():
    # Inicia a função em uma thread separada para não bloquear a interface
    threading.Thread(target=fazer_requisicao_api).start()

# Função que faz a requisição à API em uma thread separada
def fazer_requisicao_api():
    # Mostra o rótulo de carregamento
    loading_label.config(text="Carregando...")
    
    # Obtém o código-fonte Java da entrada
    codigo = codigo_texto.get("1.0", tk.END).strip()
    
    # Verifica se o código foi fornecido
    if not codigo:
        messagebox.showerror("Erro", "Por favor, insira o código-fonte Java.")
        # Esconde o rótulo de carregamento
        loading_label.config(text="")
        return
    
    # Define a URL, chave de API e cabeçalhos
    url = "https://sai-library.saiapplications.com"
    api_key = "qil5PskQL0ig4elyoQszsQ"  # Substitua pela sua chave de API
    headers = {"X-Api-Key": api_key}
    
    # Define os dados a serem enviados na requisição
    data = {
        "inputs": {
            "codigo": codigo,
        }
    }
    
    # Faz a requisição POST para a API
    response = requests.post(f"{url}/api/templates/6626987f2b1023d8c19486cd/execute", json=data, headers=headers)
    
    # Verifica a resposta da API
    if response.status_code == 200:
        # Converte a resposta em formato Markdown para HTML
        resposta_markdown = response.text
        resposta_html = markdown2.markdown(resposta_markdown)
        
        # Exibe a resposta HTML na área de texto rolante
        resposta_html_frame.set_content(resposta_html)
    else:
        # Exibe uma mensagem de erro
        messagebox.showerror("Erro", f"Erro: {response.status_code} - {response.text}")
    
    # Esconde o rótulo de carregamento
    loading_label.config(text="")

# Cria a janela principal
janela = tk.Tk()
janela.title("Análise Reversa Java")

# Cria um rótulo para a entrada de código-fonte Java
tk.Label(janela, text="Código-fonte Java:").pack(pady=5)

# Cria um widget de texto para a entrada de código-fonte Java
codigo_texto = tk.scrolledtext.ScrolledText(janela, width=60, height=10)
codigo_texto.pack(pady=5)

# Cria um rótulo para o indicador de carregamento
loading_label = tk.Label(janela, text="")
loading_label.pack()

# Cria um botão para enviar a solicitação à API
botao_enviar = ttk.Button(janela, text="Enviar", command=enviar_para_api)
botao_enviar.pack(pady=10)

# Cria um rótulo para a resposta da API
tk.Label(janela, text="Resposta da API:").pack(pady=5)

# Cria um frame HTML para exibir a resposta em HTML
resposta_html_frame = HtmlFrame(janela, width=60, height=15)
resposta_html_frame.pack(pady=5)

# Executa o loop principal da interface gráfica
janela.mainloop()
