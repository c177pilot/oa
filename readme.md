This is a readme file 

Repository contents
==============================

gr-openavionics
------------------------------
Misc GNU Radio blocks (out-of-tree) that are used to parse, route, and present data.

Use the following instructions to install all dependencies (ubuntu 12.10 + )

	sudo apt-get install python-pygame


ahrs_emul
------------------------------
This is an emulator that will parse log files from a Grand Rapid Technology EFIS
and output the data to a number of sinks with time alignment.  Basically, this 
script emulates all of the equipment on the aircraft - useful for debugging.

For more info on running the ahrs_emul with fgfs, see gr-openavionics/apps/running_emulato_to_flightgear.txt

fgfs_general_protocols
------------------------------
This has the general protocols used to parse data from the gnuradio apps.  You will need to install these in your
protocols directory in the flightgear installation.
