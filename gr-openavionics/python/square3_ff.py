import numpy
from gnuradio import gr
 
class square3_ff(gr.sync_block):
   " Squaring block " 
   def __init__(self):
       gr.sync_block.__init__(
            self,
            name = "square3_ff",
            in_sig = [numpy.float32], # Input signature: 1 float at a time
            out_sig = [numpy.float32], # Output signature: 1 float at a time
        )
 
   def work(self, input_items, output_items):
       output_items[0][:] = input_items[0] * input_items[0] # Only works because numpy.array
       return len(output_items[0])
