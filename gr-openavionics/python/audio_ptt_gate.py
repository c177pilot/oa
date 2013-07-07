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

class audio_ptt_gate(gr.basic_block):
    """
    docstring for block audio_ptt_gate
    """
    def __init__(self):
        gr.basic_block.__init__(self,
            name="audio_ptt_gate",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])
        
        self.message_port_register_in(pmt.pmt_intern('in2'))
        self.set_msg_handler(pmt.pmt_intern('in2'),self.handle_msg)
        
        self.ptt  = False

    def handle_msg(self, msg):
        #self.ptt = pmt.pmt_is_true(msg)
        print "XXXXXXXXXX"
        dict2 = pmt.to_python(msg)
        if ['button'][0] == 1:
            self.ptt = True
        else:
            self.ptt = False
        
    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        
        count = len(output_items[0])
        self.consume(0, len(out)) 
        
        if self.ptt:
            out[:] = in0
            #key = pmt.pmt_string_to_symbol("tx_sob")
            #self.add_item_tag(0, self.nitems_written(0), key, pmt.PMT_T, source)
            #key = pmt.pmt_string_to_symbol("tx_eob")
            #self.add_item_tag(0, self.nitems_written(0) + count - 1, key, pmt.PMT_T, source)
            return len(output_items[0])
        else:
            return 0

