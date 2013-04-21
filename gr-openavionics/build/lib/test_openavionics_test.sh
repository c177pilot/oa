#!/bin/sh
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/john/src/openavionics/gr-openavionics.backup/lib
export PATH=/home/john/src/openavionics/gr-openavionics.backup/build/lib:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export DYLD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-openavionics 
