import numpy as np
from aocd import data

forest = np.genfromtxt(data.split('\n'), delimiter=1)
# pad edges with -1 so the real edge trees can be included in the analysis
forest = np.pad(forest, 1, constant_values=-1)

# test data
#forest=np.array([[3,0,3,7,3],[2,5,5,1,2],[6,5,3,3,2],[3,3,5,4,9],[3,5,3,9,0]])
#forest = np.pad(forest, 1, constant_values=-1)

# calculate maximum height cumulatively from each direction
# then visibility as trees which are > the max yet reached
northmax = np.maximum.accumulate(forest)
northvis = (forest[1:, :] > northmax[:-1, :])[:-1, 1:-1].astype(int)

southmax = np.maximum.accumulate(forest[::-1, :])[::-1, :]
southvis = (forest[:-1, :] > southmax[1:, :])[1:, 1:-1].astype(int)

westmax = np.maximum.accumulate(forest, axis=1)
westvis = (forest[:, 1:] > westmax[:, :-1])[1:-1, :-1].astype(int)

eastmax = np.maximum.accumulate(forest[:, ::-1], axis=1)[:, ::-1]
eastvis = (forest[:, :-1] > eastmax[:, 1:])[1:-1, 1:].astype(int)

visible = northvis | southvis | westvis | eastvis
print(visible.sum())