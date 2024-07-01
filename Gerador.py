from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from spacy.cli import download

download("en_core_web_sm")

class ENGSM:
    ISO_639_1 = 'en_core_web_sm'
    
    chatbot = ChatBot("BotKas")

conversa = [
    "Como reiniciar meu computador?", 
     "Desligue o computador e ligue-o novamente.", 
     "Pressione o botão de energia por alguns segundos até o computador desligar.",
    "Meu computador está lento", 
     "Tente fechar programas que você não está usando.", 
     "Execute uma verificação de vírus.", 
     "Limpe o cache do seu navegador.", 
     "Verifique se há espaço livre no disco rígido.",
    "O que fazer se meu wifi não estiver funcionando?", 
     "Verifique se o roteador está ligado e se você está dentro do alcance da rede.",
     "Reinicie o roteador e o seu dispositivo.",
     "Verifique se o nome da rede está correto e se você inseriu a senha correta.",
    "Minha impressora não está imprimindo", 
     "Verifique se a impressora está ligada e se há papel.", 
     "Verifique a conexão USB ou wireless.", 
     "Tente reiniciar a impressora e o computador.", 
     "Verifique se os drivers da impressora estão atualizados.",
    "Como criar uma nova conta de usuário?", 
     "Acesse as configurações do sistema e procure por 'Criar uma nova conta'.",
     "Siga as instruções na tela para criar a conta.",
    "Esqueci minha senha", 
     "Tente recuperar sua senha usando a opção de recuperação de senha.", 
     "Se você não conseguir recuperar sua senha, entre em contato com o administrador do sistema.",
    "Meu mouse não está funcionando", 
     "Verifique se o mouse está conectado corretamente ao computador.", 
     "Tente usar outro mouse.", 
     "Verifique se o mouse possui baterias ou se está ligado.", 
     "Verifique se o mouse está funcionando em outro computador.",
    "Meu teclado não está funcionando", 
     "Verifique se o teclado está conectado corretamente ao computador.", 
     "Tente usar outro teclado.", 
     "Verifique se o teclado possui baterias ou se está ligado.", 
     "Verifique se o teclado está funcionando em outro computador.",
    "O que é um firewall?", 
     "Um firewall é um sistema de segurança que protege seu computador de acesso não autorizado.", 
     "Ele bloqueia conexões de entrada e saída não autorizadas.", 
     "É importante manter o firewall do seu computador ativado.",
    "O que é um vírus?", 
     "Um vírus é um programa malicioso que pode danificar seu computador.", 
     "Vírus podem ser transmitidos por email, downloads ou sites infectados.", 
     "É importante instalar um antivírus para proteger seu computador de vírus.",
    "Como faço backup dos meus arquivos?", 
     "Você pode fazer backup dos seus arquivos em um disco rígido externo, um serviço de armazenamento em nuvem ou em outro computador.", 
     "É importante fazer backup regularmente para evitar a perda de dados."
]

trainer = ListTrainer(chatbot)
trainer.train(conversa)

while True:
    try:
        mensagem = input("Mande uma mensagem para o gerador: ")

        if mensagem.lower() == "parar":
            break

        resposta = chatbot.get_response(mensagem)

        if resposta.confidence > 0.5:
            print('Kas Bot: ', resposta.text)
        else:
            print('Kas Bot: Ainda não sei responder esta pergunta')
            
    except Exception as e:
        print(f"Erro: {e}")
        
    finally:
    # Liberar recursos (por exemplo, fechar conexão com a API)
        pass