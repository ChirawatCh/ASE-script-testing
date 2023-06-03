from acat.adsorption_sites import get_adsorption_site
from ase.build import fcc110
from ase.visualize import view

atoms = fcc110('Cu', (2, 2, 8), vacuum=5.)

print("Number of atoms: ", atoms.get_number_of_atoms())
# print(atoms)

for atom in atoms:
    if atom.index % 2 == 0:
        atom.symbol = 'Au'
atoms.center()

# for atom in atoms:
#     i = atom.index
#     p = atom.position[2]
#     s = atom.symbol
#     print("Symbol:{0}, index= {1}, Position in z-axix: {2}".format(s, i, p))

site = get_adsorption_site(atoms, (24, 29, 31),
                           surface='fcc110',
                           surrogate_metal='Cu')

# view(atoms)
print(site)
