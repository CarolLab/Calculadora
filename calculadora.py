import tkinter as tk

#Janela


def mostrar(va):
    try:
        monitor["text"] += str(va) #Soma ao monitor o simbolo pretendido
    except: #dá erro de não poder juntar int + str então apaga e mostra o número escolhido
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




def resultado(tela): #Resultado
    try:
        conta = tela["text"]

        result = eval(conta)

        tela["text"] = result



    except: #De der erro a tela fica vazia
        tela["text"] = ""


################################################################

#Janela

janela = tk.Tk()

janela.geometry("234x330")
janela.title("Calculadora")



#Fontes
fonte_botoes = ("Ivy 9 bold")



#Monitor
monitor = tk.Label(janela, text="", anchor= "e", relief = "flat",justify= "right",
                width = 18, height= 2, padx = 7,
                bg="#423f3f", fg="White",font = "Ivy 16")
monitor.place(x = 0,y = 3)



#Operadores
#Divisão
divid = tk.Button(janela, text="/", width=7, height = 3, bg = "Orange",
               relief="raised", overrelief="ridge",
               command= lambda: mostrar("/"))


#Multiplicação
mult = tk.Button(janela, text = "*", width=7, height=3, bg = "Orange",
              relief="raised", overrelief="ridge",
              command = lambda: mostrar("*"))


#Subtração
subtrair = tk.Button(janela, text = "-", width=7,height=3, bg = "Orange",
                  relief="raised", overrelief="ridge",
                  command=lambda: mostrar("-"))

#Adição
somar = tk.Button(janela, text= "+", width=7,height=3,bg = "Orange",
               relief= "raised", overrelief="ridge",
               command= lambda: mostrar("+"))



divid.place(x = 175, y = 58)
mult.place(x = 175, y = 113)
subtrair.place(x = 175, y = 168)
somar.place(x = 175, y = 223)



#Apagar
apagtud = tk.Button(janela, text="C", padx=2,  font = fonte_botoes,
                    width=15, height = 3,
                 relief= "raised", overrelief="ridge",
                 command= apagar) #tamanho original 14

apagar = tk.Button(janela, width = 7, height = 3, text = "⌫",anchor="center", font = "Arial 9",
                command = apagar2)


apagtud.place(x = 0, y = 58)
apagar.place(x = 116, y = 58)



#A função lambda cria uma função anónima sem nome, que executa a função mostrar() quando o botão seja clicado
#def funcao():
#    mostrar("/")

#Linha 1
sete = tk.Button(janela, text= "7",width=7,height=3,  font = fonte_botoes,
              relief= "raised", overrelief="flat",
              command= lambda: mostrar("7"))

oito = tk.Button(janela, text="8",width=7,height=3,  font = fonte_botoes,
              relief= "raised", overrelief= "flat",
              command= lambda: mostrar("8"))

nove = tk.Button(janela, text = "9",width=7,height=3, font = fonte_botoes,
              relief= "raised",overrelief="flat",
              command = lambda: mostrar("9"))

sete.place(x = 0, y= 113)
oito.place(x = 58, y = 113)
nove.place(x = 116, y = 113)


#Linha2
quatro = tk.Button(janela, text = "4",width=7,height=3, font = fonte_botoes,
                relief= "raised", overrelief="flat",
                command = lambda: mostrar("4"))


cinco = tk.Button(janela, text = "5", width=7,height=3, font = fonte_botoes,
               relief= "raised", overrelief="flat",
               command= lambda: mostrar("5"))


seis= tk.Button(janela, text = "6",width=7,height=3, font = fonte_botoes,
             relief= "raised", overrelief="flat",
             command= lambda: mostrar("6"))


quatro.place(x = 0, y = 168)
cinco.place(x = 58, y = 168)
seis.place(x = 116, y = 168)


#Linha3
um = tk.Button(janela, text = "1", width=7,height=3, font = fonte_botoes,
            relief= "raised", overrelief="flat",
            command= lambda: mostrar("1"))


dois = tk.Button(janela, text = "2", width=7,height=3, font = fonte_botoes,
              relief= "raised", overrelief="flat",
              command= lambda: mostrar("2"))


tres = tk.Button(janela, text="3", width=7,height=3, font = fonte_botoes,
              relief= "raised", overrelief="flat",
              command= lambda: mostrar("3"))


um.place(x=0, y =223)
dois.place(x = 58, y = 223)
tres.place(x = 116, y = 223)


#Linha4
zero = tk.Button(janela, text = "0", width=15, height = 3,padx=2, font = fonte_botoes,
              relief= "raised", overrelief="flat",
              command= lambda: mostrar("0"))


ponto = tk.Button(janela, text = ".", width=7,height=3, font = fonte_botoes,
               relief="raised", overrelief="flat",
               command= lambda: mostrar("."))


igual = tk.Button(janela, text= "=", width=7,height=3,bg= "Orange", font = fonte_botoes,
               relief= "raised", overrelief="ridge",
               command=lambda : resultado(monitor))


zero.place(x = 0, y = 278)
ponto.place(x = 116, y = 278)
igual.place(x = 175, y = 278)


#Loop
janela.mainloop()