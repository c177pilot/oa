#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Fri Aug  2 08:32:54 2013
##################################################

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import filter
from gnuradio import gr
from gnuradio import uhd
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import numbersink2
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import math
import openavionics
import time
import wx

class top_block(grc_wxgui.top_block_gui):

    def __init__(self, antenna="TX/RX", vor_freq_1=111e6, com_freq_1=135.275e6, vor_freq_2=111e6, rx_gain=30, gain=20):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")

        ##################################################
        # Parameters
        ##################################################
        self.antenna = antenna
        self.vor_freq_1 = vor_freq_1
        self.com_freq_1 = com_freq_1
        self.vor_freq_2 = vor_freq_2
        self.rx_gain = rx_gain
        self.gain = gain

        ##################################################
        # Variables
        ##################################################
        self.obs_decimation = obs_decimation = 25
        self.ils_decimation = ils_decimation = 50
        self.am_sample_rate = am_sample_rate = 12.5e3
        self.vor_samp_rate = vor_samp_rate = 250e3
        self.vor_freq_entry_2 = vor_freq_entry_2 = vor_freq_2
        self.vor_freq_entry_1 = vor_freq_entry_1 = vor_freq_1
        self.vor_center_freq_0 = vor_center_freq_0 = (117.95e6-108.00e6)/2+117.95e6
        self.vor_center_freq = vor_center_freq = (117.95e6-108.00e6)/2+117.95e6
        self.squelch_slider = squelch_slider = -110
        self.rxgain = rxgain = 15
        self.phase_correction = phase_correction = 5
        self.obs_sample_rate = obs_sample_rate = am_sample_rate/obs_decimation
        self.ils_sample_rate = ils_sample_rate = am_sample_rate/ils_decimation
        self.gain_slider = gain_slider = gain
        self.com_freq_entry_1 = com_freq_entry_1 = com_freq_1
        self.band_center_freq = band_center_freq = (136.975e6-108.0e6)/2+108.0e6
        self.audio_select = audio_select = 0
        self.audio_sample_rate = audio_sample_rate = 48e3
        self.am_decimation = am_decimation = 1

        ##################################################
        # Blocks
        ##################################################
        self.notebook_0 = self.notebook_0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "RF Analyzer")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Channel FFT")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Demod Audio FFT")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Ref and Phase Scope")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Manipulated Ref and Phase")
        self.Add(self.notebook_0)
        self._vor_freq_entry_1_text_box = forms.text_box(
        	parent=self.notebook_0.GetPage(0).GetWin(),
        	value=self.vor_freq_entry_1,
        	callback=self.set_vor_freq_entry_1,
        	label='vor_freq_entry_1',
        	converter=forms.float_converter(),
        )
        self.notebook_0.GetPage(0).Add(self._vor_freq_entry_1_text_box)
        _gain_slider_sizer = wx.BoxSizer(wx.VERTICAL)
        self._gain_slider_text_box = forms.text_box(
        	parent=self.notebook_0.GetPage(0).GetWin(),
        	sizer=_gain_slider_sizer,
        	value=self.gain_slider,
        	callback=self.set_gain_slider,
        	label='gain_slider',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._gain_slider_slider = forms.slider(
        	parent=self.notebook_0.GetPage(0).GetWin(),
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
        self.notebook_0.GetPage(0).Add(_gain_slider_sizer)
        self._com_freq_entry_1_text_box = forms.text_box(
        	parent=self.notebook_0.GetPage(0).GetWin(),
        	value=self.com_freq_entry_1,
        	callback=self.set_com_freq_entry_1,
        	label='com_freq_entry_1',
        	converter=forms.float_converter(),
        )
        self.notebook_0.GetPage(0).Add(self._com_freq_entry_1_text_box)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.notebook_0.GetPage(1).GetWin(),
        	title="Scope Plot",
        	sample_rate=10e3,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=2,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.notebook_0.GetPage(1).Add(self.wxgui_scopesink2_0.win)
        self.wxgui_numbersink2_0 = numbersink2.number_sink_f(
        	self.GetWin(),
        	unit="Units",
        	minval=-100,
        	maxval=100,
        	factor=1.0,
        	decimal_places=10,
        	ref_level=0,
        	sample_rate=10,
        	number_rate=15,
        	average=False,
        	avg_alpha=None,
        	label="Number Plot",
        	peak_hold=False,
        	show_gauge=True,
        )
        self.Add(self.wxgui_numbersink2_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.notebook_0.GetPage(0).GetWin(),
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
        self.notebook_0.GetPage(0).Add(self.wxgui_fftsink2_0.win)
        self._vor_freq_entry_2_text_box = forms.text_box(
        	parent=self.notebook_0.GetPage(0).GetWin(),
        	value=self.vor_freq_entry_2,
        	callback=self.set_vor_freq_entry_2,
        	label='vor_freq_entry_2',
        	converter=forms.float_converter(),
        )
        self.notebook_0.GetPage(0).Add(self._vor_freq_entry_2_text_box)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	device_addr="",
        	stream_args=uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(2),
        	),
        )
        self.uhd_usrp_source_0.set_subdev_spec("A:0 A:0", 0)
        self.uhd_usrp_source_0.set_samp_rate(vor_samp_rate)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(com_freq_entry_1,rf_freq=band_center_freq, rf_freq_policy=uhd.tune_request.POLICY_MANUAL), 0)
        self.uhd_usrp_source_0.set_gain(gain_slider, 0)
        self.uhd_usrp_source_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(vor_freq_entry_1, rf_freq=band_center_freq, rf_freq_policy=uhd.tune_request.POLICY_MANUAL), 1)
        self.uhd_usrp_source_0.set_gain(gain_slider, 1)
        self.uhd_usrp_source_0.set_antenna("TX/RX", 1)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	device_addr="",
        	stream_args=uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(250e3)
        self.uhd_usrp_sink_0.set_center_freq(uhd.tune_request(com_freq_entry_1,20e6), 0)
        self.uhd_usrp_sink_0.set_gain(15, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        _squelch_slider_sizer = wx.BoxSizer(wx.VERTICAL)
        self._squelch_slider_text_box = forms.text_box(
        	parent=self.notebook_0.GetPage(0).GetWin(),
        	sizer=_squelch_slider_sizer,
        	value=self.squelch_slider,
        	callback=self.set_squelch_slider,
        	label='squelch_slider',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._squelch_slider_slider = forms.slider(
        	parent=self.notebook_0.GetPage(0).GetWin(),
        	sizer=_squelch_slider_sizer,
        	value=self.squelch_slider,
        	callback=self.set_squelch_slider,
        	minimum=-110,
        	maximum=0,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.notebook_0.GetPage(0).Add(_squelch_slider_sizer)
        self.squelch = analog.pwr_squelch_cc(squelch_slider, 0.01, 20, True)
        self.rational_resampler_xxx_2 = filter.rational_resampler_fff(
                interpolation=250,
                decimation=48,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=480,
                decimation=125,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=4,
                decimation=5,
                taps=None,
                fractional_bw=None,
        )
        self.openavionics_joystick_interface_0 = openavionics.joystick_interface()
        self.openavionics_audio_ptt_0 = openavionics.audio_ptt()
        self.null_sink_0_0_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.null_sink_0_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.multiply_xx_0_0_0 = blocks.multiply_vcc(1)
        self.multiply_xx_0_0 = blocks.multiply_vff(1)
        self.low_pass_filter_3 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, 10e3, 1, 2, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_2_0_0 = filter.fir_filter_ccf(5, firdes.low_pass(
        	1, 40e3, 2e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_2_0 = filter.fir_filter_ccf(5, firdes.low_pass(
        	1, 40e3, 2e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_2 = filter.fir_filter_ccf(5, firdes.low_pass(
        	1, vor_samp_rate, 15e3, 5e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_1 = filter.interp_fir_filter_fff(1, firdes.low_pass(
        	1, 12.5e3, 3e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(int(250e3/12.5e3), firdes.low_pass(
        	1, vor_samp_rate, 10e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.goertzel_fc_0_0 = fft.goertzel_fc(10000, 1000, 30)
        self.goertzel_fc_0 = fft.goertzel_fc(40000, 4000, 30)
        self.float_to_complex_0_0 = blocks.float_to_complex(1)
        self.const_source_x_0_0_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 0.450)
        self.const_source_x_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0.550)
        self.const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0.450)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(1)
        self.blocks_complex_to_arg_0 = blocks.complex_to_arg(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((-87.2665e-3, ))
        self.band_pass_filter_0_0 = filter.fir_filter_fff(4, firdes.band_pass(
        	1, 40e3, 20, 40, 20, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0 = filter.fir_filter_fff(1, firdes.band_pass(
        	1, 10e3, 20, 40, 20, firdes.WIN_HAMMING, 6.76))
        self.audio_source_0 = audio.source(48000, "", True)
        self.audio_sink_0 = audio.sink(int(audio_sample_rate), "", True)
        self._audio_select_chooser = forms.drop_down(
        	parent=self.GetWin(),
        	value=self.audio_select,
        	callback=self.set_audio_select,
        	label='audio_select',
        	choices=[0, 1],
        	labels=['AM Voice','VOR Subcarrier'],
        )
        self.Add(self._audio_select_chooser)
        self.analog_sig_source_x_0 = analog.sig_source_c(40e3, analog.GR_COS_WAVE, -9.96e3, 1, 0)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(1)
        self.analog_am_demod_cf_0 = analog.am_demod_cf(
        	channel_rate=40e3,
        	audio_decim=4,
        	audio_pass=5000,
        	audio_stop=5500,
        )
        self.analog_agc2_xx_0_1_0 = analog.agc2_ff(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0_1_0.set_max_gain(100)
        self.analog_agc2_xx_0_1 = analog.agc2_ff(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0_1.set_max_gain(100)
        self.analog_agc2_xx_0_0 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0_0.set_max_gain(100)
        self.analog_agc2_xx_0 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0.set_max_gain(100)
        self.am_demod_cf_0 = analog.am_demod_cf(
        	channel_rate=am_sample_rate,
        	audio_decim=am_decimation,
        	audio_pass=3e3,
        	audio_stop=4e3,
        )
        self.agc2_xx_0 = analog.agc2_cc(1, 1, 0.75, 1.0)
        self.agc2_xx_0.set_max_gain(0.0)
        self.add_xx_0_0 = blocks.add_vff(1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.agc2_xx_0, 0), (self.am_demod_cf_0, 0))
        self.connect((self.am_demod_cf_0, 0), (self.low_pass_filter_1, 0))
        self.connect((self.agc2_xx_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.multiply_xx_0_0, 0), (self.add_xx_0_0, 0))
        self.connect((self.const_source_x_0, 0), (self.multiply_xx_0_0, 1))
        self.connect((self.const_source_x_0_0, 0), (self.add_xx_0_0, 1))
        self.connect((self.multiply_xx_0_0_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.add_xx_0_0, 0), (self.float_to_complex_0_0, 0))
        self.connect((self.add_xx_0_0, 0), (self.float_to_complex_0_0, 1))
        self.connect((self.float_to_complex_0_0, 0), (self.multiply_xx_0_0_0, 0))
        self.connect((self.const_source_x_0_0_0, 0), (self.multiply_xx_0_0_0, 1))
        self.connect((self.uhd_usrp_source_0, 0), (self.null_sink_0_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.low_pass_filter_1, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.audio_sink_0, 0))
        self.connect((self.analog_agc2_xx_0_1_0, 0), (self.wxgui_scopesink2_0, 1))
        self.connect((self.analog_agc2_xx_0_1, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.analog_agc2_xx_0_1, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.analog_agc2_xx_0_1_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.goertzel_fc_0, 0))
        self.connect((self.analog_am_demod_cf_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.wxgui_numbersink2_0, 0))
        self.connect((self.blocks_complex_to_arg_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.low_pass_filter_3, 0), (self.blocks_complex_to_arg_0, 0))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.low_pass_filter_3, 0))
        self.connect((self.analog_agc2_xx_0, 0), (self.blocks_multiply_conjugate_cc_0, 1))
        self.connect((self.analog_agc2_xx_0_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))
        self.connect((self.goertzel_fc_0_0, 0), (self.analog_agc2_xx_0_0, 0))
        self.connect((self.analog_am_demod_cf_0, 0), (self.goertzel_fc_0_0, 0))
        self.connect((self.goertzel_fc_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.low_pass_filter_2_0_0, 0), (self.analog_am_demod_cf_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.low_pass_filter_2_0_0, 0))
        self.connect((self.low_pass_filter_2_0, 0), (self.analog_quadrature_demod_cf_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_2_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.uhd_usrp_source_0, 1), (self.null_sink_0_0, 0))
        self.connect((self.low_pass_filter_2, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.audio_source_0, 0), (self.openavionics_audio_ptt_0, 0))
        self.connect((self.openavionics_audio_ptt_0, 0), (self.rational_resampler_xxx_2, 0))
        self.connect((self.rational_resampler_xxx_2, 0), (self.multiply_xx_0_0, 0))
        self.connect((self.squelch, 0), (self.agc2_xx_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.squelch, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.low_pass_filter_2, 0))

        ##################################################
        # Asynch Message Connections
        ##################################################
        self.msg_connect(self.openavionics_joystick_interface_0, "out", self.openavionics_audio_ptt_0, "in2")

# QT sink close method reimplementation

    def get_antenna(self):
        return self.antenna

    def set_antenna(self, antenna):
        self.antenna = antenna

    def get_vor_freq_1(self):
        return self.vor_freq_1

    def set_vor_freq_1(self, vor_freq_1):
        self.vor_freq_1 = vor_freq_1
        self.set_vor_freq_entry_1(self.vor_freq_1)

    def get_com_freq_1(self):
        return self.com_freq_1

    def set_com_freq_1(self, com_freq_1):
        self.com_freq_1 = com_freq_1
        self.set_com_freq_entry_1(self.com_freq_1)

    def get_vor_freq_2(self):
        return self.vor_freq_2

    def set_vor_freq_2(self, vor_freq_2):
        self.vor_freq_2 = vor_freq_2
        self.set_vor_freq_entry_2(self.vor_freq_2)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.set_gain_slider(self.gain)

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
        self.set_obs_sample_rate(self.am_sample_rate/self.obs_decimation)
        self.set_ils_sample_rate(self.am_sample_rate/self.ils_decimation)

    def get_vor_samp_rate(self):
        return self.vor_samp_rate

    def set_vor_samp_rate(self, vor_samp_rate):
        self.vor_samp_rate = vor_samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.vor_samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.vor_samp_rate, 10e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_2.set_taps(firdes.low_pass(1, self.vor_samp_rate, 15e3, 5e3, firdes.WIN_HAMMING, 6.76))

    def get_vor_freq_entry_2(self):
        return self.vor_freq_entry_2

    def set_vor_freq_entry_2(self, vor_freq_entry_2):
        self.vor_freq_entry_2 = vor_freq_entry_2
        self._vor_freq_entry_2_text_box.set_value(self.vor_freq_entry_2)

    def get_vor_freq_entry_1(self):
        return self.vor_freq_entry_1

    def set_vor_freq_entry_1(self, vor_freq_entry_1):
        self.vor_freq_entry_1 = vor_freq_entry_1
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.vor_freq_entry_1, rf_freq=self.band_center_freq, rf_freq_policy=uhd.tune_request.POLICY_MANUAL), 1)
        self._vor_freq_entry_1_text_box.set_value(self.vor_freq_entry_1)

    def get_vor_center_freq_0(self):
        return self.vor_center_freq_0

    def set_vor_center_freq_0(self, vor_center_freq_0):
        self.vor_center_freq_0 = vor_center_freq_0

    def get_vor_center_freq(self):
        return self.vor_center_freq

    def set_vor_center_freq(self, vor_center_freq):
        self.vor_center_freq = vor_center_freq

    def get_squelch_slider(self):
        return self.squelch_slider

    def set_squelch_slider(self, squelch_slider):
        self.squelch_slider = squelch_slider
        self._squelch_slider_slider.set_value(self.squelch_slider)
        self._squelch_slider_text_box.set_value(self.squelch_slider)
        self.squelch.set_threshold(self.squelch_slider)

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
        self.uhd_usrp_source_0.set_gain(self.gain_slider, 0)
        self.uhd_usrp_source_0.set_gain(self.gain_slider, 1)
        self._gain_slider_slider.set_value(self.gain_slider)
        self._gain_slider_text_box.set_value(self.gain_slider)

    def get_com_freq_entry_1(self):
        return self.com_freq_entry_1

    def set_com_freq_entry_1(self, com_freq_entry_1):
        self.com_freq_entry_1 = com_freq_entry_1
        self._com_freq_entry_1_text_box.set_value(self.com_freq_entry_1)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.com_freq_entry_1,rf_freq=self.band_center_freq, rf_freq_policy=uhd.tune_request.POLICY_MANUAL), 0)
        self.uhd_usrp_sink_0.set_center_freq(uhd.tune_request(self.com_freq_entry_1,20e6), 0)

    def get_band_center_freq(self):
        return self.band_center_freq

    def set_band_center_freq(self, band_center_freq):
        self.band_center_freq = band_center_freq
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.com_freq_entry_1,rf_freq=self.band_center_freq, rf_freq_policy=uhd.tune_request.POLICY_MANUAL), 0)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.vor_freq_entry_1, rf_freq=self.band_center_freq, rf_freq_policy=uhd.tune_request.POLICY_MANUAL), 1)

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
    tb = top_block(antenna=options.antenna)
    tb.Run(True, 1000)

