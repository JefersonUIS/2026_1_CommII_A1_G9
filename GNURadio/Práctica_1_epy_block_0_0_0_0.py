import numpy as np
from gnuradio import gr

class blk(gr.sync_block):

    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='Diferenciador',
            in_sig=[np.float32],
            out_sig=[np.float32]
        )

        self.prev_sample = 0.0

    def work(self, input_items, output_items):

        entrada = input_items[0]
        salida = output_items[0]

        for i in range(len(entrada)):
            salida[i] = entrada[i] - self.prev_sample
            self.prev_sample = entrada[i]

        return len(salida)