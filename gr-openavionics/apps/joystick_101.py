#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Joystick 101
# Generated: Mon Jun 24 20:27:59 2013
##################################################

from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import openavionics
import wx

class joystick_101(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Joystick 101")

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 48000

		##################################################
		# Blocks
		##################################################
		self.openavionics_joystick_interface_0 = openavionics.joystick_interface()
		self.openavionics_audio_ptt_0 = openavionics.audio_ptt()
		self.blocks_tag_debug_0 = blocks.tag_debug(gr.sizeof_float*1, "")
		self.blocks_message_debug_0 = blocks.message_debug()
		self.audio_source_0 = audio.source(samp_rate, "", True)

		##################################################
		# Connections
		##################################################
		self.connect((self.openavionics_audio_ptt_0, 0), (self.blocks_tag_debug_0, 0))
		self.connect((self.audio_source_0, 0), (self.openavionics_audio_ptt_0, 0))

		##################################################
		# Asynch Message Connections
		##################################################
		self.msg_connect(self.openavionics_joystick_interface_0, "out", self.openavionics_audio_ptt_0, "in2")
		self.msg_connect(self.openavionics_joystick_interface_0, "out", self.blocks_message_debug_0, "print")

# QT sink close method reimplementation

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = joystick_101()
	tb.Start(True)
        tb.Wait()

