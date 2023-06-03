from acat.adsorption_sites import enumerate_adsorption_sites
from ase.cluster import Decahedron
from ase.visualize import view


atoms = Decahedron('Pd', p=3, q=2, r=1)
for atom in atoms:
    if atom.index % 2 == 0:
        atom.symbol = 'Ag'
atoms.center(vacuum=5.)
#view(atoms)

sites = enumerate_adsorption_sites(atoms, surface='fcc100',
                                   composition_effect=True,
                                   surrogate_metal='Pd')
print(sites[0])