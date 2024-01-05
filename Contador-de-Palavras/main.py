import PySimpleGUI as sg

def count_words(text):
    text = text.strip()
    if not text:
        return 0
    words = text.split()
    return len(words)

layout = [
    [sg.Text('Insira o texto para contar as palavras')],
    [sg.Multiline(size=(50,5), key='-TEXT-')],
    [sg.Button('Contar palavras'), sg.Exit()]
]

window = sg.Window('Word Counter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    elif event == 'Contar palavras':
        text_input = values['-TEXT-']
        word_count = count_words(text_input)
        sg.popup(f'O número de palavras nesse texto é: {word_count}')

window.close()