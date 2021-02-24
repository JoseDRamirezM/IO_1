import sys
import tkinter as tk
from archivo import Archivo
from granm import GranM
from dosfases import DosFases
from simplex import Simplex


def encontrar_solucion(archivo):
    try:
            problem = Archivo.leer_archivo(archivo)

            # 0=Simplex, 1=GranM, 2=DosFases
            if problem.metodo == 0 or problem.metodo == "simplex":
                try:
                    print("simplex")
                    simplex = Simplex(problem, archivo)
                    simplex.setup()
                    simplex.solucion()
                except:
                    return "Error al ejecutar simplex"

            elif problem.metodo == 1 or problem.metodo == "granm":
                try:
                    print("gran m")
                    big_m = GranM(problem, archivo)
                    big_m.setup()
                    big_m.solucion()
                except:
                    return "Error al ejecutar Gran M"

            elif problem.metodo == 2 or problem.metodo == "dosfases":
                try:
                    print("Metodo de las dos fases")
                    two_phases = DosFases(problem, archivo)
                    two_phases.solve()
                    two_phases.solucion()

                except:
                    print("error")
                    return "Error al ejecutar Dos fases"

    except:
        print("El archivo presenta un problema")

