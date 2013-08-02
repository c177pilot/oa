#!/usr/bin/env python
# 
# Copyright 2013 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr
try: import pmt
except: from gruel import pmt

class audio_mute(gr.basic_block):
    """
    docstring for block audio_ptt
    """
    def __init__(self):
        gr.basic_block.__init__(self,
            name="audio_ptt",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])
            
        self.message_port_register_in(pmt.intern('in2'))
        self.set_msg_handler(pmt.intern('in2'),self.handle_msg)
        
        self.mute  = False

    def handle_msg(self, msg):
        dict2 = pmt.to_python(msg)
        if dict2['buttons'][0] == 1:
            self.mute = True
        else:
            self.mute = False
            
    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = noutput_items
            
    def general_work(self, input_items, output_items):       
        a = len(output_items[0])
        if self.mute:
            output_items[0][:] = input_items[0][0:a]*0
            self.consume_each(len(output_items[0]))
            return len(output_items[0])
        else:
            output_items[0][:] = input_items[0][0:a]
            self.consume_each(len(input_items[0]))
            return len(output_items[0])
        
