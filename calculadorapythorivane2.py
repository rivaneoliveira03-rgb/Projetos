# importando tkinter
from tkinter import *


# cores

cor1 ="#171715"  # preto
cor2 ="#a5fc03"  # green/verde
cor3 ="#033dfc"  # blue/azul
cor4 ="#6f03fc"  # purple/roxo
cor5 ="#fc0328"  # red/vermelho



janela  =Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)

# criando frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# criando botoes 

b_1 = Button(frame_corpo, text="C", width=11, height=2)
b_1.place(x=0, y=0)

janela.mainloop()