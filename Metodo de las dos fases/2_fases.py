import math
import numpy as np

def calcular1(self):
        #Asignando los valores de las inecuaciones a la nueva matriz
        for i in range(self.__numIne):
            for j in range(4):
                self.__Valores[i][j] = self.__inecuaciones[i][j].get()
                if(j == 0):
                    self.__X[i] = float(self.__Valores[i][j])
                if(j == 1):
                    self.__Y[i] = float(self.__Valores[i][j])
                if(j == 2):
                    self.__signo[i] = self.__Valores[i][j]
                if(j == 3):
                    self.__C[i] = float(self.__Valores[i][j])

        #Despejando las variables X y Y
        for i in range(self.__numIne - 2):
            if self.__Y[i] > 0 or self.__Y[i] < 0:
                self.__puntoX[i] = self.__C[i]/self.__Y[i] #Cuando X = 0

            else:
                self.__puntoX[i] = 0 #Cuando X = 0


            if self.__X[i] > 0 or self.__X[i] < 0:
                self.__puntoY[i] = self.__C[i]/self.__X[i] #Cuando Y = 0

            else:
                self.__puntoY[i] = 0 #Cuando Y = 0
             

            self.__area[i] = abs(self.__puntoX[i]*self.__puntoY[i]/2)

        #self.__puntoX tiene los puntos de corte con el eje X
        #self.__puntoY tiene los puntos de corte con el eje Y
        
        for i in range(self.__numIne - 2):
            if(self.__signo[i] == '>='):
                self.__estado[i] = 1
            else:
                self.__estado[i] = 0

        self.__areaOrd = sorted(self.__area)
        for i in range(self.__numIne-2):
            if(self.__areaOrd[0] == self.__area[i]):
                self.__q = i



def to_tableau(c, A, b):
    xb = [eq + [x] for eq, x in zip(A, b)]
    z = c + [0]
    return xb + [z]


def pivot_step(tableau, pivot_position):
    new_tableau = [[] for eq in tableau]
    
    i, j = pivot_position
    pivot_value = tableau[i][j]
    new_tableau[i] = np.array(tableau[i]) / pivot_value
    
    for eq_i, eq in enumerate(tableau):
        if eq_i != i:
            multiplier = np.array(new_tableau[i]) * tableau[eq_i][j]
            new_tableau[eq_i] = np.array(tableau[eq_i]) - multiplier
   
    return new_tableau

def is_basic(column):
    return sum(column) == 1 and len([c for c in column if c == 0]) == len(column) - 1

def get_solution(tableau):
    columns = np.array(tableau).T
    solutions = []
    for column in columns[:-1]:
        solution = 0
        if is_basic(column):
            one_index = column.tolist().index(1)
            solution = columns[-1][one_index]
        solutions.append(solution)
        
    return solutions

def can_be_improved_for_dual(tableau):
    rhs_entries = [row[-1] for row in tableau[:-1]]
    return any([entry < 0 for entry in rhs_entries])

def get_pivot_position_for_dual(tableau):
    rhs_entries = [row[-1] for row in tableau[:-1]]
    min_rhs_value = min(rhs_entries)
    row = rhs_entries.index(min_rhs_value)
    
    columns = []
    for index, element in enumerate(tableau[row][:-1]):
        if element < 0:
            columns.append(index)
    columns_values = [tableau[row][c] / tableau[-1][c] for c in columns]
    column_min_index = columns_values.index(min(columns_values))
    column = columns[column_min_index]

    return row, column

def dos_fases(c, A, b):
    tableau = to_tableau(c, A, b)

    while can_be_improved_for_dual(tableau):
        pivot_position = get_pivot_position_for_dual(tableau)
        tableau = pivot_step(tableau, pivot_position)

    return get_solution(tableau)





class Calcular_Puntos(object):
    def __init__(self, x, y):
        #Atributos

        #Matriz que contiene los campos de texto de las inecuaciones
        self.__inecuaciones = x
        #El numero de inecuaciones
        self.__numIne = y
        #La matriz con valores de las inecuaciones
        self.__Valores = []

        self.__area = list(range(self.__numIne-2))
        self.__q = 0
        self.__areaOrd = list(range(self.__numIne-2))
        self.__lista = list(range(self.__numIne-2))
        #Lista que contiene los valores de X
        self.__X = list(range(self.__numIne))
        #Lista que contiene los valores de Y
        self.__Y = list(range(self.__numIne))
        #Lista que contiene los valores constantes
        self.__C = list(range(self.__numIne))
        #Lista que contiene el signo de la inecuacion
        self.__signo = list(range(self.__numIne))
        #Lista que contiene los puntos cuando X=0
        self.__puntoX = list(range(self.__numIne-2))
        #Lista que contiene los puntos cuando Y=0
        self.__puntoY = list(range(self.__numIne-2))
        #Lista que contiene los puntos X a evaluar en la funcion objetivo
        self.__fX = list(range(self.__numIne))
        #Lista que contiene los puntos Y a evaluar en la funcion objetivo
        self.__fY = list(range(self.__numIne))
        #lista que contiene la pendiente de cada recta
        self.__m = list(range(self.__numIne))
        #Lista que contiene la constante de cada recta
        self.__b = list(range(self.__numIne))
        #Lista que guarda los valores reemplazados en la funcion
        self.__resul = list(range(self.__numIne))
        
        self.__estado = list(range(self.__numIne))

        self.__a = 0

        #Inicializando la matriz2
        for i in range(self.__numIne):
            self.__Valores.append([])
            for j in range(4): 
                self.__Valores[i].append(None)


    def calcular(self):
        #Asignando los valores de las inecuaciones a la nueva matriz
        for i in range(self.__numIne):
            for j in range(4):
                self.__Valores[i][j] = self.__inecuaciones[i][j].get()
                if(j == 0):
                    self.__X[i] = float(self.__Valores[i][j])
                if(j == 1):
                    self.__Y[i] = float(self.__Valores[i][j])
                if(j == 2):
                    self.__signo[i] = self.__Valores[i][j]
                if(j == 3):
                    self.__C[i] = float(self.__Valores[i][j])

        #Despejando las variables X y Y
        for i in range(self.__numIne - 2):
            if self.__Y[i] > 0 or self.__Y[i] < 0:
                self.__puntoX[i] = self.__C[i]/self.__Y[i] #Cuando X = 0

            else:
                self.__puntoX[i] = 0 #Cuando X = 0


            if self.__X[i] > 0 or self.__X[i] < 0:
                self.__puntoY[i] = self.__C[i]/self.__X[i] #Cuando Y = 0

            else:
                self.__puntoY[i] = 0 #Cuando Y = 0
             

            self.__area[i] = abs(self.__puntoX[i]*self.__puntoY[i]/2)
            
        
        for i in range(self.__numIne - 2):
            if(self.__signo[i] == '>='):
                self.__estado[i] = 1
            else:
                self.__estado[i] = 0

        self.__areaOrd = sorted(self.__area)
        for i in range(self.__numIne-2):
            if(self.__areaOrd[0] == self.__area[i]):
                self.__q = i

def evaluar_funcion_objetivo(c, solucion):
    return sum(np.array(c) * np.array(solucion))

c = [7,-10,0,0,0]
A = [
    [-1, 1, 1, 0, 0],
    [-1, -5, 0, 1, 0],
    [-1, 1, 0, 0, 1]
]
b = [-4, 8, -1]

d = [180, 160, 100, 0, 0]

E = [
    [-2, -1, -1, 1, 0],
    [-1, -2, -1, 0, 1]
]

f = [-4, -6]

dual = evaluar_funcion_objetivo(c, dos_fases(c, A, b))
print('Dual: ', dual)

dual2 = evaluar_funcion_objetivo(d, dos_fases(d,E,f))
print('Dual: ', dual2)