# Importación de librerías
import numpy as np
from gnuradio import gr
import math

class blk(gr.sync_block):  
    """
    Bloque VCO de Envolvente Compleja (CE) o Banda Base. Representa la señal como un fasor en el plano complejo 
    utilizando la amplitud (A) y la fase (Q), sin incluir la frecuencia portadora[cite: 18, 20].
    """

    def __init__(self,):  
        # Se define que el bloque funcione 'uno a uno'; es decir, procesa y saca los datos en la misma 
        # medida en que le van llegando.
        gr.sync_block.__init__(
            self,
            name='e_CE_VCO_fc',   
            in_sig=[np.float32, np.float32], # Se definen las 2 entradas reales: A (Amplitud) y Q (Fase)
            out_sig=[np.complex64]           # Se define la salida de  la señal modulada en EC
        )
        
    def work(self, input_items, output_items):
        # Se le asignan variables a cada entrada del bloque
        A = input_items[0]  # Vector de amplitud (magnitud del vector)
        Q = input_items[1]  # Vector de fase (ángulo del vector en radianes)
        y = output_items[0] # Vector donde se guarda el resultado complejo
        
        N = len(A) # Cantidad de muestras a procesar en esta iteración
        
        # Aplicación vectorizada de la identidad de Euler: y[n] = A[n] * e^(j*Q[n]).
        #Este paso convierte los datos de formato polar (magnitud y fase) a  formato rectangular
        #(complejo), situando la señal en el plano complejo
        y[:] = A * np.exp(1j * Q)
        
        # Retornamos el número de muestras producidas
        return len(output_items[0])
