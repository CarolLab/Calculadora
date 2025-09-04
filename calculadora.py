import tkinter as tk


#Funções
def evento_teclado(evento):#Lida com os eventos de teclado
    if evento.char.strip() not in ("\x08"):
        dici_eventos = {"+-/*1234567890.%()":lambda:mostrar(evento.char),
                        "Cc":lambda:monitor_stringvar.set(""),
                        "a": lambda: mostrar(ultimo_resultado),
                        "x": lambda:mostrar("**")
        }

        for key, funcao in dici_eventos.items():
            if evento.char in key: #Se for um caracter válido
                funcao() #Executa a função
                break


    else:
        if evento.keysym == "Return":
            resultado() #Executa a função que faz o cálculo
        elif evento.keysym == "BackSpace":
            apagar2()#Executa a função de apagar um por um



def mostrar(caracter):#Mostar a caracter no monitor
    global mostrar_resultado

    if mostrar_resultado:#Se o resultado estiver a ser exibido
        #Limpa a tela e adiciona o novo caracter
        #O monitor fica só com o caracter

        if caracter in "0123456789":
            monitor_stringvar.set(caracter)
            mostrar_resultado = False# O resultado já não está a ser exibido
        else:#"+-*/."
            novo_texto = monitor_stringvar.get() + caracter

            monitor_stringvar.set(novo_texto)

            mostrar_resultado = False  # O resultado já não está a ser exibido

    else:#Se o resultado não estiver a ser exibido
        #Age normalmente
        #Adiciona á expressão o novo caracter
        novo_texto = monitor_stringvar.get() + str(caracter)#Adiciona o caracter pretendido

        monitor_stringvar.set(novo_texto)#Insere o texto do monitar mais o caracter



def apagar2():#Apagar um por um

    if mostrar_resultado:#Se o resultado estiver a ser exibido
        monitor_stringvar.set("")#Apaga o texto

    else:#Se não estiver a ser exibido
        texto_atual = monitor_stringvar.get() # Obtém o texto atual corretamente

        if texto_atual: #Verificar se têm texto para poder apagar
            monitor_stringvar.set(texto_atual[:-1])#O que fica na StringVar é o que têm text_atual até ao índice -2,
            # ou seja não inclui o último caracter (-1)



def resultado(): #Mostra o resultado no monitor
    global mostrar_resultado
    global ultimo_resultado

    expressao = monitor_stringvar.get()#Recebe o cáculo
    resultado_ = calcular(expressao)#Chama a função de calcular

    monitor_stringvar.set(resultado_) #Exibe o resultado

    mostrar_resultado = True#O resultado está a ser exibido
    ultimo_resultado = resultado_ #Guarda o resultado

def calcular(expressao: str)->str:#Calcula a expressão dada
    try:
        return str(eval(expressao)) #Calcula e retorna o resultado em float
    except (SyntaxError, TypeError):
        return ""


################################################################
#Varíavéis
mostrar_resultado = False #Varíavel que informa se o resultado está a ser exibido
ultimo_resultado = 0 #Variável que é usada pelo botão ANS
#Incialmente é 0


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
fonte_botoes = "Ivy 9 bold"
fonte_operadores = "Antenna 9 bold"


#Frames - - - - - -  - - -
frame_1 = tk.Frame(janela)
frame_2 = tk.Frame(janela)

#Configuração e colunas e linhas dos frames
#Frame 1
frame_1.rowconfigure(0, weight = 1)
frame_1.columnconfigure(0, weight = 1)

#Frame 2
frame_2.rowconfigure([0,1,2,3,4,5], weight = 1)
frame_2.columnconfigure([0,1,2,3], weight = 1)


frame_1.grid(row = 0, column =0, sticky = "nswe")
frame_2.grid(row = 1, column = 0, sticky = "nswe")


#Monitor - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
monitor_stringvar = tk.StringVar()

monitor = tk.Label(frame_1, textvariable=monitor_stringvar, anchor= "e", relief = "flat",justify= "right",
                width = 18, height= 2, padx = 7,
                bg="#423f3f", fg="White",font = "Ivy 16")
monitor.grid(row = 0, column = 0, sticky = "nswe")



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



divid.grid(row = 1, column = 3, sticky = "nswe")
mult.grid(row = 2,column = 3, sticky = "nswe")
subtrair.grid(row = 3, column = 3, sticky = "nswe")
somar.grid(row = 4, column = 3, sticky = "nswe")


#Botões - Apagar - - - - - - - - - - - - - - - - - - - - -
apagar_tudo= tk.Button(frame_2, text="C",font = fonte_botoes,
                    width=7,height = 3,
                 relief= "raised", overrelief="ridge",
                 command= lambda: monitor_stringvar.set(""))

apagar = tk.Button(frame_2, width = 7, height = 3,
                   text = "⌫",anchor="center", font = "Arial 9",
                   relief = "raised", overrelief="ridge",
                command = apagar2)


apagar_tudo.grid(row = 0, column = 0, columnspan = 2, sticky = "snswe")
apagar.grid(row = 0, column = 2, sticky = "nswe")


#Linha 0 -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
resto_divisao = tk.Button(frame_2, text = "%", width = 7, height = 2,
                          relief="raised", overrelief="flat",
                          command = lambda: mostrar("%"))

resto_divisao.grid(row = 0, column = 3, sticky = "nswe")

#Linha 1 -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
abre_paren = tk.Button(frame_2,text = "(", width = 7, height = 3, font = fonte_botoes,
                       relief = "raised", overrelief= "flat",
                  command = lambda: mostrar("("))
fecha_paren = tk.Button(frame_2, text = ")", width = 7, height = 2,
                        relief = "raised", overrelief = "flat",
                  command = lambda: mostrar(")"))

elevado_ao_quadrado = tk.Button(frame_2, text = "x²", width = 7, height = 2,
                                relief = "raised", overrelief= "flat",
                                command = lambda: mostrar("**"))

abre_paren.grid(row = 1, column = 0, sticky = "nswe")
fecha_paren.grid(row = 1, column = 1, sticky = "nswe")
elevado_ao_quadrado.grid(row = 1, column = 2, sticky = "nswe")


#Linha 2 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
sete = tk.Button(frame_2, text= "7",width=7,height=3,  font = fonte_botoes,
              relief= "raised", overrelief="flat",
              command= lambda: mostrar("7"))

oito = tk.Button(frame_2, text="8",width=7,height=3,  font = fonte_botoes,
              relief= "raised", overrelief= "flat",
              command= lambda: mostrar("8"))

nove = tk.Button(frame_2, text = "9",width=7,height=3, font = fonte_botoes,
              relief= "raised",overrelief="flat",
              command = lambda: mostrar("9"))

sete.grid(row = 2, column = 0, sticky = "nswe")
oito.grid(row = 2, column = 1, sticky = "nswe")
nove.grid(row = 2, column = 2, sticky = "nswe")


#Linha 3 -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
quatro = tk.Button(frame_2, text = "4",width=7,height=3, font = fonte_botoes,
                relief= "raised", overrelief="flat",
                command = lambda: mostrar("4"))


cinco = tk.Button(frame_2, text = "5", width=7,height=3, font = fonte_botoes,
               relief= "raised", overrelief="flat",
               command= lambda: mostrar("5"))


seis= tk.Button(frame_2, text = "6",width=7,height=3, font = fonte_botoes,
             relief= "raised", overrelief="flat",
             command= lambda: mostrar("6"))


quatro.grid(row = 3, column = 0, sticky = "nswe")
cinco.grid(row = 3, column = 1, sticky = "nswe")
seis.grid(row = 3,column = 2, sticky = "nswe")


#Linha 4  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
um = tk.Button(frame_2, text = "1", width=7,height=3, font = fonte_botoes,
            relief= "raised", overrelief="flat",
            command= lambda: mostrar("1"))


dois = tk.Button(frame_2, text = "2", width=7,height=3, font = fonte_botoes,
              relief= "raised", overrelief="flat",
              command= lambda: mostrar("2"))


tres = tk.Button(frame_2, text="3", width=7,height=3, font = fonte_botoes,
              relief= "raised", overrelief="flat",
              command= lambda: mostrar("3"))


um.grid(row = 4, column = 0, sticky = "nswe")
dois.grid(row = 4, column = 1, sticky = "nswe")
tres.grid(row = 4, column = 2, sticky = "nswe")


#Linha4  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
zero = tk.Button(frame_2, text = "0", width=7, height = 3, font = fonte_botoes,
              relief= "raised", overrelief="flat",
              command= lambda: mostrar("0"))


ponto = tk.Button(frame_2, text = ".", width=7,height=3, font = fonte_botoes,
               relief="raised", overrelief="flat",
               command= lambda: mostrar("."))

botao_ans = tk.Button(frame_2, text = "ANS", width = 7, height = 3,
                      relief = "raised", overrelief = "flat",
                      command = lambda: mostrar(ultimo_resultado))


igual = tk.Button(frame_2, text= "=", width=7,height=3,bg= "Orange", font = fonte_botoes,
               relief= "raised", overrelief="ridge",
               command=lambda : resultado())


zero.grid(row = 5, column = 0, sticky = "nswe")
ponto.grid(row = 5, column = 1, sticky = "nswe")
botao_ans.grid(row = 5, column = 2, sticky = "nswe")
igual.grid(row = 5, column = 3, sticky = "nswe")


#Eventos de teclado
janela.bind("<KeyPress>", evento_teclado)#Ao carregar num tecla

#Loop
janela.mainloop()