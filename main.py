import flet as ft 

def main(page: ft.Page):

    page.title = "Tela Inicial"
    page.window_width = 600
    page.window_height = 600
    page.window_resizable  = False
    page.padding = 100
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def BotaoClick(e):
        if all([nome_input.value, senha_input.value]):
            dlg = ft.AlertDialog(
                title=ft.Text('Saudações ' + nome_input.value + '🖖')
            )
            page.dialog = dlg
            dlg.open = True
            page.update()

    page.appbar = ft.AppBar(title=ft.Text('Seja Bem Vindo Pequeno Gafanhoto!'), center_title=True)
    nome_input = ft.TextField(
        label='Nome:', autofocus=True, hint_text='Digite seu nome...'
    )
    senha_input = ft.TextField(
        label='Senha:', password=True, can_reveal_password=True
    )
    botao_final = ft.ElevatedButton(
        text='Faça Login', width=600, on_click=BotaoClick
    )
    page.update()
    page.add(nome_input, senha_input, botao_final)

ft.app(target=main)