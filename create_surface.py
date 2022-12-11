from ase.build import surface, root_surface, fcc111
from ase.visualize import view
from ase.io.vasp import write_vasp

primitive_slab = fcc111('Fe', size=(1, 1, 4), a=3.9, vacuum=None, periodic=True)
slab = root_surface(primitive_slab , 13)

#view(primitive_slab)
#view(slab)
write_vasp('POSCAR', primitive_slab)
write_vasp('CONTCAR', slab)
