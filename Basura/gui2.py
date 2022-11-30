from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import csv
from Algoritmo import Alg

def getCoords(estacion):
    lista = []
    for i in coords:
        if i[0] == estacion:
            lista.append((int)(i[1])-4)
            lista.append((int)(i[2])-4)
    return lista
            
def origenDestino (estacion):

    if(seleccion.get() == 0) :
        origen.set(estacion)
        seleccion.set(1)
        lista = getCoords(estacion)
        imgTren = ImageTk.PhotoImage(Image.open('tren.jpg'))
        tren.config(image=imgTren, borderwidth=0, font=("Dolce Vita",13),relief="flat")
        tren.image = imgTren
        tren.place(x=lista[0]-10, y=lista[1]-10)
        for i in range(54):
            if btns[i][0] == estacion:
                btns[i][1].place_forget()
        
        
                
    else:
        destino.set(estacion) 
        seleccion.set(0)
        lista = getCoords(estacion)
        imgBand = ImageTk.PhotoImage(Image.open('bandera.png'))
        bandera.config(image=imgBand, borderwidth=0, font=("Dolce Vita",13),relief="flat")
        bandera.image = imgBand
        bandera.place(x=lista[0]-10, y=lista[1]-10)
        for i in range(54):
            if btns[i][0] == estacion:
                btns[i][1].place_forget()

def newWindow():
    # Toplevel object which will
    #be treated as a new window
    
    texto = StringVar()
    if(origen.get() == "---Seleccionar Origen---" or destino.get()== "---Seleccionar Destino---"):
        messagebox.showerror(title="Error", message="No se puede calcular la ruta si alguno de los camapos origen o destino esta vacio.")
    else:
        al = Alg(origen.get(), destino.get())
        al.main()
        camino = al.getRecorrido()
        newWindow = Toplevel(root)
        texto.set("Se puede")
        frameRuta = Frame(newWindow, width=710, height=778, background='white')
        frameRuta.pack_propagate(0)
        frameRuta.pack()
        canvas = Canvas(frameRuta, width=710, height=778, bg='white')
        canvas.pack(expand=YES, fill=BOTH)
        aux = Label(canvas, image=img)
        aux.image = img
        aux.pack()
        
        
        for i in camino:
            coords = getCoords(i)
            imgAux = ImageTk.PhotoImage(Image.open('LeguinaPeque.jpg'))
            label2Aux= Label(canvas,image=imgAux, width=18, height=18)
            label2Aux.image = imgAux
            label2Aux.place(x=coords[0]-10, y=coords[1]-10)
            
        fin = FALSE
        cont = 0
        while fin == FALSE:
            if al.recorrido[cont+1] == destino.get():
                fin = TRUE
            coord1 = getCoords(al.recorrido[cont])
            coord2 = getCoords(al.recorrido[cont+1])
            canvas.create_line(coord1[0], coord1[1], coord2[0], coord2[1], fill="green", width=3)
            cont += 1
        
    coords1 = getCoords(origen.get())
    coords2 = getCoords(destino.get())
    tren.place_forget()
    bandera.place_forget()
    
    for i in range (54):
        if btns[i][0] == origen.get():
            btns[i][1].place(x=coords1[0], y=coords1[1])
        if btns[i][0] == destino.get():
            btns[i][1].place(x=coords2[0], y=coords2[1])
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
global destino, origen, seleccion, varOpcion
destino = StringVar()
origen = StringVar()
seleccion = IntVar()
varOpcion = IntVar()
seleccion.set(0)
origen.set("---Seleccionar Origen---")
destino.set("---Seleccionar Destino---")
Label(framePr,width=8, text= "Origen", bg=  "#D8D8D8", font=("Dolce Vita",13),relief="flat").grid(column=0,row=0,sticky="e")
Label(framePr,width=8, text= "Destino", bg= '#D8D8D8', font=("Dolce Vita",13),relief="flat").grid(column=0,row=1,sticky="e")
Label(framePr,width=20,textvariable= origen, bg= '#D8D8D8',font=("Dolce Vita",13),borderwidth = 1,relief="solid").grid(column=1,row=0,sticky="w")
Label(framePr, width=20,textvariable= destino,bg= '#D8D8D8' ,font=("Dolce Vita",13), borderwidth = 1,relief="solid").grid(column=1,row=1,sticky="w")
Label(framePr,height=6,bg="white").grid(column=0,row=2,columnspan=2)

Radiobutton(framePr, text="Distancia", width=8,variable=varOpcion, value="1", bg="white", font=("Dolce Vita",11)).grid(column=0, row=5, columnspan=2)
Label(framePr,height=1,bg="white").grid(column=0,row=6,columnspan=2)
Radiobutton(framePr, text="Tiempo   ", width=8,variable=varOpcion, value="2", bg="white", font=("Dolce Vita",11)).grid(column=0, row=7, columnspan=2)
Label(framePr,height=6,bg="white").grid(column=0,row=8,columnspan=2)
tren = Label(frameIm)
bandera = Label(frameIm)
Button(framePr ,text = "Calcular Ruta",width=25, height=2,relief="solid",borderwidth = 1,cursor="hand2",command= lambda: newWindow() ).grid(column=0,row=9, columnspan=2)
btns = []
coords = []
with open('coordImg.csv', newline='') as File:  
    reader = csv.reader(File,delimiter=';')
    for row in reader :
        btns.append([row[0],Button(frameIm ,width=5,height=5,borderwidth = 0,image=bgrIm,cursor="hand2")])
        btns[len(btns)-1][1].pack()
        btns[len(btns)-1][1].place(x=((int)(row[1])-4),y=((int)(row[2])-4))
        coords.append([row[0], row[1], row[2]])
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
    btns[24][1].config(command= lambda : origenDestino(btns[24][0]) )
    btns[25][1].config(command= lambda : origenDestino(btns[25][0]) )
    btns[26][1].config(command= lambda : origenDestino(btns[26][0]) )
    btns[27][1].config(command= lambda : origenDestino(btns[27][0]) )
    btns[28][1].config(command= lambda : origenDestino(btns[28][0]) )
    btns[29][1].config(command= lambda : origenDestino(btns[29][0]) )
    btns[30][1].config(command= lambda : origenDestino(btns[30][0]) )
    btns[31][1].config(command= lambda : origenDestino(btns[31][0]) )
    btns[32][1].config(command= lambda : origenDestino(btns[32][0]) )
    btns[33][1].config(command= lambda : origenDestino(btns[33][0]) )
    btns[34][1].config(command= lambda : origenDestino(btns[34][0]) )
    btns[35][1].config(command= lambda : origenDestino(btns[35][0]) )
    btns[36][1].config(command= lambda : origenDestino(btns[36][0]) )
    btns[37][1].config(command= lambda : origenDestino(btns[37][0]) )
    btns[38][1].config(command= lambda : origenDestino(btns[38][0]) )
    btns[39][1].config(command= lambda : origenDestino(btns[39][0]) )
    btns[40][1].config(command= lambda : origenDestino(btns[40][0]) )
    btns[41][1].config(command= lambda : origenDestino(btns[41][0]) )
    btns[42][1].config(command= lambda : origenDestino(btns[42][0]) )
    btns[43][1].config(command= lambda : origenDestino(btns[43][0]) )
    btns[44][1].config(command= lambda : origenDestino(btns[44][0]) )
    btns[45][1].config(command= lambda : origenDestino(btns[45][0]) )
    btns[46][1].config(command= lambda : origenDestino(btns[46][0]) )
    btns[47][1].config(command= lambda : origenDestino(btns[47][0]) )
    btns[48][1].config(command= lambda : origenDestino(btns[48][0]) )
    btns[49][1].config(command= lambda : origenDestino(btns[49][0]) )
    btns[50][1].config(command= lambda : origenDestino(btns[50][0]) )
    btns[51][1].config(command= lambda : origenDestino(btns[51][0]) )
    btns[52][1].config(command= lambda : origenDestino(btns[52][0]) )
    btns[53][1].config(command= lambda : origenDestino(btns[53][0]) )

root.mainloop()