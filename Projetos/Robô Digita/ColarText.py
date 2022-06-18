import time
from os import path
import pyautogui
from PySimpleGUI import PySimpleGUI as sg
from pynput.keyboard import Controller

keyboard = Controller()

# Escolhendo a cor do App
sg.theme('Dark Grey 13')
# interface
layout1 = [
    [sg.Text('Paste your text:', justification='center', size=(25, 0), font=300), sg.Text("Tempo /s"),
     sg.Combo([3, 2, 1], key="Tempo")],
    [sg.Multiline(size=(50, 18), key='copia')],
    [sg.Button('Paste', size=(22, 0)), sg.Button('Exit', size=(25, 0))],
    [sg.Text("copyright © 2022 Tarcio Diniz", justification='center', size=(50, 0))],

]
janela1 = sg.Window('Code Paste Robot', layout1, finalize=True, size=(400, 400), icon="icon.ico")
# Definindo os eventos e valores a ser puxado com pysimplegui
while True:
    eventos, valores = janela1.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Paste':
        Seu_codigo = valores['copia']
        arquivo = open(path.expanduser("~/AppData/Local/Temp/arquivo.txt"), "w", newline="", encoding="utf-8")
        for p in Seu_codigo:
            arquivo.write(p)
        arquivo.close()
        # Descobrindo o total de linhas
        with open(path.expanduser("~/AppData/Local/Temp/arquivo.txt"), encoding="utf8") as meu_arquivo:
            total_linhas = int(sum(1 for line in meu_arquivo))
        # Copiando e colanado as informaçoes em outra aba
        pyautogui.hotkey('alt', 'tab')
        file = open(path.expanduser("~/AppData/Local/Temp/arquivo.txt"), encoding="utf-8")
        linha_especifica = list(range(total_linhas))
        for contagem, linha_num in enumerate(file):
            if contagem in linha_especifica:
                repetir = valores["Tempo"] * 10
                for x in range(repetir):
                    pyautogui.hotkey("shift", "tab")
                keyboard.type(f"{linha_num}")
                time.sleep(0.1)
        arquivo.close()
    if eventos == 'Exit':
        janela1.close()
        
