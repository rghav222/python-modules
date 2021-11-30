# python-modules
This is a collection of python modules that I use for simplifying my work.

fwhm.py:
This is a simple module for reading the full width at half/tenth maximum of a single peak, for a given dependent variable and independent variable.
To read FWHM use:
fwhm2(independent_variable, dependent_variable)
To read FWTM use:
fwtm2(independent_variable, dependent_variable)
The output is simple float number.

read_exr.py:
This is a module to read exr data from an exr file, in the form of "Red", "Green", and "Blue" channel. "Alpha" is not written yet.
To read exr file use:
read_exr(file_name)
The output is a numpy array of the three channels, accessible as indices.
output[0] = Red channel
output[1] = Green channel
output[2] = Blue channel
