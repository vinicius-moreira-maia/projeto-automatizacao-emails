import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
#from credenciais import obter_credenciais

#load_dotenv()

def obter_credenciais():
    return {
        "login": os.getenv("EMAIL_LOGIN"),
        "senha": os.getenv("EMAIL_PASSWORD")
    }

aniversarios = {"Joy": "09/08", 'Raul': '10/08', 'Zézé': '12/08'}
credenciais = obter_credenciais()

def enviar_email(assunto, corpo, para_email):
    de_email = credenciais["login"]
    de_senha = credenciais["senha"]

    # essa classe permite fornecer várias partes do email separadas
    msg = MIMEMultipart()
    msg['From'] = de_email
    msg['To'] = para_email
    msg['Subject'] = assunto

    # aqui o corpo do texto (parte) está sendo atribuído à instância (todo) - 'plain' é texto sem formatação
    msg.attach(MIMEText(corpo, 'plain'))

    # enviando o email - loop para tentar enviar de novo em caso de falhas
    for _ in range(10):
        try:
            servidor = smtplib.SMTP('smtp.gmail.com', 587) # conectando no servidor SMTP do gmail
            servidor.starttls() # estabelecendo comunicação tls, por segurança
            servidor.login(de_email, de_senha) # conectando no servidor com senha de aplicação
            servidor.send_message(msg) # enviando mensagem
            servidor.quit() # fechando a conexão
            print(f"Email enviado para {para_email}")
            break
        except Exception as e:
            print(f"Erro ao enviar email: {e}")

# vendo se hoje é niver de alguém
hoje = datetime.now().strftime('%d/%m')
for nome, data in aniversarios.items():
    if data == hoje:
        assunto = f"Feliz Aniversário, {nome}!"
        corpo = f"Oi {nome},\n\nFeliz aniversário! Esperamos que você tenha um ótimo dia!\n\nAbraços!"
        enviar_email(assunto, corpo, "viniciusconcept@gmail.com")