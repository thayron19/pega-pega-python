import tkinter
import random
import keyboard
# ---------------------------------------------------------------------------------------------------------------------
janela = tkinter.Tk()

janela.title('Pega pega')

largura_janela = 300
altura_janela = 190

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

posicaol = float(largura_janela/2 - largura_tela/2)
posicaoa = float(altura_janela/2 - altura_tela/2)

janela.geometry("%dx%d%d%d" % (largura_janela, altura_janela, posicaol, posicaoa))
janela.resizable(width=False, height=False)


# ---------------------------------------------------------------------------------------------------------------------
def adivinha(direcao):
    global acumulador

    x = personagem.winfo_x()
    y = personagem.winfo_y()

    if direcao == 8:
        if y >= 50:
            y -= 3
    elif direcao == 4:
        if x >= 10:
            x -= 3
    elif direcao == 6:
        if x <= 260:
            x += 3
    elif direcao == 2:
        if y <= 150:
            y += 3

    personagem.place(x=x, y=y)

    print(x, y)
# ---------------------------------------------------------------------------------------------------------------------
    x_ini = inimigo.winfo_x()
    y_ini = inimigo.winfo_y()

    direcao_inimigo = random.randint(1, 8)

    if direcao_inimigo == 1 or direcao_inimigo == 5:
        if y_ini >= 45:
            y_ini -= 9
    elif direcao_inimigo == 2 or direcao_inimigo == 6:
        if x_ini >= 10:
            x_ini -= 9
    elif direcao_inimigo == 3 or direcao_inimigo == 7:
        if x_ini <= 265:
            x_ini += 9
    elif direcao_inimigo == 4 or direcao_inimigo == 8:
        if y_ini <= 150:
            y_ini += 9

    inimigo.place(x=x_ini, y=y_ini)

    if x == x_ini and y == y_ini:
        acumulador += 1
        if acumulador == 1:
            jogo_var.set(f'Pega pega: {acumulador} ponto')
        else:
            jogo_var.set(f'Pega pega: {acumulador} pontos')


# ---------------------------------------------------------------------------------------------------------------------
acumulador = 0
jogo_var = tkinter.StringVar()
jogo_var.set(f'Pega pega')
jogo_texto = tkinter.Label(janela, textvariable=jogo_var, font=('', 12))
jogo_texto.place(x=10, y=10)
# ---------------------------------------------------------------------------------------------------------------------
inimigo = tkinter.Button(janela, text=' ', command=lambda: adivinha(1), bg='red')
inimigo.place(x=100, y=100, width=30)
# ---------------------------------------------------------------------------------------------------------------------
personagem = tkinter.Button(janela, text=' ', command=lambda: adivinha(1), bg='green')
personagem.place(x=100, y=100, width=30)
# ---------------------------------------------------------------------------------------------------------------------
keyboard.on_press_key('8', lambda _: adivinha(8))
keyboard.on_press_key('4', lambda _: adivinha(4))
keyboard.on_press_key('6', lambda _: adivinha(6))
keyboard.on_press_key('2', lambda _: adivinha(2))

keyboard.on_press_key('ESC', lambda _: janela.destroy())
# ---------------------------------------------------------------------------------------------------------------------
janela.mainloop()
