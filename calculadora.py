import tkinter as tk


#Funções
def evento_teclado(evento):#Lida com o evento da tecla ENTER
    if evento.char in "+-/*1234567890.":
        mostrar(evento.char)
    elif evento.keysym == "Return":
        resultado() #Executa a função que faz o cálculo



def mostrar(va):#Mostar a caracter no monitor
    try:
        monitor["text"] += str(va) #Soma ao monitor o caracter pretendido
    except: #Se o user tentar inserir um caracter depois de ter feito o cálculo mostra só o caracterdá
        monitor["text"] = va



def apagar2():
    try:
        texto_atual = monitor.cget("text")  # Obtém o texto atual corretamente
        if texto_atual: #Se tiver texto
            monitor["text"] = texto_atual[:-1] #o que fica no "text" é o que têm text_atual até ao índice -2,
            # ou seja não inclui o último (-1)
    except:
        monitor["text"] = ""



def apagar():
    monitor["text"] = "" #Apaga/transforma o texto da string(label) em nada




def resultado(): #Resultado
    try:
        calculo = monitor["text"]#Recebe o cálculo

        result = eval(calculo)#Calcula o resultado

        monitor["text"] = result#Mostra o resultado



    except: #De der erro a tela fica vazia
        monitor["text"] = ""


################################################################

#Janela - - - - -  - - - -  -

janela = tk.Tk()

janela.geometry("227x330")
janela.title("Calculadora")

#Configuração da jenale e colunas e linhas da janela
#Janela
janela.minsize(170, 250)
janela.maxsize(350,500)
#Colunas e linhas
janela.rowconfigure(0, weight = 1)
janela.rowconfigure(1, weight = 9)

janela.columnconfigure(0, weight = 1)

#Fontes - - - - - - -  - -  -
fonte_botoes = ("Ivy 9 bold")
fonte_operadores = ("Antenna 9 bold")


#Frames - - - - - -  - - -
frame_1 = tk.Frame(janela)
frame_2 = tk.Frame(janela)

#Configuração e colunas e linhas dos frames
#Frame 1
frame_1.rowconfigure(0, weight = 1)
frame_1.columnconfigure(0, weight = 1)

#Frame 2
frame_2.rowconfigure([0,1,2,3,4], weight = 1)
frame_2.columnconfigure([0,1,2,3], weight = 1)


frame_1.grid(row = 0, column =0, sticky = "nswe")
frame_2.grid(row = 1, column = 0, sticky = "nswe")


#Monitor - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
monitor = tk.Label(frame_1, text="", anchor= "e", relief = "flat",justify= "right",
                width = 18, height= 2, padx = 7,
                bg="#423f3f", fg="White",font = "Ivy 16")
monitor.grid(row = 0, column = 0, sticky = "nswe")
#monitor.place(x = 0,y = 3)



#Operadores - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#Divisão
divid = tk.Button(frame_2, text="/", width=7, height = 3, bg = "Orange",
               relief="raised", overrelief="ridge", font = fonte_operadores,
               command= lambda: mostrar("/"))


#Multiplicação
mult = tk.Button(frame_2, text = "*", width=7, height=3, bg = "Orange",
              relief="raised", overrelief="ridge",font = fonte_operadores,
              command = lambda: mostrar("*"))


#Subtração
subtrair = tk.Button(frame_2, text = "-", width=7,height=3, bg = "Orange",
                  relief="raised", overrelief="ridge", font = fonte_operadores,
                  command=lambda: mostrar("-"))

#Adição
somar = tk.Button(frame_2, text= "+", width=7,height=3,bg = "Orange",
               relief= "raised", overrelief="ridge", font = fonte_operadores,
               command= lambda: mostrar("+"))



divid.grid(row = 0, column = 3, sticky = "nswe")
mult.grid(row = 1,column = 3, sticky = "nswe")
subtrair.grid(row = 2, column = 3, sticky = "nswe")
somar.grid(row = 3, column = 3, sticky = "nswe")


#Botões - Apagar - - - - - - - - - - - - - - - - - - - - -
apagtud = tk.Button(frame_2, text="C",font = fonte_botoes,
                    width=7,height = 3,
                 relief= "raised", overrelief="ridge",
                 command= apagar) #tamanho original 14

apagar = tk.Button(frame_2, width = 7, height = 3,
                   text = "⌫",anchor="center", font = "Arial 9",
                   relief = "raised", overrelief="ridge",
                command = apagar2)


apagtud.grid(row = 0, column = 0, columnspan = 2, sticky = "snswe")
apagar.grid(row = 0, column = 2, sticky = "nswe")



#A função lambda cria uma função anónima sem nome, que executa a função mostrar() quando o botão seja clicado
#def funcao():
#    mostrar("/")

#Linha 1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
sete = tk.Button(frame_2, text= "7",width=7,height=3,  font = fonte_botoes,
              relief= "raised", overrelief="flat",
              command= lambda: mostrar("7"))

oito = tk.Button(frame_2, text="8",width=7,height=3,  font = fonte_botoes,
              relief= "raised", overrelief= "flat",
              command= lambda: mostrar("8"))

nove = tk.Button(frame_2, text = "9",width=7,height=3, font = fonte_botoes,
              relief= "raised",overrelief="flat",
              command = lambda: mostrar("9"))

sete.grid(row = 1, column = 0, sticky = "nswe")
oito.grid(row = 1, column = 1, sticky = "nswe")
nove.grid(row = 1, column = 2, sticky = "nswe")


#Linha2 -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
quatro = tk.Button(frame_2, text = "4",width=7,height=3, font = fonte_botoes,
                relief= "raised", overrelief="flat",
                command = lambda: mostrar("4"))


cinco = tk.Button(frame_2, text = "5", width=7,height=3, font = fonte_botoes,
               relief= "raised", overrelief="flat",
               command= lambda: mostrar("5"))


seis= tk.Button(frame_2, text = "6",width=7,height=3, font = fonte_botoes,
             relief= "raised", overrelief="flat",
             command= lambda: mostrar("6"))


quatro.grid(row = 2, column = 0, sticky = "nswe")
cinco.grid(row = 2, column = 1, sticky = "nswe")
seis.grid(row = 2,column = 2, sticky = "nswe")


#Linha3  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
um = tk.Button(frame_2, text = "1", width=7,height=3, font = fonte_botoes,
            relief= "raised", overrelief="flat",
            command= lambda: mostrar("1"))


dois = tk.Button(frame_2, text = "2", width=7,height=3, font = fonte_botoes,
              relief= "raised", overrelief="flat",
              command= lambda: mostrar("2"))


tres = tk.Button(frame_2, text="3", width=7,height=3, font = fonte_botoes,
              relief= "raised", overrelief="flat",
              command= lambda: mostrar("3"))


um.grid(row = 3, column = 0, sticky = "nswe")
dois.grid(row = 3, column = 1, sticky = "nswe")
tres.grid(row = 3, column = 2, sticky = "nswe")


#Linha4  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
zero = tk.Button(frame_2, text = "0", width=7, height = 3, font = fonte_botoes,
              relief= "raised", overrelief="flat",
              command= lambda: mostrar("0"))


ponto = tk.Button(frame_2, text = ".", width=7,height=3, font = fonte_botoes,
               relief="raised", overrelief="flat",
               command= lambda: mostrar("."))


igual = tk.Button(frame_2, text= "=", width=7,height=3,bg= "Orange", font = fonte_botoes,
               relief= "raised", overrelief="ridge",
               command=lambda : resultado())


zero.grid(row = 4, column = 0, columnspan = 2, sticky = "nswe")
ponto.grid(row = 4, column = 2, sticky = "nswe")
igual.grid(row = 4, column = 3, sticky = "nswe")


#Eventos de teclado
janela.bind("<Key>", evento_teclado) #Ao carregar no botão ENTER executa o cáluculo

#Loop
janela.mainloop()