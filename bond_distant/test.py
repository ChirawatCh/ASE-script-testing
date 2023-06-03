from ase import Atoms
from ase.neighborlist import NeighborList
from ase.visualize import view


def find_nearest_neighbor(atoms, index):
    neighbor_list = NeighborList(cutoffs=[cutoff_radius] * len(atoms), self_interaction=False, bothways=True)
    neighbor_list.update(atoms)
    indices, offsets = neighbor_list.get_neighbors(index)
    if len(indices) > 0:
        return indices[0], offsets[0]
    else:
        return None, None

# Define your atomic system
# symbols = ['H', 'O', 'O', 'H']
# positions = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 0]]
# atoms = Atoms(symbols=symbols, positions=positions)

from ase.io.vasp import read_vasp
# Read the VASP file and create an atoms object
atoms = read_vasp("Au-fcc111-4x4/H2/Au-fcc111-4x4-H2-ontop/POSCAR")
# view(atoms)

# Set the cutoff radius
cutoff_radius = 1.0

# Specify the atom index for which you want to find the nearest neighbor
atom_index = 64

# Find the nearest neighbor atom
nearest_neighbor_index, offset = find_nearest_neighbor(atoms, atom_index)

# Print the results
if nearest_neighbor_index is not None:
    print("Nearest neighbor atom index:", nearest_neighbor_index)
    print("Offset vector:", offset)
else:
    print("No nearest neighbor found.")
