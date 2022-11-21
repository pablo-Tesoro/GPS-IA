from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import csv
def origenDestino (estacion):

    if(seleccion.get() == 0) :
        origen.set(estacion)
        seleccion.set(1)
    else:
        destino.set(estacion) 
        seleccion.set(0)

def newWindow():
    # Toplevel object which will
    #be treated as a new window
    
    texto = StringVar()
    if(origen.get() == "---Seleccionar Origen---" or destino.get()== "---Seleccionar Destino---"):
        messagebox.showerror(title="Error", message="No se puede calcular la ruta si alguno de los camapos origen o destino esta vacio.")
    else:
        newWindow = Toplevel(root)
        texto.set("Se puede")
        frameRuta = Frame(newWindow, width=700, height=750, background='white')
        frameRuta.pack_propagate(0)    
        frameRuta.pack()
        img2 = ImageTk.PhotoImage(Image.open('Leguina.jpg'))
        label2= Label(frameRuta,image=img2)
        label2.image = img2
        label2.pack()
        Label(label2,
          textvariable= texto, font=("Dolce Vita",30)).place(x=375,y=350)
    destino.set("---Seleccionar Destino---") 
    origen.set("---Seleccionar Origen---") 
    seleccion.set(0)
    

def make_label(parent, img):
    label = Label(parent, image=img)
    label.pack()

    #Generamos y configuramos la ventana

root= Tk()
root.config(bg='white')
root.geometry("1000x790")
root.title("Metro Atenas")
root.resizable(False,False)
root.iconbitmap("icono.ico")
#Generamos y configuramos el frame que ejecuta el programa
framePr = Frame (root,width=290, height=778, background='white')
framePr.pack(side = 'left')
#Generamos y configuramos el frame que tiene la imagen
frameIm = Frame(root, width=710, height=778, background='white')
frameIm.pack_propagate(0)    
frameIm.pack(side = 'right')
img = ImageTk.PhotoImage(Image.open('metroAtenas.jpg'))
bgrIm = ImageTk.PhotoImage(Image.open('buttonIm.png'))
make_label(frameIm, img)
global destino, origen, seleccion
destino = StringVar()
origen = StringVar()
seleccion = IntVar()
seleccion.set(0)
origen.set("---Seleccionar Origen---")
destino.set("---Seleccionar Destino---")
Label(framePr,width=8, text= "Origen", bg=  "#D8D8D8", font=("Dolce Vita",13),relief="flat").grid(column=0,row=0,sticky="e")
Label(framePr,width=8, text= "Destino", bg= '#D8D8D8', font=("Dolce Vita",13),relief="flat").grid(column=0,row=1,sticky="e")
Label(framePr,width=20,textvariable= origen, bg= '#D8D8D8',font=("Dolce Vita",13),borderwidth = 1,relief="solid").grid(column=1,row=0,sticky="w")
Label(framePr, width=20,textvariable= destino,bg= '#D8D8D8' ,font=("Dolce Vita",13), borderwidth = 1,relief="solid").grid(column=1,row=1,sticky="w")
Label(framePr,height=2,bg="white").grid(column=0,row=3,columnspan=2)
Button(framePr ,text = "Calcular Ruta",width=15,relief="solid",borderwidth = 1,cursor="hand2",command= lambda: newWindow() ).grid(column=1,row=3)
btns = []
with open('coordImg.csv', newline='') as File:  
    reader = csv.reader(File,delimiter=';')
    for row in reader :
        print(row[0])
        btns.append([row[0],Button(frameIm ,width=5,height=5,borderwidth = 0,image=bgrIm,cursor="hand2")])
        btns[len(btns)-1][1].pack()
        btns[len(btns)-1][1].place(x=((int)(row[1])-4),y=((int)(row[2])-4))
    btns[0][1].config(command= lambda : origenDestino(btns[0][0]) )
    btns[1][1].config(command= lambda : origenDestino(btns[1][0]) )
    btns[2][1].config(command= lambda : origenDestino(btns[2][0]) )
    btns[3][1].config(command= lambda : origenDestino(btns[3][0]) )
    btns[4][1].config(command= lambda : origenDestino(btns[4][0]) )
    btns[5][1].config(command= lambda : origenDestino(btns[5][0]) )
    btns[6][1].config(command= lambda : origenDestino(btns[6][0]) )
    btns[7][1].config(command= lambda : origenDestino(btns[7][0]) )
    btns[8][1].config(command= lambda : origenDestino(btns[8][0]) )
    btns[9][1].config(command= lambda : origenDestino(btns[9][0]) )
    btns[10][1].config(command= lambda : origenDestino(btns[10][0]) )
    btns[11][1].config(command= lambda : origenDestino(btns[11][0]) )
    btns[12][1].config(command= lambda : origenDestino(btns[12][0]) )
    btns[13][1].config(command= lambda : origenDestino(btns[13][0]) )
    btns[14][1].config(command= lambda : origenDestino(btns[14][0]) )
    btns[15][1].config(command= lambda : origenDestino(btns[15][0]) )
    btns[16][1].config(command= lambda : origenDestino(btns[16][0]) )
    btns[17][1].config(command= lambda : origenDestino(btns[17][0]) )
    btns[18][1].config(command= lambda : origenDestino(btns[18][0]) )
    btns[19][1].config(command= lambda : origenDestino(btns[19][0]) )
    btns[20][1].config(command= lambda : origenDestino(btns[20][0]) )
    btns[21][1].config(command= lambda : origenDestino(btns[21][0]) )
    btns[22][1].config(command= lambda : origenDestino(btns[22][0]) )
    btns[23][1].config(command= lambda : origenDestino(btns[23][0]) ) 


   
        



root.mainloop()