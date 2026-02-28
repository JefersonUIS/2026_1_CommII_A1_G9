import numpy as np
from gnuradio import gr

class blk(gr.sync_block):

    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='Analizador_Estadistico',
            in_sig=[np.float32],
            out_sig=[np.float32,
                     np.float32,
                     np.float32,
                     np.float32,
                     np.float32]
        )

    def work(self, input_items, output_items):

        signal_in = input_items[0]

        mean_out = output_items[0]
        avg_out  = output_items[1]
        rms_out  = output_items[2]
        power_out = output_items[3]
        std_out  = output_items[4]

        # Media aritmética
        mean_value = np.mean(signal_in)

        # Potencia media
        power_value = np.mean(signal_in**2)

        # RMS
        rms_value = np.sqrt(power_value)

        # Desviación estándar
        std_value = np.std(signal_in)

        mean_out[:] = mean_value
        avg_out[:]  = mean_value
        rms_out[:]  = rms_value
        power_out[:] = power_value
        std_out[:]  = std_value

        return len(signal_in)