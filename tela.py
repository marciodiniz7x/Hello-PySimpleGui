import PySimpleGUI as sg

# Criação commpleta da tela
class TelaPython:
    def __init__(self):

        sg.change_look_and_feel('Reddit')
        # Layout
        layout = [
            [sg.Text('Nome', size=(5,0)),sg.Input(size=(15,0),key='Nome')],
            [sg.Text('Idade', size=(5,0)),sg.Input(size=(15,0),key='Idade')],
            [sg.Text('Quais provedores de email são aceitos?')],
            [sg.Checkbox('Gmail',key='Gmail'),sg.Checkbox('Outlook',key='Outlook'),sg.Checkbox('Yahoo',key='Yahoo')],
            [sg.Text('Aceita Cartão?')],
            [sg.Radio('Sim','cartoes',key='AceitaCartao'),sg.Radio('Não', 'cartoes', key='NaoAceita')],
            [sg.Slider(range=(0,100),default_value=0, orientation='h', size=(15,20), key='SliderVelocidade')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30,20))]
        ]

        # Janela
        self.janela = sg.Window("Dados do usuário").layout(layout)


        

    def Iniciar(self):
        while True:
            # Extrair os dados da tela continuamente
            self.button, self.values = self.janela.Read()
            nome = self.values['Nome']
            idade = self.values['Idade']
            aceita_gmail = self.values['Gmail']
            aceita_outlook = self.values['Outlook']
            aceita_yahoo = self.values['Yahoo']
            cartao_sim = self.values['AceitaCartao']
            cartao_nao = self.values['NaoAceita']
            velocidade_script = self.values['SliderVelocidade']

            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Aceita Gmail: {aceita_gmail}')
            print(f'Aceita Outlook: {aceita_outlook}')
            print(f'Aceita Yahoo: {aceita_yahoo}')
            print(f'Aceita Cartão: {cartao_sim}')
            print(f'Não Aceita: {cartao_nao}')
            print(f'Velocidade Scripts: {velocidade_script}')

tela = TelaPython()
tela.Iniciar()