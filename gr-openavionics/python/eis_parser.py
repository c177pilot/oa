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

SEARCHING_HEADER = 0 
HEADER_MSB_FOUND = 1
HEADER_LSB_FOUND = 2
ID_FOUND = 3
GET_DATA = 4
GET_CHECKSUM = 5

number_bytes_to_get = 0 

HEADER_MSB = 0xFE
HEADER_LSB = 0xFF

OUTPUT_SENTENCE_1_ID = 0xFE
OUTPUT_SENTENCE_2_ID = 0xFD
OUTPUT_SENTENCE_3_ID = 0xFC
OUTPUT_SENTENCE_4_ID = 0xFB
OUTPUT_SENTENCE_5_ID = 0xFA

sentence_size = [23,21,25,40,99]

class eis_parser(gr.basic_block):
    """
    docstring for block eis_parser
    """
    def __init__(self):
        gr.basic_block.__init__(self,
            name="eis_parser",
            in_sig=None,
            out_sig=None)
            
        self.state = SEARCHING_HEADER
        self.i = 0 
        self.bytes_got = 0
        self.running_checksum = 0
        self.buf = []
        self.i = 0 
        self.bytes_got = 0
        self.running_checksum = 0

        self.message_port_register_out(pmt.intern('out'))
        
        self.msg_list = []
        self.message_port_register_in(pmt.intern('in'))
        self.set_msg_handler(pmt.intern('in'),self.handle_msg)
        
    def process(self,buf):
        i = 0
        
        tach = buf[i] * 256 + buf[i+1]
        i+= 2
        
        cht = [0,0,0,0,0,0]
        j = 0 
        while j < 6:
             cht[j] = buf[i] * 256 + buf[i+1]
             j += 1
             i += 2
        
        egt = [0,0,0,0,0,0]
        j = 0 
        while j < 6:
             egt[j] = buf[i] * 256 + buf[i+1]
             j += 1
             i += 2        
        
        #aux5, fill in array later
        aux5 = buf[i] * 256 + buf[i + 1]
        i += 2
        
        #aux6, fill in array later
        aux6 = buf[i] * 256 + buf[i + 1]
        i += 2
        
        #airspeed, units match whatever efis is set to
        airspeed = buf[i] * 256 + buf[i + 1]
        i += 2
            
        #alt in ft
        altitude = buf[i] * 256 + buf[i + 1]
        i += 2      

        #bat voltage?
        volt  = buf[i] * 256 + buf[i + 1] * 0.1
        i += 2
        
        #fuel_flow (gallons/hour)
        fuel_flow = buf[i] * 256 + buf[i + 1] * 0.1
        i += 2        
        
        #eis internal temp
        unit_temp = buf[i]
        i += 1
        
        #carb what?
        carb = buf[i]
        i += 1    
        
        #vertical speed
        climb_rate = buf[i] * 100
        i += 1
        
        #outside air temp
        oat = buf[i] - 50 
        i += 1        
        
        #oil temp
        oil_temp = buf[i] * 256 + buf[i + 1] * 0.1
        i += 2
        
        #oil press
        oil_press = buf[i]
        i += 1

        #aux1-4 and align aux5,6
        aux = [0,0,0,0,0,0]
        j = 0 
        while j < 4:
             aux[j] = buf[i] * 256 + buf[i+1]
             j += 1
             i += 2
        aux[4] = aux5
        aux[5] = aux6

        #coolant temp
        coolant_temp = buf[i] * 256 + buf[i + 1]
        i += 2
        
        #hour meter
        hour_meter = buf[i] * 256 + buf[i + 1] * 0.1
        i += 2

        #fuel qty
        fuel_quantity = buf[i] * 256 + buf[i + 1] * 0.1
        i += 2
        
        #flight time
        flight_time_secs = buf[i] * 60 * 60 + buf[i+1] * 60 + buf[i+2]
        i += 3
        
        #time until fuel empty
        time_remaining_fuel_min = buf[i] * 60 + buf[i + 1]
        i += 2
        
        #barometric setting in HG
        alt_setting  = buf[i] * 256 + buf[i + 1] * 0.01
        i += 2

        #engine #2 tach
        tach2 = buf[i] * 256 + buf[i + 1] * 0.1
        i += 2
        
        #spare
        spare = buf[i]


        dict2 = { "tach1" : tach,
        "tach2" : tach2,
        "cht" : cht,
        "egt" : egt,
        "aux" : aux,
        "airspeed" : airspeed,
        "altitude" : altitude,
        "fuel_flow" : fuel_flow,
        "eis_temp" : unit_temp,
        "carb" : carb,
        "oat" : oat,
        "oil_temp" : oil_temp,
        "coolant_temp" : coolant_temp,
        "hours_of_operation" : hour_meter,
        "fuel_qty" : fuel_quantity,
        "flight_time_in_seconds" : flight_time_secs,
        "minutes_fuel_remaining" : time_remaining_fuel_min,
        "alt_setting" : alt_setting}
        
        pmt_dict = pmt.to_pmt(dict2)
        self.message_port_pub(pmt.intern('out'),pmt.to_pmt(pmt_dict))
        #dict_out = pmt.to_python(pmt_dict)
        
        #print dict_out


    def handle_msg(self, msg):
        tx_string = pmt.symbol_to_string(msg)
        a =  map(ord,tx_string)
        iterations = len(a)           
        i = 0
             
        while i < iterations:  
            char = a[i]
            if self.state == SEARCHING_HEADER:
                self.bytes_got = 0
                if char == HEADER_MSB:
                    self.state = HEADER_MSB_FOUND
            elif self.state == HEADER_MSB_FOUND:
                if char == HEADER_LSB:
                    self.state = HEADER_LSB_FOUND
                else:
                    self.state == SEARCHING_HEADER
            elif self.state == HEADER_LSB_FOUND:
                if char == 0xFE:
                    self.num_of_bytes_to_get = 73
                    #self.running_checksum = (self.running_checksum + char )
                    self.state = GET_DATA
                else: 
                    self.state = SEARCHING_HEADER
            elif self.state == GET_DATA:
                self.buf.append(char)
                self.running_checksum = (self.running_checksum + char)
                self.bytes_got += 1
                if self.bytes_got == self.num_of_bytes_to_get - 4:
                    self.state = GET_CHECKSUM
            elif self.state == GET_CHECKSUM:
                #print char, 256 - abs(~(self.running_checksum % 256))
                if char == 256 - abs(~(self.running_checksum % 256)):
                    #print "Good checksum"
                    self.process(self.buf)
                #else:
                #    print "Bad checksum"
                self.buf = []
                self.running_checksum = 0
                self.state = SEARCHING_HEADER
                
            i += 1
            
