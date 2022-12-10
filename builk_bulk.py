from ase.build import bulk, surface
from ase.visualize import view
Mobulk_bcc = bulk('Mo', 'bcc', a=3.16, cubic=True)
Mobulk_fcc = bulk('Mo', 'fcc', a=3.16, cubic=True)
s2 = surface(Mobulk_bcc, (1, 1, 1), 9, periodic=True)
s2.center(vacuum=10, axis=2)

view(s2)