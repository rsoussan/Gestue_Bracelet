# Gestue_Bracelet
Autonomous Gesture Recognition Bracelet
Code for autonomous gesture recognition bracelet for COS 436 Human Computer Interaction final project.

# Project Description:
A bracelet using an Arduino to automatically recognize 5 unique gestures.  Sends accelerometer data from the bracelet to a client computer running our app that used the dynamic time warping algorithm to determine the gesture. Data is compared against a library of pre-recorded data and the gesture is determined using a nearest-neighbor algorithm.

# Python Dependencies:
numpy
scipy
pygsl
gsl
mlpy


# Description of files:
liveFindMatch_n_libs.py:
	reads data from bracelet and matches it with n libraries to find best match
	takes n libraries (each for different gesture) as arguments
	first argument is filename that input will be saved to
example:
	python liveFindMatch_n_libs.py test.npz counterc clockc upswipe 	downswipe rswipe lswipe
dependencies: compareLib, sys, getData_wireless, numpy

compareLib.py:
	takes in a file and a library name and returns the distances using a dwt (dynamic time-warping)	
	from the input to the library
dependencies: numpy, mlpy, compareData

compareData.py:
	takes in an input file and a single file from a library and computes the total 	distance (sum of all errors between input and lib file) and a vector of 
	distance values for x,y, and z axes
dependencies: numpy, mlpy

getData_wireless: reads data from the usb port for the xbee and returns x,y and
	z matrices for each accelerometer value
dependencies: serial, os, sys, numpy, serial.tools, time

# Videos of Bracelet in use:
Demo: https://www.youtube.com/watch?v=7P9_5Gr0QCA&feature=youtu.be

Bracelet Design: https://www.youtube.com/watch?v=BYHNV_khiv0

