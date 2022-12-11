from acat.adsorption_sites import get_adsorption_site
from ase.build import fcc110
from ase_visualize import view

atoms = fcc110('Cu', (2, 2, 8), vacuum=5.)
for atom in atoms:
     if atom.index % 2 == 0:
         atom.symbol = 'Au'
atoms.center()
site = get_adsorption_site(atoms, (24, 29, 31),
                            surface='fcc110',
                            surrogate_metal='Cu')
print(site)
view(atoms)

