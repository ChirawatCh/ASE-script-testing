import numpy as np
from ase import Atoms
from ase.neighborlist import NeighborList
from ase.visualize import view
from ase.io.vasp import read_vasp

# Read the VASP file and create an atoms object
atoms = read_vasp("Au-fcc111-4x4/H2/Au-fcc111-4x4-H2-ontop/POSCAR")

# # Define the atoms in your system
# atoms = Atoms('H3',
#               positions=[[0, 0, 0], [1, 1, 1], [2, 2, 2]],
#               cell=[10, 10, 10],
#               pbc=True)
# view(atoms)

# Define the cutoff distance
cutoffs = [1.0] * len(atoms)  # In this example, we set the cutoff to 1.0 Angstrom for all atoms

# Create the NeighborList object
nl = NeighborList(cutoffs, skin=0.3, sorted=False, self_interaction=False, bothways=False)

# Generate the neighbor list
nl.update(atoms)

# Get the neighbor indices for atom 0
atom_index = 1
indices, offsets = nl.get_neighbors(atom_index)

# Calculate bond distances
bond_distances = []
for neighbor_index, offset in zip(indices, offsets):
    neighbor_position = atoms.positions[neighbor_index] + np.dot(offset, atoms.get_cell())
    bond_distance = np.linalg.norm(neighbor_position - atoms.positions[atom_index])
    bond_distances.append(bond_distance)

print(f"Bond distances of atom {atom_index} with its neighbors:")
for neighbor_index, bond_distance in zip(indices, bond_distances):
    print(f"Neighbor index: {neighbor_index}, bond distance: {bond_distance:.3f} Angstrom")
