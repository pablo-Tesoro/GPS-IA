from tkinter import *
from PIL import Image
from PIL import ImageTk
import csv

def make_label(parent, img):
    label = Label(parent, image=img)
    label.pack()
if __name__ == '__main__':

    #Generamos y configuramos la ventana
    root= Tk()
    root.config(bg='white')
    root.geometry("1000x780")
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
    Label(framePr, text= "Origen", bg= 'white', font=("Dolce Vita",13)).grid(column=0,row=0,padx=10,pady=10)
    Label(framePr, text= "Destino", bg= 'white', font=("Dolce Vita",13)).grid(column=0,row=1,padx=10,pady=10)
    Label(framePr, text= "---Selecciona Origen---", bg= 'white',font=("Dolce Vita",13),borderwidth = 2).grid(column=1,row=0,padx=10,pady=10)
    Label(framePr, text= "---Selecciona Destino---",bg= 'white' ,font=("Dolce Vita",13), borderwidth = 1).grid(column=1,row=1,padx=10,pady=10)
    Button(framePr ,text = 'Buscar Ruta',width=20,height=5,borderwidth = 1,cursor="hand2").grid(column=1,row=2,padx=10,pady=10)

    btns = []
    with open('coordImg.csv', newline='') as File:  
        reader = csv.reader(File,delimiter=';')
        for row in reader :
            btns.append([row[0],Button(frameIm ,width=5,height=5,borderwidth = 0,image=bgrIm,cursor="hand2")])
            btns[len(btns)-1][1].pack()
            btns[len(btns)-1][1].place(x=((int)(row[1])-4),y=((int)(row[2])-4))

root.mainloop()
