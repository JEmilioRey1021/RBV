import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def cargar_y_procesar_datos(ruta_csv, num_corridas):
    # Cargar los datos del archivo CSV
    datos = pd.read_csv(ruta_csv)
    
    # Inicializar listas para almacenar los datos procesados
    tiempos = []
    voltajes = []
    
    # Procesar cada par tiempo-corrida
    for i in range(num_corridas):
        tiempos.append(datos.iloc[:, i*2])
        voltajes.append(datos.iloc[:, i*2 + 1])
    
    return tiempos, voltajes

def calcular_derivada(t, V):
    return np.gradient(V.dropna(), t.dropna())

def generar_diagrama_fase_individual(t, V, corrida, titulo):
    dV_dt = calcular_derivada(t, V)
    plt.figure()
    plt.plot(V.dropna(), dV_dt)
    plt.xlabel('Voltaje (V)')
    plt.ylabel('dV/dt')
    plt.title(f'{titulo} - Corrida {corrida}')
    plt.show()

# Cargar y procesar datos del segundo archivo
tiempos_segunda_reaccion, voltajes_segunda_reaccion = cargar_y_procesar_datos('segundo_archivo.csv', 4)

# Generar diagramas de fase individuales para la segunda reacción
for i in range(4):
    generar_diagrama_fase_individual(tiempos_segunda_reaccion[i], voltajes_segunda_reaccion[i], i+1, 'Diagrama de fase - Segunda reacción BZ')
