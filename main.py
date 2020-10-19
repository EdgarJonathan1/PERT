from tkinter import *
from tkinter import filedialog
from Graficadora import  Graficadora
from Graph import Graph
from pathlib import Path
import os

root = Tk()
root.title('Grafo Pert')
root.geometry("200x50")


content = ""
BASE_DIR = Path(__file__).resolve().parent.parent
# #############################################################################################
# ############################ Init Funciones #################################################
# #############################################################################################
def open_file():
    global content
    global  BASE_DIR
    print(BASE_DIR)

    # text_file = filedialog.askopenfilename(initialdir='/home/jonathan/Documentos/2S2020/IO1/Clase/Teoria de Redes/H14',title="Open File",filetypes=[("csv","*.csv")])
    text_file = filedialog.askopenfilename(initialdir=BASE_DIR,title="Open File",filetypes=[("csv","*.csv")])
    # Open the file
    text_file = open(text_file,'r')

    # el contenido del texto se guarda en la variable stuff
    stuff =  text_file.read()
    content = stuff

    # Close the opened file
    text_file.close()

def plot():
    grafo = Graph(content)
    graficadora = Graficadora(grafo)
    graficadora.graficar()
    pass
def calcPath():
    pass
 ############################################################################################
# ############################ Fin Funciones #################################################
# ############################################################################################

# Create a toolbar frame
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)

# Create Main Frame
my_frame = Frame(root)
my_frame.pack(pady=2,padx=2,side=LEFT)


# Create Menu
my_menu =Menu(root)
root.config(menu=my_menu)


# Add File Menu
file_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label='Archivo',menu=file_menu)
file_menu.add_command(label='Cargar Archivo',command=open_file)
file_menu.add_separator()
file_menu.add_command(label='Exit',command=root.quit)



# Boton analizador
Analizador_button = Button(toolbar_frame,text="Graficar",command=plot)
Analizador_button.grid(row=0,column=0,padx=5)

# Boton Reporte
Report_button = Button(toolbar_frame,text="Calcular rutas",command=calcPath)
Report_button.grid(row=0,column=20,padx=5)


root.mainloop()

