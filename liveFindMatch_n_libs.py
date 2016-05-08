from compareLib import compareLib
import sys
from getData_wireless import getData_wireless
import numpy as np

n = len(sys.argv) - 2
in_file = sys.argv[1]

lib_dist_V = np.ones(n)*-1
mins_M = np.ones((n,3))*-1
sum_mins_V = np.ones(n)*-1

# arg 1 is file name, 2 and 3 are lib prefixes (i.e. circle, rswipe)
x,y,z = getData_wireless()
np.savez(in_file, x,y,z)


for i in range(0,n):
	lib = sys.argv[i+2]
	lib_dist,lib_dists = compareLib(in_file,lib)
	mins = lib_dists.min(axis=0)
	sum_mins = sum(mins)

	lib_dist_V[i] = lib_dist
	mins_M[i,:] = mins
	sum_mins_V[i] = sum_mins

#index = sum_mins_V.index(min(sum_mins)) 
index = sum_mins_V.argmin(axis=0)
print sum_mins_V
print mins_M
print(sys.argv[index+2] + "!")


