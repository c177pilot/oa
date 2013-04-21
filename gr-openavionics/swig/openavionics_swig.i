/* -*- c++ -*- */

#define OPENAVIONICS_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "openavionics_swig_doc.i"

%{
#include "openavionics/square_ff.h"
%}


%include "openavionics/square_ff.h"
GR_SWIG_BLOCK_MAGIC2(openavionics, square_ff);
