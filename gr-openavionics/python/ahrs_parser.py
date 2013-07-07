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

HEADER_MSB = 0x7F
HEADER_LSB = 0xFF

OUTPUT_SENTENCE_1_ID = 0xFE
OUTPUT_SENTENCE_2_ID = 0xFD
OUTPUT_SENTENCE_3_ID = 0xFC
OUTPUT_SENTENCE_4_ID = 0xFB
OUTPUT_SENTENCE_5_ID = 0xFA

sentence_size = [23,21,25,40,99]

class ahrs_parser(gr.basic_block):
    """
    docstring for block ahrs_parser
    """
    def __init__(self):
        gr.basic_block.__init__(self,
            name="ahrs_parser",
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
        self.set_msg_handler(pmt.intern('in'),
                             self.handle_msg)
        
    def if_negative(self,char):
        if ( ( char >> 7 ) & 1 ) == 1:
            return True
        else:
            return False
        
    def process_sentence_1(self,buf):
        
        char = buf[0]
        if not char == 4:
            print char
        align_mode_in_progress = char & 1
        air_align =  ( char >> 1 ) & 1
        mx_sentence_active = ( char >> 2) & 1
        factory_cal_in_progress = ( char >> 3 ) & 1
        gyro_bias_averaged = ( char >> 4 ) & 1
        fine_mag_cal_in_progress = ( char >> 5 ) & 1
        ahrs_invalid = ( char >> 6 ) & 1
         
        #calc roll angle
        msb = buf[1]
        lsb = buf[2]
        value = msb * 256 + lsb
        if value < 0x8000:
            value = value / 32768.0 * 180.0
        else:
            value = value - 0x8000
            value = -( value / 32768.0 * -180.0 + 180.0 )
        roll = value
        #print msb,lsb,value
        

        
        #calc pitch angle
        msb = buf[3]
        lsb = buf[4]
        value = msb * 256 + lsb
        #print msb,lsb
        if value < 0x8000:
            value = value / 32768.0 * 180.0
        else:
            value = value - 0x8000
            value = -( value / 32768.0 * -180.0 + 180.0 )
        pitch = value
        #print msb,lsb,value
        
        #calc yaw angle 
        msb = buf[5]
        lsb = buf[6]
        value = msb * 256 + lsb
        if value < 0x8000:
            value = value / 32768.0 * 180.0
        else:
            value = value - 0x8000
            value = -( value / 32768.0 * -180.0 + 180.0)
        #print msb,lsb,value    
        yaw = value    
        
        #calc altitude
        msb = buf[7]
        lsb = buf[8]
        value = msb * 256 + lsb
        if value == 0:
            data_invalid = 1
        else:
            data_invalid = 0
            value = value - 5000.0
        #print msb,lsb,value
        altitude = value

        #calc altitude rate
        msb = buf[9]
        lsb = buf[10]
        value = msb * 256 + lsb
        if value < 0x8000:
            value = value * 1.0
        else:
            value = value - 0x8000
            value = value * -1.0
        vertical_speed = value
        #print msb,lsb,value    
           
   
           
        #calc indicated airspeed
        msb = buf[11]
        lsb = buf[12]
        value = msb * 256 + lsb
        if value < 0x8000:
            value = value * 1.0
        else:
            value = value - 0x8000
            value = value * -1.0
        value = value / 10 * .592483 # conversion from .1 ft/s units to kts
        airspeed = value
        if (airspeed < 35):
            dont_use_airspeed = True
        else:
            dont_use_airspeed = False

        #print msb,lsb,value 
        

                    
                    
        #calc ias rate
        msb = buf[13]
        lsb = buf[14]
        value = msb * 256 + lsb
        if value < 0x8000:
            value = value * 1.0
        else:
            value = value - 0x8000
            value = value * -1.0
        value = value / 10 * .592483 # conversion from .1 ft/s units to kts
        airspeed_rate = value
        #print msb,lsb,value 
        
        #calc accel roll angle
        msb = buf[15]
        lsb = buf[16]
        value = msb * 256 + lsb
        #print msb,lsb
        if value < 0x8000:
            value = value / 32768.0 * 180.0
        else:
            value = value - 0x8000
            value = value / 32768.0 * -180.0
        accel_roll = value
        #print value
        
        
        #calc normal accel
        msb = buf[17]
        lsb = buf[18]
        value = msb * 256 + lsb
        if value < 0x8000:
            value = value  * 0.001
        else:
            value = value - 0x8000
            value = value * -0.001
        normal_accel = value
        #print msb,lsb,value 
        #print value    

        #dict1 = pmt.pmt_make_dict()

        dict2 = { "align_mode_in_progress" : align_mode_in_progress,
        "air_align" : air_align,
        "max_sentence_active" : mx_sentence_active,
        "factory_cal_in_progress" : factory_cal_in_progress,
        "gyro_bias_averaged" : gyro_bias_averaged,
        "fine_mag_cal_in_progress" : fine_mag_cal_in_progress,
        "ahrs_invalid" : ahrs_invalid,
        "roll" : roll,
        "pitch" : pitch,
        "yaw" : yaw,
        "altitude" : altitude,
        "vertical_speed" : vertical_speed,
        "airspeed" : airspeed,
        "dont_use_airspeed" : dont_use_airspeed,
        "airspeed_rate" : airspeed_rate,
        "accel_roll_angle" : accel_roll,
        "accel" : normal_accel }
        
        
        pmt_dict = pmt.to_pmt(dict2)
        self.message_port_pub(pmt.intern('out'),pmt.to_pmt(pmt_dict))
        #dict_out = pmt.to_python(pmt_dict)
        #print dict_out

    def process_sentence_2(self,buf):
        
        #calculate oat
        msb = buf[0]
        value = msb
        if value >= 0x80:
            value = value - 0x80
        value = value * 1.0
        #print msb, value
        
        #calc voltage 1
        msb = buf[1]
        lsb = buf[2]
        value = msb * 256 + lsb
        if value < 0x8000:
            value = value  * 0.01
        else:
            value = value - 0x8000
            value = value * -0.01
        voltage1 = value
        #print msb,lsb,value 
        #print value    

        #calc voltage 2
        msb = buf[3]
        lsb = buf[4]
        value = msb * 256 + lsb
        if value < 0x8000:
            value = value  * 0.01
        else:
            value = value - 0x8000
            value = value * -0.01
        voltage2 = value
        #print msb,lsb,value 
        #print value
        
        #calc voltage 3
        msb = buf[5]
        lsb = buf[6]
        value = msb * 256 + lsb
        if value < 0x8000:
            value = value  * 0.01
        else:
            value = value - 0x8000
            value = value * -0.01
        voltage3 = value
        #print msb,lsb,value 
        #print value
        
        #status_word_1
        msb = buf[7]
        coarse_mag_invalid = msb & 1
        fine_mag_invalid = ( msb >> 1 ) & 1
        cal_fialed_heading = ( msb >> 2 ) & 1
        mag_fail = ( msb >> 3 ) & 1
        voltage_fail = ( msb >> 4 ) & 1
        gyro_max_rate = ( msb >> 5 ) & 1
        roll_max_rate = ( msb >> 6 ) & 1
        yaw_max_rate = ( msb >> 7 ) & 1
        
        #status_word_2
        msb = buf[8]
        movement_during_alignment = msb & 1
        mag_x_fail = ( msb >> 1 ) & 1
        mag_y_fail = ( msb >> 2 ) & 1
        mag_z_fail = ( msb >> 3 ) & 1
        gyro_x_fail = ( msb >> 4 ) & 1
        gyrp_y_fail = ( msb >> 5 ) & 1
        gyro_z_fail = ( msb >> 6 ) & 1
        
        #status_word_3
        msb = buf[9]
        acc_x_fail = msb & 1
        acc_y_fail = ( msb >> 1 ) & 1
        acc_z_fail = ( msb >> 2 ) & 1
        altimeter_fail = ( msb >> 3 ) & 1
        airspeed_fail = ( msb >> 4 ) & 1
        internal_temp_fail= ( msb >> 5 ) & 1   
        
        #internal temp
        msb = buf[10]
        value = msb
        if value >= 0x80:
            value = value - 0x80
        value = value * 1.0
        internal_temp = value
        #print msb, value
        
        #version
        msb = buf[11]
        lsb = buf[12]
        software = "%d,%d" % (msb,lsb)
        #print msb,lsb,software
        

        
    def process(self,buf,sentence_id):
            
        if sentence_id == 1:
            self.process_sentence_1(buf)
        elif sentence_id == 2:
            self.process_sentence_2(buf)
        elif sentence_id == 3:
            o = 2
        elif sentence_id == 4:
            o = 2
        elif sentence_id == 5:
            o = 3
            
        
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
                if char <= 0xFE and char > 0xFA: #ignore eeprom msgs for now
                    self.sentence = abs(char - 0xFA - 5) 
                    self.num_of_bytes_to_get = sentence_size[self.sentence - 1]
                    #print self.num_of_bytes_to_get
                    self.running_checksum = (self.running_checksum + char )
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
                    #print "Good checksum", self.sentence
                    self.process(self.buf,self.sentence)

                self.buf = []
                self.running_checksum = 0
                self.state = SEARCHING_HEADER
                
            i += 1
            

