from tkinter import *
import os
c = os.path.dirname(__file__)
nArquivo = c+'\\Lista.txt'
def gravar():
    arquivo = open(nArquivo,'a')
    arquivo.write("\nNome...:%s" % Vnome.get())
    arquivo.write("\nTelefone...:%s" % Vfone.get())
    arquivo.write("\nE-mail...:%s" % Vmail.get())
    arquivo.write("\nObservação...:%s" % Vobs.get('1.0', END))
    arquivo.write('\n\n')
    arquivo.close()

app = Tk()
app.title('Salva Dados')
app.geometry('300x600')
app.configure(background = '#F28500', border = 5)

#label Central ...

lbc = Label(text = 'Scriptando\nMeneleu', background = '#F28500', foreground = "#FFFFFF", font = 'ballerina-script 80 italic bold', anchor = W)
lbc.place(x = 320, y = 150, width = 800, height = 320)

# Label e Entry do nome ...
lb = Label(text = 'Nome de Usuário', background = '#F28500', foreground = "#FFFFFF", anchor = W)
lb.place(x = 10, y = 20, width = 130, height = 20)
Vnome = Entry(app, border = 5)
Vnome.place(x = 10, y = 40, width = 130, height = 20)

# Label e Entry do Telefone ...
lbb = Label(text = 'Telefone', background = '#F28500', foreground = "#FFFFFF", anchor = W)
lbb.place(x = 10, y = 80, width = 130, height = 20)
Vfone = Entry(app, border = 5)
Vfone.place(x = 10, y = 100, width = 130, height = 20)

# Label e Entry do E-mail ...
lbbb = Label(text = 'E-mail', background = '#F28500', foreground = "#FFFFFF", anchor = W)
lbbb.place(x = 10, y = 140, width = 130, height = 20)
Vmail = Entry(app, border = 5)
Vmail.place(x = 10, y = 160, width = 130, height = 20)

# Label e Entry do nome ... do tipo TEXT ...
lb = Label(text = 'Observação', background = '#F28500', foreground = "#FFFFFF", anchor = W)
lb.place(x = 10, y = 200, width = 80, height = 20)
Vobs = Text(app, border = 5)
Vobs.place(x = 10, y = 220, width = 140, height = 60)

#Inserção do Button ...
bt = Button(app, text = 'Login', command = gravar, anchor = W)
bt.place(x = 10, y = 300, width = 50, height = 20)


app.mainloop()
