#Importación de librerías
import numpy as np
from gnuradio import gr
import math

class blk(gr.sync_block):  
    """
    Bloque VCO de Radiofrecuencia (RF).
    Sintetiza una señal portadora y la modula utilizando las variaciones 
    instantáneas de amplitud (A) y fase (Q).
    """

    def __init__(self, fc=128000, samp_rate=320000):  
# Se define que el bloque funcione 'uno a uno'; es decir, procesa y saca los datos en la misma medida en que
#le van llegando
        gr.sync_block.__init__(
            self,
            name='e_RF_VCO_ff',              
            in_sig=[np.float32, np.float32], # Se definen las 2 entradas del bloque: A (Amplitud) y Q (Fase)
            out_sig=[np.float32]             # Se definen la salida del bloque: y (Señal modulada en RF)
        )
        
        # Asignamos variables a los parámetros del bloque.
        self.fc = fc                   # Frecuencia portadora (Hz)
        self.samp_rate = samp_rate     # Frecuencia de muestreo (Hz)
        
        # Acumulador de tiempo (índice de muestras).
        self.n_m = 0

    def work(self, input_items, output_items):
        #Se le asignan variables a cada entrada del bloque
        A = input_items[0]  # Vector de amplitud
        Q = input_items[1]  # Vector de fase (en radianes)
        y = output_items[0] # Vector donde se guarda el resultado
        
        N = len(A) # Cantidad de muestras a procesar en esta iteración (tamaño del bloque)
        
        # Generación del vector de tiempo discreto "n" que va desde el valor histórico actual hasta N-1 muestras en el futuro.
        n = np.linspace(self.n_m, self.n_m + N - 1, N)
        
        # Actualizamos el contador histórico sumándole las muestras recién procesadas
        self.n_m += N
        
        # Aplicación vectorizada de la ecuación del VCO: y[n] = A[n] * cos(2*pi*fc*n/fs + Q[n])
        y[:] = A * np.cos(2 * math.pi * self.fc * n / self.samp_rate + Q)
        # Retornamos el número de muestras producidas
        return len(output_items[0])
