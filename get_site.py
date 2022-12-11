from acat.adsorption_sites import SlabAdsorptionSites
from ase.build import fcc211
from ase.visualize import view
atoms = fcc211('Cu', (3, 3, 4), vacuum=5.)
atoms.center()
sas = SlabAdsorptionSites(atoms, surface='fcc211',
                           allow_6fold=False,
                           composition_effect=True,
                           label_sites=True,
                           surrogate_metal='Cu')
site = sas.get_sites() # Use sas.get_sites() to get all sites
print(len(site))
print(site[0])
#view(atoms)