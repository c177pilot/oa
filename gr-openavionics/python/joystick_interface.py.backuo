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
import pygame
import sys



# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

# This is a simple class that will help us print to the screen
# It has nothing to do with the joysticks, just outputing the
# information.
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def prints(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
        
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
        
    def indent(self):
        self.x += 10
        
    def unindent(self):
        self.x -= 10

class joystick_interface(gr.sync_block):
    """
    docstring for block joystick_interface
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="joystick_interface",
            in_sig=None,
            out_sig=None)

        self.message_port_register_out(pmt.intern('out'))
        thread.start_new_thread( self.tx_work, (1, ))
        
    def tx_work(self,x):

        pipe = open('/dev/input/js0','r')
        action = []
        spacing = 0
        button = [None] * 4
        while 1:
            for character in pipe.read(1):
                action += ['%02X' % ord(character)]
                if len(action) == 8:

                    num = int(action[5], 16) # Translate back to integer form
                    percent254 = str(((float(num)-128.0)/126.0)-100)[4:6] # Calculate the percentage of push
                    percent128 = str((float(num)/127.0))[2:4]

                    if percent254 == '.0':
                        percent254 = '100'
                    if percent128 == '0':
                        percent128 = '100'

                    if action[6] == '01': # Button
                        if action[4] == '01':
                            print 'You pressed button: ' + action[7]
                            button[int(action[7])] = 1
                        else:
                            print 'You released button: ' + action[7]
                            button[int(action[7])] = 0
                            
                        dict2 = { "id" : "joystick",
                        "buttons" : button}
                
                        #pmt_dict = pmt.to_pmt(dict2)
                        self.message_port_pub(pmt.intern('out'),pmt.to_pmt(dict2))
                    
                    action = []
