#!/bin/sh
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/john/src/openavionics/gr-openavionics.backup/python
export PATH=/home/john/src/openavionics/gr-openavionics.backup/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export DYLD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export PYTHONPATH=/home/john/src/openavionics/gr-openavionics.backup/build/swig:$PYTHONPATH
/usr/bin/python /home/john/src/openavionics/gr-openavionics.backup/python/qa_square_ff.py 
