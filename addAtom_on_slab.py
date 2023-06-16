# FCC (111) surface of platinum with absorbed N2
from ase.build import fcc111 , add_adsorbate , molecule
from ase.visualize import view

slab = fcc111('Pt', size=(4, 4, 4), a=4.0, vacuum=6.0)
#add_adsorbate(slab, molecule('N2'), height=3.0, position='ontop')
add_adsorbate(slab, molecule('N2'), height=3.0, offset=(1, 1), position='ontop')

view(slab)