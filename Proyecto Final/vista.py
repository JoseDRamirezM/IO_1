
import tkinter as tk
from archivo import Archivo
from inicial import encontrar_solucion
from solucion import VentanaResultados
import sys

def calcular_inecuaciones():
    objeto = Inecuaciones(numIne.get())
    objeto.iniciar()

    #Boton para enviar inecuaciones
    btnCalcular = tk.Button(marco, text ="Calcular", command = objeto.hacer_algo, width = 10)
    btnCalcular.pack()
    btnCalcular.place(x = 450, y = 300)

class Inecuaciones():
    def __init__(self, x):
        #Atributos

        #El numero de inecuaciones
        self.__numIne = int(x)
        #Matriz donde se guardan los campos de las inecuaciones
        self.__Inecuaciones = []
        self.__CalcularPuntos = None

        #Inicializando la matriz
        for i in range(self.__numIne):
            self.__Inecuaciones.append([])
            for j in range(4): 
                self.__Inecuaciones[i].append(None)

    def iniciar(self):
        #Creando los campos para las inecuaciones
        for i in range(self.__numIne):
            for j in range(4):
                self.__Inecuaciones[i][j] = tk.Entry(marco, width = 7)
                self.__Inecuaciones[i][j].pack()
                self.__Inecuaciones[i][j].place(x = j*100 + 100, y = i*30 + 150)

                if j == 2:
                    if i >= self.__numIne - 2:
                        self.__Inecuaciones[i][j].insert(0, ">=")
                        self.__Inecuaciones[i][j].config(state = "readonly")
                    else:
                        self.__Inecuaciones[i][j].insert(0, "<=")

        #Se muestran las inecuaciones de positividad de las variables
        self.__Inecuaciones[self.__numIne - 2][0].insert(0, "1")
        self.__Inecuaciones[self.__numIne - 2][0].config(state = "readonly")
        self.__Inecuaciones[self.__numIne - 2][1].insert(0, "0")
        self.__Inecuaciones[self.__numIne - 2][1].config(state = "readonly")
        self.__Inecuaciones[self.__numIne - 2][3].insert(0, "0")
        self.__Inecuaciones[self.__numIne - 2][3].config(state = "readonly")

        self.__Inecuaciones[self.__numIne - 1][0].insert(0, "0")
        self.__Inecuaciones[self.__numIne - 1][0].config(state = "readonly")
        self.__Inecuaciones[self.__numIne - 1][1].insert(0, "1")
        self.__Inecuaciones[self.__numIne - 1][1].config(state = "readonly")
        self.__Inecuaciones[self.__numIne - 1][3].insert(0, "0")
        self.__Inecuaciones[self.__numIne - 1][3].config(state = "readonly")
    
    def hacer_algo(self):
        lista_valores=[]
        lista_final=[]
        for val in range(len(self.__Inecuaciones)):
            for j in range(4):
                lista_valores.append(self.__Inecuaciones[val][j].get())
                lista_separada = [lista_valores[x:x+4] for x in range(0, len(lista_valores),4)]
                lista_final = lista_separada

        #
        lista_strings=[]
        for lista in (lista_final):
            linea = ""
            for x in range(len(lista)):
                if x != len(lista)-1:
                    linea = linea + lista[x] + ","
                else:
                    linea = linea + lista[x]
            lista_strings.append(linea)

        lista_strings
        del lista_strings[-2:]
        
        Archivo.crear_modelo(lista_strings)
        
        root = tk.Tk()
        root.title("Solución Modelo optimización Tasajero II")
        VentanaResultados(root).pack(expand=True, fill=tk.BOTH)
        encontrar_solucion("planta_termo_electrica.txt")
        root.mainloop()


#Crea el marco
marco = tk.Tk()
marco.title("Modelo optimización Tasajero II")
marco.geometry("600x400")
marco.configure(background="#ddd7c9")

#Etiquetas
lbl1 = tk.Label(marco, text = "Función objetivo: ")
lbl1.pack()
lbl1.configure(background="#ddd7c9")
lbl1.place(x = 0, y = 30)

lbl2 = tk.Label(marco, text = "X      +")
lbl2.pack()
lbl2.configure(background="#ddd7c9")
lbl2.place(x = 230, y = 30)

lbl3 = tk.Label(marco, text = "Y")
lbl3.pack()
lbl3.configure(background="#ddd7c9")
lbl3.place(x = 380, y = 30)

lbl4 = tk.Label(marco, text = "max o min")
lbl4.pack()
lbl4.configure(background="#cc99ff")
lbl4.place(x = 460, y = 5)

lbl5 = tk.Label(marco, text = "Digite el numero de inecuaciones: ")
lbl5.pack()
lbl5.configure(background="#ddd7c9")
lbl5.place(x = 210, y = 60)

lbl6 = tk.Label(marco, text = "")
lbl6.pack()
lbl6.configure(background="#cc99ff")
lbl6.place(x = 100, y = 350)

lbl7 = tk.Label(marco, text = "Coef X")
lbl7.pack()
lbl7.configure(background="#ddd7c9")
lbl7.place(x = 100, y = 120)

lbl8 = tk.Label(marco, text = "Coef Y")
lbl8.pack()
lbl8.configure(background="#ddd7c9")
lbl8.place(x = 200, y = 120)

#Funcion objetivo
fObj1 = tk.Entry(marco, width = 10)
fObj1.pack(anchor = tk.CENTER)
fObj1.config(background="#ffffff")
fObj1.place(x = 150, y = 30)

fObj2 = tk.Entry(marco, width = 10)
fObj2.pack(anchor = tk.CENTER)
fObj2.config(background="#ffffff")
fObj2.place(x = 300, y = 30)

fObj3 = tk.Entry(marco, width = 10)
fObj3.pack(anchor = tk.CENTER)
fObj3.config(background="#ffffff")
fObj3.place(x = 450, y = 30)

#Inecuaciones
numIne = tk.Entry(marco, width = 10)
numIne.pack(anchor = tk.CENTER)
numIne.config(background="#ffffff")
numIne.place(x = 200, y = 90)

#Boton enviar inecuaciones
btnEnviar = tk.Button(marco, text ="Enviar", command = calcular_inecuaciones, width = 10)
btnEnviar.pack()
btnEnviar.place(x = 350, y = 90)

marco.mainloop()
