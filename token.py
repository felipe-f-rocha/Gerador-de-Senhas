import secrets  # Modúlo para geração de senhas e "tokens"
import string  # Modúlo para agrupamento dos caracteres
import pyperclip
import customtkinter
from CTkMessagebox import CTkMessagebox


def gerar_senha(size):
    character = string.ascii_letters + string.digits + string.punctuation  # "Váriavel" com todos os "possiveis caract"
    password = "".join(secrets.choice(character) for i in range(size))
    return password  # Escolha aleatória dos caracteres fornecidos


def gerar_token():
    character = string.digits  # Gera os "digitos númericos" que irão compor a senha inicial
    password = "".join(secrets.choice(character) for i in range(3))  # Escolhe 3 "digitos" aleatoriamente
    token = secrets.token_hex(int(password))  # Converte a senha em um "token"
    return token


def copiar_texto(texto):
    pyperclip.copy(texto)
    msg = CTkMessagebox(
        title="Copiado",
        message="O valor foi copiado para a área de transferência!",
        icon="check"
    )
    msg.get()  # exibe e espera o usuário fechar


app = customtkinter.CTk()
app.withdraw()

msg = CTkMessagebox(
    title="Gerador de Senhas",
    message="Você deseja gerar uma senha ou um Token?",
    icon="question",
    option_1="Senha",
    option_2="Token"

)

resposta = msg.get()  # Retorna o texto do botão clicado

if resposta == "Senha":
    dialog = customtkinter.CTkInputDialog(text="Digite o tamanho da sua senha:")
    size = int(dialog.get_input())
    senha = gerar_senha(size)
    copiar_texto(senha)
elif resposta == "Token":
    token = gerar_token()
    copiar_texto(token)

app.destroy()