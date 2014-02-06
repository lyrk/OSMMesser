#!/usr/bin/env python
"""Copyright (c) 2014, Thomas Skowron
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."""

import os
import sys
import subprocess
import argparse
from math import radians, cos, sin, asin, sqrt

try:
	from imposm.parser import OSMParser
except ImportError as e:
	print("""It appears that imposm.parser is not installed.
In order to install dependencies, type: python setup.py install""")
	sys.exit(0)


class OSMMeter(object):
	def __init__(self, filepath, silent=True):
		self.filepath = filepath
		self.way_distances = []
		self.coords = {}
		self.ways = []
		self.silent = silent


	def calc_all_ways(self):
		p = OSMParser(concurrency=4, coords_callback=self._read_coords,
			ways_callback=self._read_ways)
		if not self.silent:
			print("Reading file")
		p.parse(self.filepath)
		if not self.silent:
			print("Summing")
		self._calc_ways()
		return sum(self.way_distances)


	def _read_coords(self, coordlist):
		for coord in coordlist:
			self.coords[coord[0]] = (coord[1], coord[2])


	def _read_ways(self, waylist):
		for way in waylist:
			self.ways.append(way)


	def _calc_ways(self):
		for way in self.ways:
			last_node = None
			way_length = 0

			for node_id in way[2]:
				node = self.coords[node_id]
				if last_node is not None:
					way_length += self.haversine(last_node[0], last_node[1],
						node[0], node[1])
				last_node = (node[0], node[1])

			self.way_distances.append(way_length)


	def _read_ways_and_calc(self, waylist):
		for way in waylist:
			last_node = None
			way_length = 0

			for node_id in way[2]:
				node = self.coords[node_id]
				if last_node is not None:
					way_length += self.haversine(last_node[0], last_node[1],
						node[0], node[1])
				last_node = (node[0], node[1])

			self.way_distances.append(way_length)


	def haversine(self, lon1, lat1, lon2, lat2):
		EARTHRAD = 6367
		lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
		dlon = lon2 - lon1
		dlat = lat2 - lat1
		a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
		c = 2 * asin(sqrt(a))
		return EARTHRAD * c


def filter_and_process(filepath, filterargs, silent):
	converted = False

	if filepath.endswith(".pbf"):
		o5mfile = "osmmesser_temp.o5m"
		if not silent:
			print("Converting file")
		subprocess.call("osmconvert {} -o={}".format(filepath, o5mfile), shell=True)
		converted = True
	else:
		o5mfile = filepath

	outputpath = "osmmesser_temp.osm"
	if not silent:
		print("Filtering file")
	subprocess.call("""osmfilter {} --keep="{}" -o={}""".format(o5mfile, filterargs, outputpath), shell=True)
	o = OSMMeter(outputpath)
	print(str(o.calc_all_ways()) + " km")

	if converted:
		os.remove(o5mfile)
	os.remove(outputpath)


def main():
	parser = argparse.ArgumentParser(description="Measuring way lengths in OSM files.")
	parser.add_argument('--filter', help="""filtering arguments for osmfilter, as specified in http://wiki.openstreetmap.org/wiki/Osmfilter, e.g. "highway=track" """)
	parser.add_argument('osmfile', help="file to be processed")
	parser.add_argument('-s', '--silent', action='store_true', help='prints out only the final result, no progress will be show while processing')

	args = parser.parse_args()

	if args.filter:
		filter_and_process(args.osmfile, args.filter, args.silent)
	else:
		o = OSMMeter(args.osmfile)
		print(str(o.calc_all_ways()) + " km")


if __name__ == "__main__":
	main()