#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: VOR Receiver
# Generated: Sat Jul 13 13:30:58 2013
##################################################

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import numbersink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import math
import wx

class vor2(grc_wxgui.top_block_gui):

	def __init__(self, fm_subcarrier=9960, zero_point=-5):
		grc_wxgui.top_block_gui.__init__(self, title="VOR Receiver")

		##################################################
		# Parameters
		##################################################
		self.fm_subcarrier = fm_subcarrier
		self.zero_point = zero_point

		##################################################
		# Variables
		##################################################
		self.rf_rate = rf_rate = 1000000
		self.dir_rate = dir_rate = 10
		self.channel_rate = channel_rate = 40000
		self.audio_rate = audio_rate = 10000
		self.vor_freq = vor_freq = 113.9e6
		self.volume = volume = 0
		self.rf_scale = rf_scale = int(rf_rate/channel_rate) + rf_rate % channel_rate
		self.offset = offset = fm_subcarrier + 4000
		self.dir_scale = dir_scale = int(audio_rate/dir_rate) + audio_rate % dir_rate
		self.channel = channel = 113.9e6
		self.audio_scale = audio_scale = int(channel_rate/audio_rate) + channel_rate % audio_rate

		##################################################
		# Blocks
		##################################################
		_volume_sizer = wx.BoxSizer(wx.VERTICAL)
		self._volume_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_volume_sizer,
			value=self.volume,
			callback=self.set_volume,
			label='volume',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._volume_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_volume_sizer,
			value=self.volume,
			callback=self.set_volume,
			minimum=-10,
			maximum=10,
			num_steps=1000,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_volume_sizer)
		self._channel_text_box = forms.text_box(
			parent=self.GetWin(),
			value=self.channel,
			callback=self.set_channel,
			label="Channel (Hz)",
			converter=forms.float_converter(),
		)
		self.Add(self._channel_text_box)
		self.zeroer = blocks.add_const_vff((zero_point*(math.pi/180), ))
		self.wxgui_numbersink2_0 = numbersink2.number_sink_f(
			self.GetWin(),
			unit="deg",
			minval=-180,
			maxval=180,
			factor=180/math.acos(-1),
			decimal_places=2,
			ref_level=0,
			sample_rate=dir_rate,
			number_rate=dir_rate,
			average=True,
			avg_alpha=.25,
			label="Direction",
			peak_hold=False,
			show_gauge=True,
		)
		self.Add(self.wxgui_numbersink2_0.win)
		self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
			self.GetWin(),
			baseband_freq=channel,
			y_per_div=10,
			y_divs=10,
			ref_level=0,
			ref_scale=2.0,
			sample_rate=channel_rate,
			fft_size=1024,
			fft_rate=15,
			average=True,
			avg_alpha=0.25,
			title="Channel",
			peak_hold=False,
		)
		self.Add(self.wxgui_fftsink2_0.win)
		self._vor_freq_text_box = forms.text_box(
			parent=self.GetWin(),
			value=self.vor_freq,
			callback=self.set_vor_freq,
			label='vor_freq',
			converter=forms.float_converter(),
		)
		self.Add(self._vor_freq_text_box)
		self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
		        interpolation=40,
		        decimation=1,
		        taps=None,
		        fractional_bw=None,
		)
		self.low_pass_filter_1 = filter.fir_filter_ccf(1, firdes.low_pass(
			1, dir_rate, 1, 2, firdes.WIN_HAMMING, 6.76))
		self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
			1, channel_rate, 10000, 4000, firdes.WIN_HAMMING, 6.76))
		self.goertzel_fc_0_0 = fft.goertzel_fc(channel_rate, dir_scale*audio_scale, 30)
		self.goertzel_fc_0 = fft.goertzel_fc(audio_rate, dir_scale, 30)
		self.freq_xlating_fir_filter_xxx_0_0 = filter.freq_xlating_fir_filter_ccc(1, (firdes.low_pass(1.0, channel_rate, 500, 100, firdes.WIN_HAMMING)), fm_subcarrier, channel_rate)
		self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(rf_scale, (firdes.low_pass(1.0, rf_rate, channel_rate, channel_rate/2, firdes.WIN_HAMMING)), 900, rf_rate)
		self.dc_blocker_xx_0 = filter.dc_blocker_ff(128, True)
		self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, 1e6)
		self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((10**(volume/10), ))
		self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(1)
		self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/john/apps/aviation_rx/woodside_vor25.dat", True)
		self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, int(channel_rate/30*0.0))
		self.blocks_complex_to_arg_0 = blocks.complex_to_arg(1)
		self.audio_sink_0 = audio.sink(audio_rate, "", True)
		self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(1)
		self.analog_am_demod_cf_0 = analog.am_demod_cf(
			channel_rate=40e3,
			audio_decim=4,
			audio_pass=5000,
			audio_stop=5500,
		)
		self.analog_agc2_xx_1 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
		self.analog_agc2_xx_1.set_max_gain(65536)
		self.analog_agc2_xx_0_1_0 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
		self.analog_agc2_xx_0_1_0.set_max_gain(100)
		self.analog_agc2_xx_0_1 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
		self.analog_agc2_xx_0_1.set_max_gain(100)

		##################################################
		# Connections
		##################################################
		self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.wxgui_fftsink2_0, 0))
		self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.low_pass_filter_0, 0))
		self.connect((self.freq_xlating_fir_filter_xxx_0_0, 0), (self.analog_quadrature_demod_cf_0, 0))
		self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.blocks_delay_0, 0))
		self.connect((self.analog_quadrature_demod_cf_0, 0), (self.goertzel_fc_0_0, 0))
		self.connect((self.goertzel_fc_0, 0), (self.analog_agc2_xx_0_1, 0))
		self.connect((self.goertzel_fc_0_0, 0), (self.analog_agc2_xx_0_1_0, 0))
		self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
		self.connect((self.dc_blocker_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
		self.connect((self.blocks_delay_0, 0), (self.freq_xlating_fir_filter_xxx_0_0, 0))
		self.connect((self.blocks_complex_to_arg_0, 0), (self.zeroer, 0))
		self.connect((self.zeroer, 0), (self.wxgui_numbersink2_0, 0))
		self.connect((self.low_pass_filter_1, 0), (self.blocks_complex_to_arg_0, 0))
		self.connect((self.analog_agc2_xx_0_1, 0), (self.blocks_multiply_conjugate_cc_0, 0))
		self.connect((self.analog_agc2_xx_0_1_0, 0), (self.blocks_multiply_conjugate_cc_0, 1))
		self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.low_pass_filter_1, 0))
		self.connect((self.low_pass_filter_0, 0), (self.analog_am_demod_cf_0, 0))
		self.connect((self.analog_am_demod_cf_0, 0), (self.goertzel_fc_0, 0))
		self.connect((self.analog_am_demod_cf_0, 0), (self.dc_blocker_xx_0, 0))
		self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_throttle_0, 0))
		self.connect((self.blocks_file_source_0, 0), (self.rational_resampler_xxx_0, 0))
		self.connect((self.blocks_throttle_0, 0), (self.analog_agc2_xx_1, 0))
		self.connect((self.analog_agc2_xx_1, 0), (self.freq_xlating_fir_filter_xxx_0, 0))


# QT sink close method reimplementation

	def get_fm_subcarrier(self):
		return self.fm_subcarrier

	def set_fm_subcarrier(self, fm_subcarrier):
		self.fm_subcarrier = fm_subcarrier
		self.freq_xlating_fir_filter_xxx_0_0.set_center_freq(self.fm_subcarrier)
		self.set_offset(self.fm_subcarrier + 4000)

	def get_zero_point(self):
		return self.zero_point

	def set_zero_point(self, zero_point):
		self.zero_point = zero_point
		self.zeroer.set_k((self.zero_point*(math.pi/180), ))

	def get_rf_rate(self):
		return self.rf_rate

	def set_rf_rate(self, rf_rate):
		self.rf_rate = rf_rate
		self.set_rf_scale(int(self.rf_rate/self.channel_rate) + self.rf_rate % self.channel_rate)
		self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.low_pass(1.0, self.rf_rate, self.channel_rate, self.channel_rate/2, firdes.WIN_HAMMING)))

	def get_dir_rate(self):
		return self.dir_rate

	def set_dir_rate(self, dir_rate):
		self.dir_rate = dir_rate
		self.set_dir_scale(int(self.audio_rate/self.dir_rate) + self.audio_rate % self.dir_rate)
		self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.dir_rate, 1, 2, firdes.WIN_HAMMING, 6.76))

	def get_channel_rate(self):
		return self.channel_rate

	def set_channel_rate(self, channel_rate):
		self.channel_rate = channel_rate
		self.goertzel_fc_0_0.set_rate(self.channel_rate)
		self.freq_xlating_fir_filter_xxx_0_0.set_taps((firdes.low_pass(1.0, self.channel_rate, 500, 100, firdes.WIN_HAMMING)))
		self.blocks_delay_0.set_dly(int(self.channel_rate/30*0.0))
		self.set_rf_scale(int(self.rf_rate/self.channel_rate) + self.rf_rate % self.channel_rate)
		self.set_audio_scale(int(self.channel_rate/self.audio_rate) + self.channel_rate % self.audio_rate)
		self.wxgui_fftsink2_0.set_sample_rate(self.channel_rate)
		self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.channel_rate, 10000, 4000, firdes.WIN_HAMMING, 6.76))
		self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.low_pass(1.0, self.rf_rate, self.channel_rate, self.channel_rate/2, firdes.WIN_HAMMING)))

	def get_audio_rate(self):
		return self.audio_rate

	def set_audio_rate(self, audio_rate):
		self.audio_rate = audio_rate
		self.set_dir_scale(int(self.audio_rate/self.dir_rate) + self.audio_rate % self.dir_rate)
		self.set_audio_scale(int(self.channel_rate/self.audio_rate) + self.channel_rate % self.audio_rate)
		self.goertzel_fc_0.set_rate(self.audio_rate)

	def get_vor_freq(self):
		return self.vor_freq

	def set_vor_freq(self, vor_freq):
		self.vor_freq = vor_freq
		self._vor_freq_text_box.set_value(self.vor_freq)

	def get_volume(self):
		return self.volume

	def set_volume(self, volume):
		self.volume = volume
		self._volume_slider.set_value(self.volume)
		self._volume_text_box.set_value(self.volume)
		self.blocks_multiply_const_vxx_0.set_k((10**(self.volume/10), ))

	def get_rf_scale(self):
		return self.rf_scale

	def set_rf_scale(self, rf_scale):
		self.rf_scale = rf_scale

	def get_offset(self):
		return self.offset

	def set_offset(self, offset):
		self.offset = offset

	def get_dir_scale(self):
		return self.dir_scale

	def set_dir_scale(self, dir_scale):
		self.dir_scale = dir_scale

	def get_channel(self):
		return self.channel

	def set_channel(self, channel):
		self.channel = channel
		self._channel_text_box.set_value(self.channel)
		self.wxgui_fftsink2_0.set_baseband_freq(self.channel)

	def get_audio_scale(self):
		return self.audio_scale

	def set_audio_scale(self, audio_scale):
		self.audio_scale = audio_scale

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = vor2()
	tb.Start(True)
        tb.Wait()

