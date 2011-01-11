from distutils.core import setup, Extension
import sys

if sys.version_info < (2, 6):
	print "At least Python 2.6 is required."
	sys.exit(1)

module = Extension('libcutadapt.calign', sources = [ 'calignmodule.c' ])

setup(
	name = 'cutadapt',
	version = '0.9.1',
	author = 'Marcel Martin',
	author_email = 'marcel.martin@tu-dortmund.de',
	url = 'http://code.google.com/p/cutadapt/',
	description = 'trim adapters from high-throughput sequencing reads',
	license = 'MIT',
	ext_modules = [ module ],
	packages = ['libcutadapt'],
	scripts = ['cutadapt'],
	classifiers = [
		"Development Status :: 5 - Production/Stable",
		"Environment :: Console",
		"Intended Audience :: Science/Research",
		"License :: OSI Approved :: MIT License",
		"Natural Language :: English",
		"Programming Language :: Python :: 2.6",
		"Programming Language :: Python :: 2.7",
		#"Programming Language :: Python :: 3",
		#"Operating System :: POSIX",
		"Topic :: Scientific/Engineering :: Bio-Informatics"
	]
)

# Aims for the package layout
#
# - The name of the program must be 'cutadapt'.
# - It must be possible to run cutadapt without installing the package, preferably
#   by typing ./cutadapt or something like ./scripts/cutadapt or ./bin/cutadapt.
# - Use a separate package for the additional modules, don't clutter the global
#   namespace.
