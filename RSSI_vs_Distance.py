#Tenemos valores de RSSI, necesitamos calcular las distancias y representarlas en una gráfica
import matplotlib.pyplot as plt
import math

RSSI=[] 
distancias=[]
i=0

# Parámetros de la ecuación de Friis
Pt = 20  # Potencia de transmisión (dBm)
Gt = 2  # Ganancia de la antena transmisora (dBi)
Gr = 2  # Ganancia de la antena receptora (dBi)
f = 2400  # Frecuencia de operación (MHz)
L = 2  # Pérdidas del medio (dB)

#introducir valores de RSSI
n=int(input("Cuantos nodos hay: "))
while i<n:
    while True:
        valor=float(input("Introduzca el valor del RSSI para el nodo "+ str(i) + ": "))
        if valor<=(-30) and valor>=(-80):
            break
    Pr = valor + 20 * math.log10(10**((Gr + Gt) / 10)) - 20 * math.log10(f) - L #esto es la formula de Friis
    dis = 10**((Pt - Pr) / 20)

    RSSI.append(valor)
    distancias.append(dis)
    i=i+1

#comenzamos con el grafico
plt.figure(figsize=(10,8)) #esto indica el tamaño

#establecemos los ejes y añadimos los valores
plt.plot(distancias,RSSI,'o-')
plt.xlabel("distancias (m)")
plt.ylabel("RSSI (dBm)")
plt.title("RSSI vs Distancia")
plt.grid(True)

#se muestra el gráfico
plt.show()











