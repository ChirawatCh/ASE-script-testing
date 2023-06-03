import numpy as np
from acat.utilities import get_mic

# Define two positions in Cartesian coordinates
pos1 = np.array([0.0, 0.0, 0.0])
pos2 = np.array([1.0, 1.0, 0.0])

# Define the cell vectors in Cartesian coordinates
cell = np.array([[10.0, 0.0, 0.0], [0.0, 10.0, 0.0], [0.0, 0.0, 10.0]])

# Calculate the minimum image convention (MIC) vector between the two positions
mic = get_mic(pos1, pos2, cell)

print("Minimum image convention vector:", mic)
