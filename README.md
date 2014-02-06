# OSMMesser

OSMMesser is a tool for measuring ways in OpenStreetMap files. Works on Python 2.7 and PyPy.


## Installation

Run `python setup.py install`.


## Usage

	osmmesser.py [-h] [--filter FILTER] [-s] osmfile

	Measuring way lengths in OSM files.

	positional arguments:
	  osmfile          file to be processed

	optional arguments:
	  -h, --help       show this help message and exit
	  --filter FILTER  filtering arguments for osmfilter, as specified in
	                   http://wiki.openstreetmap.org/wiki/Osmfilter, e.g.
	                   "highway=track"
	  -s, --silent     prints out only the final result, no progress will be show
	                   while processing


## License

__BSD 2 clause license. No bullshit.__


Copyright (c) 2014, Thomas Skowron

All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.