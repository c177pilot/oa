#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Ahrs Gps Eis To Fg
# Generated: Thu Aug  1 11:53:44 2013
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import openavionics
import wx

class ahrs_gps_eis_to_fg(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Ahrs Gps Eis To Fg")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.openavionics_serial_io_0_0_0 = openavionics.serial_io("/dev/pts/14",0,19200,0,1,False)
        self.openavionics_serial_io_0_0 = openavionics.serial_io("/dev/pts/12",0,19200,0,1,False)
        self.openavionics_serial_io_0 = openavionics.serial_io("/dev/pts/10",0,19200,0,1,False)
        self.openavionics_gns430_to_fg_0 = openavionics.gns430_to_fg("127.0.0.1",5502)
        self.openavionics_gns430_parser_0 = openavionics.gns430_parser()
        self.openavionics_eis_parser_0 = openavionics.eis_parser()
        self.openavionics_ahrs_to_fg_0 = openavionics.ahrs_to_fg("127.0.0.1",5501)
        self.openavionics_ahrs_parser_0 = openavionics.ahrs_parser()
        self.blocks_message_debug_0_0_0 = blocks.message_debug()

        ##################################################
        # Asynch Message Connections
        ##################################################
        self.msg_connect(self.openavionics_serial_io_0_0_0, "out", self.openavionics_gns430_parser_0, "in")
        self.msg_connect(self.openavionics_gns430_parser_0, "out", self.openavionics_gns430_to_fg_0, "in")
        self.msg_connect(self.openavionics_ahrs_parser_0, "out", self.openavionics_ahrs_to_fg_0, "in")
        self.msg_connect(self.openavionics_serial_io_0, "out", self.openavionics_ahrs_parser_0, "in")
        self.msg_connect(self.openavionics_serial_io_0_0, "out", self.openavionics_eis_parser_0, "in")
        self.msg_connect(self.openavionics_gns430_parser_0, "out", self.blocks_message_debug_0_0_0, "print")

# QT sink close method reimplementation

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = ahrs_gps_eis_to_fg()
    tb.Start(True)
    tb.Wait()

