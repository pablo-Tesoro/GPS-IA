
import cv2
import csv
from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import imutils
import numpy as np



#Creamos los botones
# btns = []
# with open('coordImg.csv', newline='') as File:  
#     reader = csv.reader(File,delimiter=';')
#     for row in reader :
#         btns.append([row[0],Button(root, text= "texto prueba" ,bg='green',width=1)])
#         btns[len(btns)-1][1].pack()
#         btns[len(btns)-1][1].place(x=row[1],y=row[2])
# labelImage = Label(root)
def openNewWindow ():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(root)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
    # sets the geometry of toplevel
    # frame2 = Frame(newWindow, width=700, height=750, background='white')
    # frame2.pack_propagate(0)    
    # frame2.pack()
    img2 = ImageTk.PhotoImage(Image.open('Leguina.jpg'))
    label2= Label(newWindow,image=img2)
    label2.image = img2
    label2.pack()

    # A Label widget to show in toplevel
    Label(newWindow,
          text ="This is a new window").pack()

def make_label(parent, img):
    label = Label(parent, image=img)
    label.pack()
if __name__ == '__main__':
    root = Tk()
    root.title("Metro Atenas")
    root.resizable(False,False)
    root.iconbitmap("icono.ico")
    frame = Frame(root, width=710, height=778, background='white')
    frame.pack_propagate(0)    
    frame.pack()
    img = ImageTk.PhotoImage(Image.open('metroAtenas.jpg'))
    bgrIm = ImageTk.PhotoImage(Image.open('buttonIm.png'))
    make_label(frame, img)
    btns = []
    with open('coordImg.csv', newline='') as File:  
        reader = csv.reader(File,delimiter=';')
        for row in reader :
            btns.append([row[0],Button(root ,width=5,height=5,borderwidth = 0,image=bgrIm,cursor="hand2",command= openNewWindow)])
            btns[len(btns)-1][1].pack()
            btns[len(btns)-1][1].place(x=((int)(row[1])-5),y=((int)(row[2])-5))
root.mainloop()


# def click_event(event, x, y, flags, params):

#     if event == cv2.EVENT_LBUTTONDOWN:
#         pass
#     if event==cv2.EVENT_RBUTTONDOWN:
#         pass


# # driver function
# if __name__=="__main__":

#     img = cv2.imread('metroAtenas.jpg',1)

#     cv2.imshow('image', img)

#     cv2.setMouseCallback('image', click_event)

#     cv2.waitKey(0)

#     cv2.destroyAllWindows()