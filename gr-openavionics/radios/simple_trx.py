#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Simple Trx
# Generated: Sun Jun  2 12:24:48 2013
##################################################

execfile("/home/john/.grc_gnuradio/fft_tone_to_angle.py")
from gnuradio import analog
from gnuradio import audio
from gnuradio import blks2
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import uhd
from gnuradio import window
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.gr import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import numbersink2
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import openavionics
import wx

class simple_trx(grc_wxgui.top_block_gui):

	def __init__(self, antenna="TX/RX", rx_gain=30, vor_samp_rate=250e3, com_freq_1=135.275e6, gain=21, vor_freq_1=115e6):
		grc_wxgui.top_block_gui.__init__(self, title="Simple Trx")

		##################################################
		# Parameters
		##################################################
		self.antenna = antenna
		self.rx_gain = rx_gain
		self.vor_samp_rate = vor_samp_rate
		self.com_freq_1 = com_freq_1
		self.gain = gain
		self.vor_freq_1 = vor_freq_1

		##################################################
		# Variables
		##################################################
		self.obs_decimation = obs_decimation = 25
		self.ils_decimation = ils_decimation = 50
		self.am_sample_rate = am_sample_rate = 12.5e3
		self.vor_volume_slider = vor_volume_slider = 5
		self.vor_ident = vor_ident = False
		self.vor_freq_entry_1 = vor_freq_entry_1 = vor_freq_1
		self.vor_center_freq_0 = vor_center_freq_0 = (117.95e6-108.00e6)/2+117.95e6
		self.system_center_freq = system_center_freq = 133.9e6
		self.squelch_slider = squelch_slider = -85
		self.samp_rate = samp_rate = 250e3
		self.rxgain = rxgain = 15
		self.phase_correction = phase_correction = 5
		self.obs_sample_rate = obs_sample_rate = am_sample_rate/obs_decimation
		self.ils_sample_rate = ils_sample_rate = am_sample_rate/ils_decimation
		self.gain_slider = gain_slider = gain
		self.correction_gain = correction_gain = 0.8
		self.com_volume_slider = com_volume_slider = 1
		self.com_freq_entry_1 = com_freq_entry_1 = com_freq_1
		self.com_enable = com_enable = True
		self.audio_select = audio_select = 0
		self.audio_sample_rate = audio_sample_rate = 48e3
		self.am_decimation = am_decimation = 1

		##################################################
		# Blocks
		##################################################
		_vor_volume_slider_sizer = wx.BoxSizer(wx.VERTICAL)
		self._vor_volume_slider_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_vor_volume_slider_sizer,
			value=self.vor_volume_slider,
			callback=self.set_vor_volume_slider,
			label='vor_volume_slider',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._vor_volume_slider_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_vor_volume_slider_sizer,
			value=self.vor_volume_slider,
			callback=self.set_vor_volume_slider,
			minimum=0,
			maximum=10,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.GridAdd(_vor_volume_slider_sizer, 1, 4, 1, 1)
		self._vor_ident_check_box = forms.check_box(
			parent=self.GetWin(),
			value=self.vor_ident,
			callback=self.set_vor_ident,
			label='vor_ident',
			true=1,
			false=0,
		)
		self.GridAdd(self._vor_ident_check_box, 0, 3, 1, 1)
		self._vor_freq_entry_1_text_box = forms.text_box(
			parent=self.GetWin(),
			value=self.vor_freq_entry_1,
			callback=self.set_vor_freq_entry_1,
			label='vor_freq_entry_1',
			converter=forms.float_converter(),
		)
		self.GridAdd(self._vor_freq_entry_1_text_box, 0, 1, 1, 1)
		self.notebook_0 = self.notebook_0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
		self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "RF Analyzer")
		self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Channel FFT")
		self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Demod Audio FFT")
		self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Ref and Phase Scope")
		self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Manipulated Ref and Phase")
		self.Add(self.notebook_0)
		_com_volume_slider_sizer = wx.BoxSizer(wx.VERTICAL)
		self._com_volume_slider_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_com_volume_slider_sizer,
			value=self.com_volume_slider,
			callback=self.set_com_volume_slider,
			label='com_volume_slider',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._com_volume_slider_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_com_volume_slider_sizer,
			value=self.com_volume_slider,
			callback=self.set_com_volume_slider,
			minimum=0,
			maximum=10,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.GridAdd(_com_volume_slider_sizer, 1, 5, 1, 1)
		self._com_freq_entry_1_text_box = forms.text_box(
			parent=self.GetWin(),
			value=self.com_freq_entry_1,
			callback=self.set_com_freq_entry_1,
			label='com_freq_entry_1',
			converter=forms.float_converter(),
		)
		self.GridAdd(self._com_freq_entry_1_text_box, 0, 0, 1, 1)
		self._com_enable_check_box = forms.check_box(
			parent=self.GetWin(),
			value=self.com_enable,
			callback=self.set_com_enable,
			label='com_enable',
			true=1,
			false=0,
		)
		self.GridAdd(self._com_enable_check_box, 2, 3, 1, 1)
		self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
			self.notebook_0.GetPage(3).GetWin(),
			title="Scope Plot",
			sample_rate=12.5e3,
			v_scale=0,
			v_offset=0,
			t_scale=0,
			ac_couple=False,
			xy_mode=False,
			num_inputs=2,
			trig_mode=gr.gr_TRIG_MODE_AUTO,
			y_axis_label="Counts",
		)
		self.notebook_0.GetPage(3).Add(self.wxgui_scopesink2_0.win)
		self.wxgui_numbersink2_0 = numbersink2.number_sink_f(
			self.GetWin(),
			unit="Units",
			minval=-200,
			maxval=200,
			factor=1.0,
			decimal_places=10,
			ref_level=0,
			sample_rate=25e3/2000,
			number_rate=15,
			average=True,
			avg_alpha=0.02,
			label="Number Plot",
			peak_hold=False,
			show_gauge=True,
		)
		self.Add(self.wxgui_numbersink2_0.win)
		self.wxgui_fftsink2_0_1 = fftsink2.fft_sink_c(
			self.notebook_0.GetPage(0).GetWin(),
			baseband_freq=0,
			y_per_div=10,
			y_divs=10,
			ref_level=0,
			ref_scale=2.0,
			sample_rate=25e3,
			fft_size=1024,
			fft_rate=5,
			average=False,
			avg_alpha=None,
			title="FFT Plot",
			peak_hold=False,
		)
		self.notebook_0.GetPage(0).Add(self.wxgui_fftsink2_0_1.win)
		self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
			self.notebook_0.GetPage(1).GetWin(),
			baseband_freq=0,
			y_per_div=10,
			y_divs=10,
			ref_level=0,
			ref_scale=2.0,
			sample_rate=12.5e3,
			fft_size=1024,
			fft_rate=5,
			average=False,
			avg_alpha=None,
			title="FFT Plot",
			peak_hold=False,
		)
		self.notebook_0.GetPage(1).Add(self.wxgui_fftsink2_0.win)
		self.uhd_usrp_source_0 = uhd.usrp_source(
			device_addr="",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(2),
			),
		)
		self.uhd_usrp_source_0.set_clock_source("internal", 0)
		self.uhd_usrp_source_0.set_subdev_spec("A:0 A:0", 0)
		self.uhd_usrp_source_0.set_samp_rate(vor_samp_rate)
		self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(com_freq_entry_1, rf_freq=system_center_freq, rf_freq_policy=uhd.tune_request.POLICY_MANUAL), 0)
		self.uhd_usrp_source_0.set_gain(rx_gain, 0)
		self.uhd_usrp_source_0.set_antenna("RX2", 0)
		self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(vor_freq_entry_1, rf_freq=system_center_freq, rf_freq_policy=uhd.tune_request.POLICY_MANUAL), 1)
		self.uhd_usrp_source_0.set_gain(rx_gain, 1)
		self.uhd_usrp_source_0.set_antenna("RX2", 1)
		self.uhd_usrp_sink_0 = uhd.usrp_sink(
			device_addr="",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_sink_0.set_samp_rate(250e3)
		self.uhd_usrp_sink_0.set_center_freq(com_freq_entry_1, 0)
		self.uhd_usrp_sink_0.set_gain(25, 0)
		self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
		_squelch_slider_sizer = wx.BoxSizer(wx.VERTICAL)
		self._squelch_slider_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_squelch_slider_sizer,
			value=self.squelch_slider,
			callback=self.set_squelch_slider,
			label='squelch_slider',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._squelch_slider_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_squelch_slider_sizer,
			value=self.squelch_slider,
			callback=self.set_squelch_slider,
			minimum=-100,
			maximum=0,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.GridAdd(_squelch_slider_sizer, 1, 0, 1, 1)
		self.squelch = gr.pwr_squelch_cc(squelch_slider, 0.01, 20, False)
		self.openavionics_joystick_interface_0 = openavionics.joystick_interface()
		self.openavionics_audio_ptt_0 = openavionics.audio_ptt()
		self.low_pass_filter_3_0 = filter.fir_filter_fff(5, firdes.low_pass(
			1, 25e3, 200, 50, firdes.WIN_HAMMING, 6.76))
		self.low_pass_filter_3 = filter.fir_filter_fff(5, firdes.low_pass(
			1, 25e3, 200, 50, firdes.WIN_HAMMING, 6.76))
		self.low_pass_filter_2 = filter.fir_filter_ccf(1, firdes.low_pass(
			1, 25e3, 3e3, 500, firdes.WIN_HAMMING, 6.76))
		self.low_pass_filter_1 = filter.interp_fir_filter_fff(1, firdes.low_pass(
			1, 12.5e3, 3e3, 1e3, firdes.WIN_HAMMING, 6.76))
		self.low_pass_filter_0_0 = filter.fir_filter_ccf(int(250e3/25e3), firdes.low_pass(
			1, vor_samp_rate, 11e3, 1e3, firdes.WIN_HAMMING, 6.76))
		self.low_pass_filter_0 = filter.fir_filter_ccf(int(250e3/12.5e3), firdes.low_pass(
			1, vor_samp_rate, 10e3, 1e3, firdes.WIN_HAMMING, 6.76))
		self.gr_sig_source_x_0 = gr.sig_source_c(25e3, gr.GR_COS_WAVE, 9960, 1, 0)
		self.gr_quadrature_demod_cf_0 = gr.quadrature_demod_cf(1)
		self.gr_pwr_squelch_xx_0 = gr.pwr_squelch_ff(-50, 0.5, 1, False)
		self.gr_null_sink_0_0 = gr.null_sink(gr.sizeof_gr_complex*1)
		self.gr_multiply_xx_0_0_1 = gr.multiply_vff(1)
		self.gr_multiply_xx_0_0_0_0 = gr.multiply_vcc(1)
		self.gr_multiply_xx_0 = gr.multiply_vcc(1)
		self.gr_float_to_complex_0_0_0 = gr.float_to_complex(1)
		self.gr_float_to_complex_0 = gr.float_to_complex(1)
		self.gr_agc2_xx_0_0 = gr.agc2_cc(1, 1, 0.75, 1.0, 0.0)
		self.gr_agc2_xx_0 = gr.agc2_cc(1, 1, 0.75, 1.0, 0.0)
		self.gr_add_xx_0_0_0 = gr.add_vff(1)
		_gain_slider_sizer = wx.BoxSizer(wx.VERTICAL)
		self._gain_slider_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_gain_slider_sizer,
			value=self.gain_slider,
			callback=self.set_gain_slider,
			label='gain_slider',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._gain_slider_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_gain_slider_sizer,
			value=self.gain_slider,
			callback=self.set_gain_slider,
			minimum=0,
			maximum=30,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.GridAdd(_gain_slider_sizer, 1, 1, 1, 1)
		self.fft_tone_to_angle_0 = fft_tone_to_angle(
			fft_bin=12,
			fft_size=2000,
		)
		self.const_source_x_0_1 = gr.sig_source_f(0, gr.GR_CONST_WAVE, 0, 0, 0.450)
		self.const_source_x_0_0_1 = gr.sig_source_f(0, gr.GR_CONST_WAVE, 0, 0, 0.550)
		self.const_source_x_0_0_0_0 = gr.sig_source_c(0, gr.GR_CONST_WAVE, 0, 0, 0.450)
		self.blocks_null_sink_1 = blocks.null_sink(gr.sizeof_float*1)
		self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
		self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((180.0/3.1415, ))
		self.blocks_add_xx_0 = blocks.add_vff(1)
		self.blks2_rational_resampler_xxx_2_0 = blks2.rational_resampler_fff(
			interpolation=250,
			decimation=48,
			taps=None,
			fractional_bw=None,
		)
		self.blks2_rational_resampler_xxx_1 = blks2.rational_resampler_fff(
			interpolation=480,
			decimation=125,
			taps=None,
			fractional_bw=None,
		)
		self.blks2_am_demod_cf_0_0 = blks2.am_demod_cf(
			channel_rate=25e3,
			audio_decim=am_decimation,
			audio_pass=11.5e3,
			audio_stop=12.250e3,
		)
		self.blks2_am_demod_cf_0 = blks2.am_demod_cf(
			channel_rate=am_sample_rate,
			audio_decim=am_decimation,
			audio_pass=3e3,
			audio_stop=4e3,
		)
		self.band_pass_filter_0 = gr.fir_filter_fff(2, firdes.band_pass(
			1, 25000, 980, 1150, 50, firdes.WIN_HAMMING, 6.76))
		self.audio_sink_0 = audio.sink(int(audio_sample_rate), "", True)
		self._audio_select_chooser = forms.drop_down(
			parent=self.GetWin(),
			value=self.audio_select,
			callback=self.set_audio_select,
			label='audio_select',
			choices=[0, 1],
			labels=['AM Voice','VOR Subcarrier'],
		)
		self.GridAdd(self._audio_select_chooser, 0, 2, 1, 1)
		self.analog_sig_source_x_0_0 = analog.sig_source_f(48000, analog.GR_COS_WAVE, 1000, 1, 0)
		self.adsf_0 = blocks.multiply_const_vff((com_enable*com_volume_slider, ))
		self.adsf = blocks.multiply_const_vff((vor_ident*vor_volume_slider, ))

		##################################################
		# Connections
		##################################################
		self.connect((self.gr_float_to_complex_0, 0), (self.gr_multiply_xx_0, 0))
		self.connect((self.blks2_rational_resampler_xxx_1, 0), (self.audio_sink_0, 0))
		self.connect((self.blks2_am_demod_cf_0, 0), (self.low_pass_filter_1, 0))
		self.connect((self.uhd_usrp_source_0, 0), (self.low_pass_filter_0, 0))
		self.connect((self.uhd_usrp_source_0, 1), (self.gr_null_sink_0_0, 0))
		self.connect((self.low_pass_filter_0, 0), (self.squelch, 0))
		self.connect((self.squelch, 0), (self.gr_agc2_xx_0, 0))
		self.connect((self.low_pass_filter_0, 0), (self.wxgui_fftsink2_0, 0))
		self.connect((self.gr_agc2_xx_0, 0), (self.blks2_am_demod_cf_0, 0))
		self.connect((self.low_pass_filter_0_0, 0), (self.wxgui_fftsink2_0_1, 0))
		self.connect((self.gr_agc2_xx_0_0, 0), (self.blks2_am_demod_cf_0_0, 0))
		self.connect((self.uhd_usrp_source_0, 1), (self.low_pass_filter_0_0, 0))
		self.connect((self.blks2_am_demod_cf_0_0, 0), (self.gr_float_to_complex_0, 0))
		self.connect((self.fft_tone_to_angle_0, 0), (self.blocks_multiply_const_vxx_0, 0))
		self.connect((self.blocks_multiply_const_vxx_0, 0), (self.wxgui_numbersink2_0, 0))
		self.connect((self.fft_tone_to_angle_0, 1), (self.blocks_null_sink_0, 0))
		self.connect((self.fft_tone_to_angle_0, 2), (self.blocks_null_sink_1, 0))
		self.connect((self.low_pass_filter_0_0, 0), (self.gr_agc2_xx_0_0, 0))
		self.connect((self.gr_quadrature_demod_cf_0, 0), (self.low_pass_filter_3, 0))
		self.connect((self.low_pass_filter_3, 0), (self.fft_tone_to_angle_0, 0))
		self.connect((self.low_pass_filter_3_0, 0), (self.fft_tone_to_angle_0, 1))
		self.connect((self.blks2_am_demod_cf_0_0, 0), (self.low_pass_filter_3_0, 0))
		self.connect((self.blks2_am_demod_cf_0_0, 0), (self.gr_float_to_complex_0, 1))
		self.connect((self.gr_multiply_xx_0, 0), (self.low_pass_filter_2, 0))
		self.connect((self.gr_sig_source_x_0, 0), (self.gr_multiply_xx_0, 1))
		self.connect((self.low_pass_filter_2, 0), (self.gr_quadrature_demod_cf_0, 0))
		self.connect((self.blks2_am_demod_cf_0_0, 0), (self.band_pass_filter_0, 0))
		self.connect((self.adsf, 0), (self.blocks_add_xx_0, 1))
		self.connect((self.blocks_add_xx_0, 0), (self.blks2_rational_resampler_xxx_1, 0))
		self.connect((self.adsf, 0), (self.wxgui_scopesink2_0, 1))
		self.connect((self.low_pass_filter_1, 0), (self.adsf_0, 0))
		self.connect((self.adsf_0, 0), (self.blocks_add_xx_0, 0))
		self.connect((self.adsf_0, 0), (self.wxgui_scopesink2_0, 0))
		self.connect((self.band_pass_filter_0, 0), (self.gr_pwr_squelch_xx_0, 0))
		self.connect((self.gr_pwr_squelch_xx_0, 0), (self.adsf, 0))
		self.connect((self.const_source_x_0_0_0_0, 0), (self.gr_multiply_xx_0_0_0_0, 1))
		self.connect((self.gr_float_to_complex_0_0_0, 0), (self.gr_multiply_xx_0_0_0_0, 0))
		self.connect((self.gr_add_xx_0_0_0, 0), (self.gr_float_to_complex_0_0_0, 1))
		self.connect((self.gr_add_xx_0_0_0, 0), (self.gr_float_to_complex_0_0_0, 0))
		self.connect((self.const_source_x_0_0_1, 0), (self.gr_add_xx_0_0_0, 1))
		self.connect((self.gr_multiply_xx_0_0_1, 0), (self.gr_add_xx_0_0_0, 0))
		self.connect((self.const_source_x_0_1, 0), (self.gr_multiply_xx_0_0_1, 1))
		self.connect((self.gr_multiply_xx_0_0_0_0, 0), (self.uhd_usrp_sink_0, 0))
		self.connect((self.blks2_rational_resampler_xxx_2_0, 0), (self.openavionics_audio_ptt_0, 0))
		self.connect((self.analog_sig_source_x_0_0, 0), (self.blks2_rational_resampler_xxx_2_0, 0))
		self.connect((self.openavionics_audio_ptt_0, 0), (self.gr_multiply_xx_0_0_1, 0))

		##################################################
		# Asynch Message Connections
		##################################################
		self.msg_connect(self.openavionics_joystick_interface_0, "out", self.openavionics_audio_ptt_0, "in2")

	def get_antenna(self):
		return self.antenna

	def set_antenna(self, antenna):
		self.antenna = antenna

	def get_rx_gain(self):
		return self.rx_gain

	def set_rx_gain(self, rx_gain):
		self.rx_gain = rx_gain
		self.uhd_usrp_source_0.set_gain(self.rx_gain, 0)
		self.uhd_usrp_source_0.set_gain(self.rx_gain, 1)

	def get_vor_samp_rate(self):
		return self.vor_samp_rate

	def set_vor_samp_rate(self, vor_samp_rate):
		self.vor_samp_rate = vor_samp_rate
		self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.vor_samp_rate, 10e3, 1e3, firdes.WIN_HAMMING, 6.76))
		self.uhd_usrp_source_0.set_samp_rate(self.vor_samp_rate)
		self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.vor_samp_rate, 11e3, 1e3, firdes.WIN_HAMMING, 6.76))

	def get_com_freq_1(self):
		return self.com_freq_1

	def set_com_freq_1(self, com_freq_1):
		self.com_freq_1 = com_freq_1
		self.set_com_freq_entry_1(self.com_freq_1)

	def get_gain(self):
		return self.gain

	def set_gain(self, gain):
		self.gain = gain
		self.set_gain_slider(self.gain)

	def get_vor_freq_1(self):
		return self.vor_freq_1

	def set_vor_freq_1(self, vor_freq_1):
		self.vor_freq_1 = vor_freq_1
		self.set_vor_freq_entry_1(self.vor_freq_1)

	def get_obs_decimation(self):
		return self.obs_decimation

	def set_obs_decimation(self, obs_decimation):
		self.obs_decimation = obs_decimation
		self.set_obs_sample_rate(self.am_sample_rate/self.obs_decimation)

	def get_ils_decimation(self):
		return self.ils_decimation

	def set_ils_decimation(self, ils_decimation):
		self.ils_decimation = ils_decimation
		self.set_ils_sample_rate(self.am_sample_rate/self.ils_decimation)

	def get_am_sample_rate(self):
		return self.am_sample_rate

	def set_am_sample_rate(self, am_sample_rate):
		self.am_sample_rate = am_sample_rate
		self.set_ils_sample_rate(self.am_sample_rate/self.ils_decimation)
		self.set_obs_sample_rate(self.am_sample_rate/self.obs_decimation)

	def get_vor_volume_slider(self):
		return self.vor_volume_slider

	def set_vor_volume_slider(self, vor_volume_slider):
		self.vor_volume_slider = vor_volume_slider
		self.adsf.set_k((self.vor_ident*self.vor_volume_slider, ))
		self._vor_volume_slider_slider.set_value(self.vor_volume_slider)
		self._vor_volume_slider_text_box.set_value(self.vor_volume_slider)

	def get_vor_ident(self):
		return self.vor_ident

	def set_vor_ident(self, vor_ident):
		self.vor_ident = vor_ident
		self._vor_ident_check_box.set_value(self.vor_ident)
		self.adsf.set_k((self.vor_ident*self.vor_volume_slider, ))

	def get_vor_freq_entry_1(self):
		return self.vor_freq_entry_1

	def set_vor_freq_entry_1(self, vor_freq_entry_1):
		self.vor_freq_entry_1 = vor_freq_entry_1
		self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.vor_freq_entry_1, rf_freq=self.system_center_freq, rf_freq_policy=uhd.tune_request.POLICY_MANUAL), 1)
		self._vor_freq_entry_1_text_box.set_value(self.vor_freq_entry_1)

	def get_vor_center_freq_0(self):
		return self.vor_center_freq_0

	def set_vor_center_freq_0(self, vor_center_freq_0):
		self.vor_center_freq_0 = vor_center_freq_0

	def get_system_center_freq(self):
		return self.system_center_freq

	def set_system_center_freq(self, system_center_freq):
		self.system_center_freq = system_center_freq
		self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.com_freq_entry_1, rf_freq=self.system_center_freq, rf_freq_policy=uhd.tune_request.POLICY_MANUAL), 0)
		self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.vor_freq_entry_1, rf_freq=self.system_center_freq, rf_freq_policy=uhd.tune_request.POLICY_MANUAL), 1)

	def get_squelch_slider(self):
		return self.squelch_slider

	def set_squelch_slider(self, squelch_slider):
		self.squelch_slider = squelch_slider
		self._squelch_slider_slider.set_value(self.squelch_slider)
		self._squelch_slider_text_box.set_value(self.squelch_slider)
		self.squelch.set_threshold(self.squelch_slider)

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate

	def get_rxgain(self):
		return self.rxgain

	def set_rxgain(self, rxgain):
		self.rxgain = rxgain

	def get_phase_correction(self):
		return self.phase_correction

	def set_phase_correction(self, phase_correction):
		self.phase_correction = phase_correction

	def get_obs_sample_rate(self):
		return self.obs_sample_rate

	def set_obs_sample_rate(self, obs_sample_rate):
		self.obs_sample_rate = obs_sample_rate

	def get_ils_sample_rate(self):
		return self.ils_sample_rate

	def set_ils_sample_rate(self, ils_sample_rate):
		self.ils_sample_rate = ils_sample_rate

	def get_gain_slider(self):
		return self.gain_slider

	def set_gain_slider(self, gain_slider):
		self.gain_slider = gain_slider
		self._gain_slider_slider.set_value(self.gain_slider)
		self._gain_slider_text_box.set_value(self.gain_slider)

	def get_correction_gain(self):
		return self.correction_gain

	def set_correction_gain(self, correction_gain):
		self.correction_gain = correction_gain

	def get_com_volume_slider(self):
		return self.com_volume_slider

	def set_com_volume_slider(self, com_volume_slider):
		self.com_volume_slider = com_volume_slider
		self.adsf_0.set_k((self.com_enable*self.com_volume_slider, ))
		self._com_volume_slider_slider.set_value(self.com_volume_slider)
		self._com_volume_slider_text_box.set_value(self.com_volume_slider)

	def get_com_freq_entry_1(self):
		return self.com_freq_entry_1

	def set_com_freq_entry_1(self, com_freq_entry_1):
		self.com_freq_entry_1 = com_freq_entry_1
		self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.com_freq_entry_1, rf_freq=self.system_center_freq, rf_freq_policy=uhd.tune_request.POLICY_MANUAL), 0)
		self._com_freq_entry_1_text_box.set_value(self.com_freq_entry_1)
		self.uhd_usrp_sink_0.set_center_freq(self.com_freq_entry_1, 0)

	def get_com_enable(self):
		return self.com_enable

	def set_com_enable(self, com_enable):
		self.com_enable = com_enable
		self._com_enable_check_box.set_value(self.com_enable)
		self.adsf_0.set_k((self.com_enable*self.com_volume_slider, ))

	def get_audio_select(self):
		return self.audio_select

	def set_audio_select(self, audio_select):
		self.audio_select = audio_select
		self._audio_select_chooser.set_value(self.audio_select)

	def get_audio_sample_rate(self):
		return self.audio_sample_rate

	def set_audio_sample_rate(self, audio_sample_rate):
		self.audio_sample_rate = audio_sample_rate

	def get_am_decimation(self):
		return self.am_decimation

	def set_am_decimation(self, am_decimation):
		self.am_decimation = am_decimation

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	parser.add_option("", "--antenna", dest="antenna", type="string", default="TX/RX",
		help="Set antenna [default=%default]")
	(options, args) = parser.parse_args()
	tb = simple_trx(antenna=options.antenna)
	tb.Run(True)

