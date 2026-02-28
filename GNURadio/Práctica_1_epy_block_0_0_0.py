import numpy as np
from gnuradio import gr

class blk(gr.sync_block):

    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='Acumulador',
            in_sig=[np.float32],
            out_sig=[np.float32]
        )

        self.total = 0.0   # memoria del sistema

    def work(self, input_items, output_items):

        entrada = input_items[0]
        salida = output_items[0]

        for i in range(len(entrada)):
            self.total += entrada[i]
            salida[i] = self.total

        return len(salida)
