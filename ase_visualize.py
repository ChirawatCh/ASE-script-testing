import os
from ase.visualize import view
from ase.io import read, write
#atoms = read("CONTCAR", format='vasp')
atoms = read("CONTCAR", format='vasp')
view(atoms)

