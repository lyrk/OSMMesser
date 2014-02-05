from setuptools import setup, find_packages

setup(
	name = "OSMMesser",
	version = "0.1",
	scripts = ['osmmesser.py'],
	install_requires = ['imposm.parser>=1.0.4'],

	package_data = {
	},

	author = "Thomas Skowron",
	author_email = "thomas@lyrk.org",
	description = "A tool for measuring ways in OpenStreetMap files.",
	license = "BSD"
)