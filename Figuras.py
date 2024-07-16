import math
import os
import datetime
from crearDBcaras import verificar_facial

print("--CIRCULO----ESFERA--")
radio= int(input("Ingrese el radio de la Figura: "))

print("Por favor, mire a la cámara para la verificación facial.")
nombre_empleado = verificar_facial()
if nombre_empleado:
    print(f"Bienvenido {nombre_empleado}")
    AreaC = (2*math.pi*radio)
    AreaE= ((4*math.pi)*(radio*radio))
    print("Area del Circulo= ",AreaC)
    print("Area de la Esfera= ",AreaE)
else:
    print("Verificación facial fallida. No se encontró coincidencia.")
    VolumenE= ((4/3*math.pi) *(radio*radio*radio))
    print("Volumen Esfera= ",VolumenE)
    print("EL Circulo no tiene Volumen.")
