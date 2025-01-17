# Tela inicial
# Titulo: PapiZap
# Botão: Iniciar Chat
    # quando clicar no botão:
    # abrir um popup(modal/alerta)
        # Titulo: Bem Vindo Aninha ao PapiZap
        # Caixa de Texto: Escreva seu nome no chat
        # Botão: Entrar no chat
            # Quando clicar no botão
                # fechar o popup
                # Sumir com o titulo
                # Sumir com o botão iniciar chat
                    # Carregar o Chat
                    # Carregar o campo de enviar mensagem: "Digite sua mensagem"
                    # Botão enviar
                        # Quando clicar no botão enviar
                            # Enviar a Mensagem
                            # Limpar a caixa de mensagem

# Flet
# Importar o flet
import flet as ft


# Criar uma função principal para rodar o seu aplicativo
    #titulo
def main(pagina):
    titulo = ft.Text("PapiZap")

    #conexao entre usuarios

    def enviar_mensagem_tunel(mensagem):
        #executar tudo o q eu quero que aconteça para todos os usuarios que receberam a msg
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    #Componentes da tela chat

    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = f"{nome_usuario}: {texto_campo_mensagem}"
        pagina.pubsub.send_all(mensagem)
        #Limpar a caixa de enviar mensagem
        campo_enviar_mensagem.value = ""
        pagina.update()

    campo_enviar_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])
    chat = ft.Column()
    #botao inicial
    def abrir_popup(evento):#Função para abrir o popup
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        print("Clicou no botao")
    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
    
    def entrar_chat(evento):#Função após o click no botão Iniciar Chat
        # fechar o popup
        popup.open = False
        # Sumir com o titulo
        pagina.remove(titulo)
        # Sumir com o botão iniciar chat
        pagina.remove(botao)
        # Carregar o chat 
        pagina.add(chat)
        
        # Carregar o campo enviar mensagem Carregar o botao enviar
        pagina.add(linha_enviar)

        #adicionar no chat a mensagem "Fulano entrou no chat"
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat"
        pagina.pubsub.send_all(mensagem)
        pagina.update()
    #criar o popup
    titulo_popup = ft.Text("Bem vindo ao PapiZap")
    caixa_nome = ft.TextField(label="Digite seu nome")
    botao_popup = ft.ElevatedButton("Entrar no chat",on_click=entrar_chat)
    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome,actions=[botao_popup])
    

    #colocar os elementos na tela
    pagina.add(titulo)
    pagina.add(botao)


# Executar essa função com flet
ft.app(main, view = ft.WEB_BROWSER)