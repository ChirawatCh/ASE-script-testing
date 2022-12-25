from ase.build import bulk, surface
from ase.visualize import view
from ase.io.vasp import write_vasp

Mobulk_bcc = bulk('Mo', 'bcc', a=3.16, cubic=True)
Mobulk_fcc_cubic = bulk('Mo', 'fcc', a=3.16, cubic=True)
Mobulk_fcc_orthorhombic = bulk('Mo', 'fcc', a=3.16, orthorhombic=True)
s2 = surface(Mobulk_bcc, (1, 1, 1), 9, periodic=True)
s2.center(vacuum=10, axis=2)

#view(s2)
write_vasp('POSCAR_cubic', Mobulk_fcc_cubic)
write_vasp('POSCAR_orthorhombic', Mobulk_fcc_orthorhombic)