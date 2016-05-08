import numpy as np
import mlpy
from compareData import compareData

def compareLib(in_file, lib_name):
	n = 6;
	lib_dist = 0;
	lib_dists = np.ones((n-1,3))*(-1)
	for i in range(1,n):
		lib_file = lib_name + str(i) + ".npz"
		dist, dists = compareData(in_file,lib_file)
		lib_dist += dist
		lib_dists[i-1,:] = dists

	return(lib_dist,lib_dists)
	 
