import matplotlib.pyplot as plt
import math
import random

# Solicitar el número de nodos al usuario
n = int(input("Introduzca el número de nodos: "))

# Inicializar listas vacías para los datos de RSSI, distancias y nombres de nodos
rssi = []
distancias = []
nodos = []

# Parámetros de la ecuación de Friis
Pt = 20  # Potencia de transmisión (dBm)
Gt = 2  # Ganancia de la antena transmisora (dBi)
Gr = 2  # Ganancia de la antena receptora (dBi)
f = 2400  # Frecuencia de operación (MHz)
L = 2  # Pérdidas del medio (dB)

for i in range(n):
    nodo = i
    while True:
        rssi_valor = float(input("Introduzca el valor de RSSI del nodo "+ str(i) +": "))
        if rssi_valor<=(-30) and rssi_valor>=(-80):
            break
    #rssi_valor = random.uniform(-80, -30) para hacerlo random y que no haya que introducirlo

    nodos.append(nodo)#esto añade un valor al final del vector
    rssi.append(rssi_valor)

    # Calcular la distancia utilizando la ecuación de Friis
    # y agregarla a la lista de distancias
    Pr = rssi_valor + 20 * math.log10(10**((Gr + Gt) / 10)) - 20 * math.log10(f) - L
    d = 10**((Pt - Pr) / 20)
    distancias.append(d)

# Crear el gráfico de distancia vs. RSSI
plt.figure(figsize=(8, 6))  #Tamaño de la figura

# Grafica de los datos de distancia vs. RSSI
plt.plot(distancias, rssi, 'o-')
plt.xlabel('Distancia (m)')
plt.ylabel('RSSI (dBm)')
plt.title('Distancia vs. RSSI')
plt.grid(True)

#Agregar etiquetas a los puntos de datos
for i in range(n):
    plt.text(distancias[i], rssi[i], nodos[i])

plt.show()  # Mostrar gráfico
