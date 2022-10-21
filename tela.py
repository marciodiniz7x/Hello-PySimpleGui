import PySimpleGUI as sg

# Criação commpleta da tela
class TelaPython:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Nome', size=(5,0)),sg.Input(size=(15,0),key='Nome')],
            [sg.Text('Idade', size=(5,0)),sg.Input(size=(15,0),key='Idade')],
            [sg.Text('Quais provedores de email são aceitos?')],
            [sg.Checkbox('Gmail',key='Gmail'),sg.Checkbox('Outlook',key='Outlook'),sg.Checkbox('Yahoo',key='Yahoo')],
            [sg.Text('Aceita Cartão?')],
            [sg.Radio('Sim','cartoes',key='AceitaCartao'),sg.Radio('Não', 'cartoes', key='NaoAceita')],
            [sg.Button('Enviar Dados')]
        ]

        # Janela
        janela = sg.Window("Dados do usuário").layout(layout)

        # Extrair os dados da tela
        self.button, self.values = janela.Read()

    def Iniciar(self):
        nome = self.values['Nome']
        idade = self.values['Idade']
        aceita_gmail = self.values['Gmail']
        aceita_outlook = self.values['Outlook']
        aceita_yahoo = self.values['Yahoo']
        cartao_sim = self.values['AceitaCartao']
        cartao_nao = self.values['NaoAceita']

        print(f'Nome: {nome}')
        print(f'Idade: {idade}')
        print(f'Aceita Gmail: {aceita_gmail}')
        print(f'Aceita Outlook: {aceita_outlook}')
        print(f'Aceita Yahoo: {aceita_yahoo}')
        print(f'Aceita Cartão: {cartao_sim}')
        print(f'Não Aceita: {cartao_nao}')

tela = TelaPython()
tela.Iniciar()