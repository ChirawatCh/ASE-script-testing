from ase.build import surface, root_surface, fcc111
from ase.visualize import view
from ase.io.vasp import write_vasp

primitive_slab = fcc111('Fe', size=(1, 1, 2), a=3.9, vacuum=10, periodic=True)
slab = root_surface(primitive_slab , 36)

view(slab)
write_vasp('POSCAR', slab)