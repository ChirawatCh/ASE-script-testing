from ase.io.vasp import write_vasp
from ase.visualize import view
from ase.build import fcc111
slab = fcc111('Al', size=(3,3,5), vacuum=10.0, periodic=True)
view(slab)
#write_vasp('POSCAR_Ag_fcc111', slab)