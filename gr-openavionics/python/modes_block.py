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

from gnuradio import gr
from gnuradio import gru, optfir, eng_notation, blks2
import gnuradio.gr.gr_threading as _threading
import csv
from string import split, join
import air_modes
import csv
from air_modes.exceptions import *
#import zmq

class modes_block(gr.hier_block2):
    """
    docstring for block modes_block
    """
    def __init__(self,rate,threshold):
        gr.hier_block2.__init__(self,
            "modes_block",
            gr.io_signature(1,1, gr.sizeof_gr_complex),  # Input signature
            gr.io_signature(0,0,0)) # Output signature

        self._queue = gr.msg_queue()

        self.rx_path = air_modes.rx_path(rate, threshold, self._queue)

        self.connect(self, self.rx_path)

        #self._sender = air_modes.zmq_pubsub_iface(context, subaddr=None, pubaddr="inproc://modes-radio-pub")
        self._async_sender = gru.msgq_runner(self._queue, self.send)

    def send(self, msg):
        #self._sender["dl_data"] = msg.to_string()
        print msg.to_string()
            
        
