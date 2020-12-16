# **Investigacion de operaciones 1 - Universidad Distrital**

<img src="https://www.udistrital.edu.co/themes/custom/versh/images/default/preloader.png" align="left" width="192px" height="192px"/>
<img align="left" width="0" height="192px" hspace="10"/>


## Integrantes: 
- Ariel Ernesto Forero Meneses  - **COD. 20181020135**
- Jose David Ramirez Maldonado  - **COD. 20181020047**
- Jaime Nicolas Castro Acuña  - **COD. 20181020147**

[![Ariel Ernesto Forero Meneses](https://img.shields.io/badge/arefome-github-br?style=flat-square)](https://github.com/arefome)
[![Jose David Ramirez Maldonado](https://img.shields.io/badge/JoseDRamirezM-github-br?style=flat-square)](https://github.com/JoseDRamirezM)

---
# **Manual de usuario**
La forma de ingresar los plantemientos se hace mediante archivos .txt de la siguiente manera

```python
#Primera linea: el numero de metodo de solucion siempre sera igual a dos, para ejecutar el metodo de las dos fases
metodo de solucion, maximizar(max) o minimizar(min), numero de variables,numero de restricciones
#Segunda linea: coeficientes de las variables
coef 1, coef  2, coef 3,..., coef n
#Tercera linea: restricciones, se soportan todos los tipos de desigualdades
coef 1, coef 2, coef 3,..., coef n, <=, lado derecho
coef 1, coef 2, coef 3,..., coef n, <=, lado derecho
.
.
.
```
A continuación un ejemplo de la entrada de un problema de maximización.
```python
2,max,2,3
4,6
2,1,<=,180
1,2,<=,160
1,1,<=,100
```
A continuación un ejemplo de la entrada de un problema de minimización.
```python
2,min,2,3
2,3
0.5,0.25,<=,4
1,3,>=,20
1,1,=,10
```
Posteriormente en el archivo 'main.py' en la linea 45 asignamos el nombre del archivo
que contiene el problema, a continuacion un ejemplo:
```python
main("nombreDelArchivo.txt")
```

