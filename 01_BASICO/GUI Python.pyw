from tkinter import *
 
tela = Tk()
tela.title("TELA INICIAL")
tela["bg"] = "light yellow"
tela.geometry("200x200")
 
Container = Frame()
Container["pady"] = 10
Container["bg"] = "light yellow"
Container.pack()
 
texto = Text(Container)
texto["height"] = 1
texto["width"] = 15
texto.pack()
 
btOK = Button(Container)
btOK["text"] = "OK"
btOK["font"] = ("Calibri", "10","bold")
btOK["width"] = 12
btOK["bg"] = "blue"
btOK.pack()
 
btsair = Button()
btsair["text"] = "SAIR"
btsair["font"] = ("Calibri", "10","bold")
btsair["width"] = 5
btsair["command"] = quit
btsair.pack()
 
tela.mainloop()
