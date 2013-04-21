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
from math import pi
import serial
import thread
import time
import socket


class gns430_to_fg(gr.sync_block):
    """
    docstring for block gns430_to_fg
    """
    def __init__(self,ip_addr,port):
        gr.sync_block.__init__(self,
            name="gns430_to_fg",
            in_sig=None,
            out_sig=None)
            
        self.message_port_register_in(pmt.pmt_intern('in'))
        self.set_msg_handler(pmt.pmt_intern('in'),self.handle_msg)
        
        #open udp port
        try:            
            self.ip_addr = ip_addr
            self.port = port
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        except:
            print 'could not open port'

        
    def handle_msg(self, msg):
        received = pmt.to_python(msg)
        lat = received['lat']
        lon = received['lon']
        ground_speed = received['ground_speed']
        outgoing = "%f:%f:%f\n\r" % (lat,lon,ground_speed)
        #print outgoing
        self.sock.sendto(outgoing, (self.ip_addr, self.port))

