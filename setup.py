import os
import sys
import subprocess
from setuptools import setup, find_packages

setup(
	name = "OSMMesser",
	version = "0.1",
	scripts = ['osmmesser.py'],
	install_requires = ['imposm.parser>=1.0.4'],
	author = "Thomas Skowron",
	author_email = "thomas@lyrk.org",
	description = "A tool for measuring ways in OpenStreetMap files.",
	license = "BSD"
)

if sys.argv[1] == "install":
	subprocess.call("wget -O - http://m.m.i24.cc/osmfilter.c | cc -x c - -O3 -o /usr/local/bin/osmfilter", shell=True)
	subprocess.call("wget -O - http://m.m.i24.cc/osmconvert.c | cc -x c - -lz -O3 -o /usr/local/bin/osmconvert", shell=True)