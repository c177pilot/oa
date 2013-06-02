#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Joystick 101
# Generated: Sun Jun  2 11:11:13 2013
##################################################

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import scopesink2
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
		self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
			self.GetWin(),
			title="Scope Plot",
			sample_rate=samp_rate,
			v_scale=0,
			v_offset=0,
			t_scale=0,
			ac_couple=False,
			xy_mode=False,
			num_inputs=1,
			trig_mode=gr.gr_TRIG_MODE_AUTO,
			y_axis_label="Counts",
		)
		self.Add(self.wxgui_scopesink2_0.win)
		self.openavionics_joystick_interface_0 = openavionics.joystick_interface()
		self.openavionics_audio_ptt_0 = openavionics.audio_ptt()
		self.blocks_tag_debug_0 = blocks.tag_debug(gr.sizeof_float*1, "")
		self.audio_sink_0 = audio.sink(48000, "", True)
		self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 1000, 0.2, 0)

		##################################################
		# Connections
		##################################################
		self.connect((self.openavionics_audio_ptt_0, 0), (self.blocks_tag_debug_0, 0))
		self.connect((self.openavionics_audio_ptt_0, 0), (self.wxgui_scopesink2_0, 0))
		self.connect((self.openavionics_audio_ptt_0, 0), (self.audio_sink_0, 0))
		self.connect((self.analog_sig_source_x_0, 0), (self.openavionics_audio_ptt_0, 0))

		##################################################
		# Asynch Message Connections
		##################################################
		self.msg_connect(self.openavionics_joystick_interface_0, "out", self.openavionics_audio_ptt_0, "in2")

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
		self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = joystick_101()
	tb.Run(True)

