from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import csv
from Algoritmo import Alg
import time

def comboChangedOrigen(event):
    origenDestino(variable1.get())
    
def comboChangedDestino(event):
    origenDestino(variable2.get())

def getCoords(estacion):
    lista = []
    for i in coords:
        if i[0] == estacion:
            lista.append((int)(i[1]))
            lista.append((int)(i[2]))
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
                comboOrigen.current(i+1)     
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
                comboDestino.current(i+1)

def showPath():
    global contLineas, al, canvas, coordsExtra, frameInfo, listbox, contaador
    if al.recorrido[contLineas] == destino.get():
        contLineas = 0
        destino.set("---Seleccionar Destino---") 
        origen.set("---Seleccionar Origen---") 
        fin = Label(frameInfo, text="Buen Viaje!", background="black", font=("Copperplate Gothic Bold", 15))
        fin.configure(fg="white")
        fin.place(x=80, y=670)
        listbox.insert(contaador, al.recorrido[contaador])
        return
    else:
        coordIn = getCoords(al.recorrido[contLineas])
        coordFin = getCoords(al.recorrido[contLineas+1])
        listaAux = []
        listaAux.append(coordIn)
        for i in coordsExtra:
            if(i[0] == al.recorrido[contLineas] and i[1] == al.recorrido[contLineas+1]):
                listaAux.append(i[2])    
        listaAux.append(coordFin)
        for j in range(len(listaAux)-1):
            coord1 = listaAux[j]
            coord2 = listaAux[j+1]
            canvas.create_line(coord1[0], coord1[1], coord2[0], coord2[1], fill="black", width=12)
            canvas.create_line(coord1[0], coord1[1], coord2[0], coord2[1], fill="gray", width=7)
            
            
        canvas.create_oval(coordIn[0]-8, coordIn[1]-8, coordIn[0]+8, coordIn[1]+8, fill="white")
        listbox.insert(contaador, al.recorrido[contaador])
        contaador += 1
        contLineas += 1
        canvas.after(300, showPath)
        canvas.create_oval(coordFin[0]-8, coordFin[1]-8, coordFin[0]+8, coordFin[1]+8, fill="white")
    
def newWindow():
    # Toplevel object which will
    #be treated as a new window
    
    global al, canvas, matriz, coordsExtra, criterio, frameInfo, listbox, contaador
    if(origen.get() == "---Seleccionar Origen---" or destino.get()== "---Seleccionar Destino---"):
        messagebox.showerror(title="Error", message="No se puede calcular la ruta si alguno de los camapos origen o destino esta vacio.")
        return
    else:
        al = Alg(origen.get(), destino.get(), varOpcion.get())
        al.main()
        contaador = 0
        camino = al.getRecorrido()
        newWindow = Toplevel(root, width=1000, height=778)
        newWindow.resizable(FALSE, FALSE)
        frameRuta = Frame(newWindow, width=710, height=778, background='white')
        frameRuta.pack_propagate(0)
        frameRuta.pack(side="left")
        frameInfo = Frame(newWindow, width=290, height=778, background='black')
        frameInfo.pack_propagate(0)
        frameInfo.pack(side="right")
        estaciones = Label(frameInfo, text="Estaciones: ", background="black", font=("Copperplate Gothic Bold", 15))
        estaciones.configure(fg="white")
        estaciones.place(x=80, y=30)
        listbox = Listbox(frameInfo, font=("Copperplate Gothic Bold", 11), background="black")  
        # for list in range (len(camino)):
        #      listbox.insert(list, camino[list])
        listbox.configure(fg="white")
        listbox.place(x=40, y=80)
        boton = Button(frameInfo, height="2", width="12", text="START", font=("Copperplate Gothic Bold", 11), cursor="hand2")
        boton.config(command=lambda:showPath())
        boton.configure(fg="black")
        boton.place(x=80, y=550)
        criterioBus = Label(frameInfo, text="Criterio: " + varOpcion.get(), background="black", font=("Copperplate Gothic Bold", 11))
        criterioBus.configure(fg="white")
        criterioBus.place(x=60, y=300)
        if(varOpcion.get() == "DISTANCIA"):
            valor = Label(frameInfo, text="Distancia(km): " + str(al.principal), background="black", font=("Copperplate Gothic Bold", 11))
            valor2 = Label(frameInfo, text="Tiempo(min): " + str(al.secundario), background="black", font=("Copperplate Gothic Bold", 11))
        else:
            valor = Label(frameInfo, text="Tiempo(min): " + str(al.principal), background="black", font=("Copperplate Gothic Bold", 11))
            valor2 = Label(frameInfo, text="Distancia(km): " + str(al.secundario), background="black", font=("Copperplate Gothic Bold", 11))
        valor.place(x=60, y=320)
        valor2.place(x=60, y=340)
        valor.configure(fg="white")
        valor2.configure(fg="white")
        lineas = Label(frameInfo, text="Lineas utilizadas: ", background="black", font=("Copperplate Gothic Bold", 11))
        lineas.configure(fg="white")
        lineas.place(x=60, y=360)
        
        coordsExtra = []
        for estacion in range (len(camino)-1):
            for row in matriz:
                if row[0] == camino[estacion] and row[1] == camino[estacion+1]:
                    coordsExtra.append(row)
                    
        # entry = ttk.Entry(frameInfo)
        # contador=0
        # for i in camino:
        #     entry.insert(contador, i)
        #     contador += 1
        # entry.pack()
        
        canvas = Canvas(frameRuta, width=710, height=778, bg='white')
        canvas.pack(anchor='nw', fill='both', expand=1)
        metro = Image.open('metroAtenas.png')
        metro = ImageTk.PhotoImage(metro)
        canvas.create_image(0,0,image=metro,anchor="nw")
        
        for i in camino:
            coords = getCoords(i)
            # imgAux = ImageTk.PhotoImage(Image.open('circle.png'))
            # label2Aux= Label(canvas,image=imgAux, width=12, height=12, borderwidth=0)
            # label2Aux.image = imgAux
            # label2Aux.place(x=coords[0]-6, y=coords[1]-6)
            canvas.create_oval(coords[0]-8, coords[1]-8, coords[0]+8, coords[1]+8, fill="white")
            
    coords1 = getCoords(origen.get())
    coords2 = getCoords(destino.get())
    tren.place_forget()
    bandera.place_forget()
    
    for i in range (54):
        if btns[i][0] == origen.get():
            btns[i][1].place(x=coords1[0]-5, y=coords1[1]-5)
        if btns[i][0] == destino.get():
            btns[i][1].place(x=coords2[0]-5, y=coords2[1]-5)

    seleccion.set(0)
    comboOrigen.current(0)
    comboDestino.current(0)

    newWindow.mainloop()
    
def make_label(parent, img):
    label = Label(parent, image=img)
    label.pack()
    return label

    #Generamos y configuramos la ventana

root= Tk()
root.config(bg='white')
root.geometry("1000x778")
root.title("Metro Atenas")
root.resizable(False,False)
root.iconbitmap("icono.ico")
#Generamos y configuramos el frame que ejecuta el programa
framePr = Frame (root,width=290, height=778, background='white')
framePr.pack(side = 'left')
imgg = ImageTk.PhotoImage(Image.open('metroAtenass.png'))
make_label(framePr, imgg)
#Label(framePr, width=8, text= "Origen", bg=  "#D8D8D8", font=("Dolce Vita",13),relief="flat").place(x=60, y=200)
#Generamos y configuramos el frame que tiene la imagen
frameIm = Frame(root, width=710, height=778, background='white')
frameIm.pack_propagate(0)    
frameIm.pack(side = 'right')
img = ImageTk.PhotoImage(Image.open('metroAtenas.png'))
imagen= Image.open('buttonIm.png')
bgrIm = ImageTk.PhotoImage(imagen) 
make_label(frameIm, img)
global destino, origen, seleccion, varOpcion, comboOrigen, comboDestino, contLineas, al, canvas, matriz, coordsExtra
coordsExtra = []
matriz = []
contLineas = 0
destino = StringVar()
origen = StringVar()
seleccion = IntVar()
varOpcion = StringVar()
tren = Label(frameIm)
bandera = Label(frameIm)
btns = []
coords = []
with open('coordImg.csv', newline='') as File:  
    reader = csv.reader(File,delimiter=';')
    for row in reader :
        btns.append([row[0],Button(frameIm,width =4, height = 4,border=0,image=bgrIm,cursor="hand2")])
        btns[len(btns)-1][1].pack()
        btns[len(btns)-1][1].place(x=((int)(row[1])-5),y=((int)(row[2])-5))
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
    
valuesOrigen = []
valuesDestino = []
valuesOrigen.append("---Seleccionar Origen---")
valuesDestino.append("---Seleccionar Destino---")
for i in range (54):
    valuesOrigen.append(btns[i][0])
    valuesDestino.append(btns[i][0])
variable1 = StringVar()
variable2 = StringVar()
comboOrigen= ttk.Combobox(framePr, textvariable = variable1)
comboDestino= ttk.Combobox(framePr, textvariable = variable2)
comboOrigen['values'] = valuesOrigen
comboOrigen['state'] = 'readonly'
comboOrigen.current(0)
comboOrigen.place(x=90, y=200)
comboDestino['values'] = valuesDestino
comboDestino['state'] = 'readonly'
comboDestino.current(0)
comboDestino.place(x=90, y=230)
varOpcion.set("DISTANCIA")
Radiobutton(framePr, text="Distancia", width=8,variable=varOpcion, value="DISTANCIA", bg="white",font=("Dolce Vita",11)).place(x=90, y=320)
Radiobutton(framePr, text="Tiempo", width=8,variable=varOpcion, value="TIEMPO", bg="white", font=("Dolce Vita",11)).place(x=90, y=380)
Button(framePr ,text = "Calcular Ruta",width=25, height=2,relief="solid",borderwidth = 1,cursor="hand2",command= lambda: newWindow() ).place(x=60, y=450)
comboOrigen.bind('<<ComboboxSelected>>', comboChangedOrigen)
comboDestino.bind('<<ComboboxSelected>>', comboChangedDestino)
origen.set("---Seleccionar Origen---")
destino.set("---Seleccionar Destino---")
contMatriz = 0
with open('coordsAux.csv', newline='') as File:  
    reader = csv.reader(File,delimiter=';')
    for row in reader :
        matriz.append([])
        coordsAux = []
        coordsAux.append((int)(row[2]))
        coordsAux.append((int)(row[3]))
        matriz[contMatriz].append(row[0])
        matriz[contMatriz].append(row[1])
        matriz[contMatriz].append(coordsAux)
        contMatriz += 1
root.mainloop()