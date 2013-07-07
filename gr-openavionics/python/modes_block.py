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

from gnuradio import gr,gru,eng_notation
import gnuradio.gr.gr_threading as _threading
import csv
from string import split, join
import air_modes
from air_modes.exceptions import *
try: import pmt
except: from gruel import pmt
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
        
        self.message_port_register_hier_out("out")
        #self.message_port_register_hier_out('out')

        self._queue = gr.msg_queue()

        self.rx_path = air_modes.rx_path(rate, threshold, self._queue)

        self.connect(self, self.rx_path)

        #self._sender = air_modes.zmq_pubsub_iface(context, subaddr=None, pubaddr="inproc://modes-radio-pub")
        self._queue_to_blob = _queue_to_blob(self._queue)
        #self._async_sender = gru.msgq_runner(self._queue, self.send)
                

        #self.msg_connect(self._queue_to_blob,"out",self,"out")


    def send(self, msg):
        #self._sender["dl_data"] = msg.to_string()
        raw_string = msg.to_string()
        dict2 = { "id" : "raw_mode_s",
                "raw_data" : raw_string}
        #pmt_dict = pmt.to_pmt(dict2)
        #self.message_port_pub(pmt.pmt_intern('out'),pmt.to_pmt(pmt_dict))

class _queue_to_blob(gr.basic_block):
    """
    Helper for the deframer, reads queue, unpacks packets, posts.
    It would be nicer if the framer_sink output'd messages.
    """
    def __init__(self, msgq):
        gr.basic_block.__init__(self,
            name="_queue_to_blob",
            in_sig=None,
            out_sig=None
        )
        self._msgq = msgq
        self.message_port_register_out(pmt.intern('out'))

        
    def work(self, input_items, output_items):
        while True:
            try: msg = self._msgq.delete_head()
            except: return -1
            print "msg_rx"

            msg = pmt.pmt_string_to_symbol(msg.to_string())
            self.message_port_pub(pmt.intern('out'),msg)
