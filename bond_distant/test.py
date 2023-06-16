from ase.visualize import view
from ase.io import read

atoms = read("POSCAR_Ag_fcc111", format='vasp')
view(atoms)