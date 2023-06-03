import ase
from ase.visualize import view
from ase.io.vasp import read_vasp

# Read the VASP file and create an atoms object
atoms = read_vasp("Au-fcc111-4x4/H2/Au-fcc111-4x4-H2-ontop/POSCAR")

# Visualize the atoms
#view(atoms)

# Print the number of atoms
print("Number of atoms: " + str(atoms.get_global_number_of_atoms()))

# List the index of "H" atoms
hydrogen_indices = [atom.index for atom in atoms if atom.symbol=='H']

# Print the hydrogen indices
print("H-H indices: ", hydrogen_indices)

# Print the distance between the 64th and 65th atom
print("H-H distance: ", atoms.get_distance(64,65))

# Sample indices atoms list
indices_list = [1, 63, 64]
# Print the distances between all "H" atoms and the 65th atom
print("Distances: ",atoms.get_distances(indices_list, 65))

