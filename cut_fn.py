import ase
from ase.spacegroup import crystal
from ase.build import cut, root_surface
from ase.visualize import view
from ase.io.vasp import write_vasp

# Create an aluminium (111) slab with three layers
#
# First an unit cell of Al
a = 4.05
aluminium = crystal('Al', [(0,0,0)], spacegroup=225, cellpar=[a, a, a, 90, 90, 90])
# Then cut out the slab
al111 = cut(aluminium, (1,-1,0), (0,1,-1), nlayers=3 )

#view(al111)

slab = root_surface(al111 , 5)

view(slab)
write_vasp('POSCAR', slab)

