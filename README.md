# python-modules
This is a collection of python modules that I use for simplifying my work.

fwhm.py:<br/>
This is a simple module for reading the full width at half/tenth maximum of a single peak, for a given dependent variable and independent variable.<br/>
To read FWHM use:<br/>
fwhm2(independent_variable, dependent_variable)<br/>
To read FWTM use:<br/>
fwtm2(independent_variable, dependent_variable)<br/>
The output is simple float number.<br/>

read_exr.py:<br/>
This is a module to read exr data from an exr file, in the form of "Red", "Green", and "Blue" channel. "Alpha" is not written yet.<br/>
To read exr file use:<br/>
read_exr(file_name)<br/>
The output is a numpy array of the three channels, accessible as indices.<br/>
output[0] = Red channel<br/>
output[1] = Green channel<br/>
output[2] = Blue channel
