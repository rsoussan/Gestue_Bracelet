import numpy as np
import mlpy

def compareData(in_file,lib_file):
	vector_index = ['arr_0','arr_1','arr_2']
	dist = 0
	total_dist = 0
	dists = []


	in_data = np.load(in_file)
	lib_data = np.load(lib_file)
	for j in range(0,3):
		a = in_data[vector_index[j]] 
		b = lib_data[vector_index[j]] 
		dist = 	mlpy.dtw_std(a,b,dist_only=True)
		total_dist += dist
		dists.append(dist)

	return (total_dist,dists)


