
#interface grafica

from tkinter import * #Tk biblioteca para desenhos graficos
#from tkinter import Tk, Laber, CENTER,Entry, messagebox

from tkinter import messagebox

janela = Tk()
janela.geometry("400x400")

rotulo = Label(janela, text="olá <3", font = ("Comic Sans", 14)) # 'janela' dentro do () indica que rotulo pertence a janela
rotulo.place(x=200,y=100, anchor=CENTER) #posicao do rotulo na janela

# .place define posicao do item antes do "." na janela


caixa_texto = Entry(janela, width=15,font = ("Comic Sans", 14)) 
caixa_texto.place(x=100,y=200) 


caixa_texto2 = Entry(janela, width=15,font = ("Comic Sans", 14))
caixa_texto2.place(x=100,y=300)

def copiar():
    texto = caixa_texto.get() #.get retorna conteudo dentro da caixa e coloca dentro da variavel texto
    caixa_texto2.insert(0,texto) #get insere um conteudo  (0 mostra que é para colocar no inicio)

def mensagem():
    messagebox.showinfo("Aviso","Vamos programar")
    
botao = Button(janela,text="clique aqui", command=copiar)
botao.place(x=150,y=250)

botao2 = Button(janela,text="aviso", command=mensagem)
botao2.place(x=150,y=350)

janela.mainloop() #fica atualizando a janela 

#ancora objeto (usando coordenadas (norte, sul, leste, oeste, centro)) referente ao texto ex centro do objeto "ola"