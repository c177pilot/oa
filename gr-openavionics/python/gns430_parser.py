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

class gns430_parser(gr.sync_block):
    """
    docstring for block gns430_parser
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="gns430_parser",
            in_sig=None,
            out_sig=None)
            
        self.count = 0
        self.message_port_register_out(pmt.pmt_intern('out'))
        self.buf = ''
        self.message_port_register_in(pmt.pmt_intern('in'))
        self.set_msg_handler(pmt.pmt_intern('in'),self.handle_msg)
        
        self.dict2 = {}
        
        self.lat = 0
        self.lon = 0
        self.alt = 0
        self.nav_status = ''
        self.track = 0
        self.track_error = 0
        self.ground_speed = 0
        self.distance_to_wpt = 0
        self.bearing_to_wpt = 0
        self.destination_id = ''
        self.desired_track = 0
        
    def process(self,buf):
        
        #print buf
        
        if(buf[0] == 'A'):
            if(buf[1] == 'N'):
                sign = 1
            else:
                sign = -1
            values = buf.split(' ')
            self.lat = sign * ( float(values[1]) + ( float(values[2])/100 )/60.0 )#check format
        elif(buf[0] == 'B'):
            if(buf[1] == 'E'):
                sign = 1
            else:
                sign = -1
            values = buf.split(' ')
            self.lon = sign * ( float(values[1]) + ( float(values[2])/100 )/60.0  )#check format
        elif(buf[0] == 'z'):
            print 'got here',buf
            time.sleep(100)
            values = buf[1:]
            self.alt = float(values)
        elif(buf[0] == 'C'):
            values = buf[1:]
            self.track = float(values)
        elif(buf[0] == 'D'):
            values = buf[1:]
            self.ground_speed = float(values) 
        elif(buf[0] == 'E'):
            values = buf[1:]
            self.distance_to_wpt= float(values) * .1
        elif(buf[0] == 'I'):
            values = buf[1:]
            self.desired_track= float(values)*.1
        elif(buf[0] == 'K'):
            values = buf[1:]
            self.destination_id = values 
        elif(buf[0] == 'L'):
            values = buf[1:]
            self.bearing_to_wpt = float(values)*.1
        elif(buf[0] == 'l'):
            values = buf[1:]
            self.distance_to_wpt = float(values)*.1
        elif(buf[0] == 'S'):
            values = buf[1:]
            self.nav_status = values
        elif(buf[0] == 'G'):
            values = buf[2:]
            if(buf[1] == 'L'):
                sign = -1
            else:
                sign = 1
            self.track_error = float(values)*.01
        elif(buf[0] == 'T'):
            self.dict2 = { "lat" : self.lat,
             "lon" : self.lon,
             "alt" : self.alt,
             "track" : self.track,
             "ground_speed" : self.ground_speed,
             "distance_to_wpt" : self.distance_to_wpt,
             "desired_track" : self.desired_track,
             "destination_id" : self.destination_id,
             "bearing_to_wpt" : self.bearing_to_wpt,
             "nav_status" : self.nav_status,
             "track_error" : self.track_error
            }
            #print self.dict2
            pmt_dict = pmt.to_pmt(self.dict2)
            self.message_port_pub(pmt.pmt_intern('out'),pmt.to_pmt(pmt_dict))
        
 
    def handle_msg(self, msg):
        tx_string = pmt.pmt_symbol_to_string(msg)
        
        for i in range(len(tx_string)):
            if tx_string[i] == '\n':
                #print len(self.buf)
                #time.sleep(1)
                #self.buf = self.buf + (tx_string[i])
                self.process(self.buf)
                self.buf =''
                self.count += 1
            else:
                self.buf = self.buf + (tx_string[i])
        
        

