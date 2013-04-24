#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Simple Message Passing Example
# Generated: Tue Apr 23 20:52:40 2013
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from grc_gnuradio import wxgui as grc_wxgui
from gruel import pmt
from optparse import OptionParser
import openavionics
import wx

class simple_message_passing_example(grc_wxgui.top_block_gui):

	def __init__(self, baudrate=19200, device="/dev/pts/3"):
		grc_wxgui.top_block_gui.__init__(self, title="Simple Message Passing Example")

		##################################################
		# Parameters
		##################################################
		self.baudrate = baudrate
		self.device = device

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 32000

		##################################################
		# Blocks
		##################################################
		self.openavionics_serial_io_0 = openavionics.serial_io(device,0,baudrate,0,1,False)
		self.blocks_message_strobe_0 = blocks.message_strobe(pmt.pmt_intern("TEST"), 1000)
		self.blocks_message_debug_0 = blocks.message_debug()

		##################################################
		# Asynch Message Connections
		##################################################
		self.msg_connect(self.blocks_message_strobe_0, "strobe", self.openavionics_serial_io_0, "in")
		self.msg_connect(self.openavionics_serial_io_0, "out", self.blocks_message_debug_0, "print")

	def get_baudrate(self):
		return self.baudrate

	def set_baudrate(self, baudrate):
		self.baudrate = baudrate

	def get_device(self):
		return self.device

	def set_device(self, device):
		self.device = device

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	parser.add_option("", "--baudrate", dest="baudrate", type="intx", default=19200,
		help="Set baudrate [default=%default]")
	parser.add_option("", "--device", dest="device", type="string", default="/dev/pts/3",
		help="Set device [default=%default]")
	(options, args) = parser.parse_args()
	tb = simple_message_passing_example(baudrate=options.baudrate, device=options.device)
	tb.Run(True)

