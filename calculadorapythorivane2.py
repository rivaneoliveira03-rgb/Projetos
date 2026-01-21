# importando tkinter
from tkinter import *


# cores

cor1 ="#171715"  # preto
cor2 ="#a5fc03"  # green/verde
cor3 ="#033dfc"  # blue/azul
cor4 ="#6f03fc"  # purple/roxo
cor5 ="#FC6E0F"  # laranja
cor6 ="#BAAFAF"  # cinza
cor7 ="#7C7878"  # cinza escuro 

janela  =Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)

# criando frames
frame_tela = Frame(janela, width=235, height=50, bg=cor7)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# criando botoes 

b_1 = Button(frame_corpo, text="C", width=11, height=2, bg=cor6)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, text="%", width=5, height=2, bg=cor6)
b_2.place(x=88, y=0)
b_3 = Button(frame_corpo, text="/", width=5, height=2, bg=cor5, fg=cor2)
b_3.place(x=177, y=0)


janela.mainloop()

