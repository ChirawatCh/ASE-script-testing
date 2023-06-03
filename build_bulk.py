from ase.build import bulk, surface
from ase.visualize import view
from ase.io.vasp import write_vasp
from ase.build import fcc100, fcc110, fcc111, bcc100, bcc110, bcc111, hcp0001

Mobulk_bcc = bulk('Mo', 'bcc', a=3.16, cubic=True)
Mobulk_fcc_cubic = bulk('Mo', 'fcc', a=3.16, cubic=True)
Mobulk_fcc_orthorhombic = bulk('Mo', 'fcc', a=3.16, orthorhombic=True)

s2 = surface(Mobulk_bcc, (1, 1, 1), 9, periodic=True)
s2.center(vacuum=10, axis=2)

slab = fcc111('Pd', size=(1, 1, 4), periodic=True)

view(slab)
# write_vasp('POSCAR_S2', s2)
# write_vasp('POSCAR_cubic', Mobulk_fcc_cubic)
# write_vasp('POSCAR_orthorhombic', Mobulk_fcc_orthorhombic)