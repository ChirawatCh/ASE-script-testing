# Support 20 common surfaces: fcc100, fcc111, fcc110, fcc211, fcc221, fcc311, fcc322, fcc331, fcc332,
# bcc100, bcc111, bcc110, bcc210, bcc211, bcc310, hcp0001, hcp10m10t, hcp10m10h, hcp10m11, hcp10m12.
############################################################################################################
# Supported sites: the site type, support ‘ontop’, ‘bridge’, ‘longbridge’, ‘shortbridge’,
# ‘fcc’, ‘hcp’, ‘3fold’, ‘4fold’, ‘5fold’, ‘6fold’.
############################################################################################################
from acat.adsorption_sites import SlabAdsorptionSites
from ase.build import fcc110
from ase.build import bcc100
from ase.build import bcc110

from ase.visualize import view
atoms = fcc110('Ag', (4, 4, 4), vacuum=10., periodic=True)
atoms.center()
view(atoms)
sas = SlabAdsorptionSites(atoms, surface='fcc110',
                           allow_6fold=False,
                           composition_effect=True,
                           label_sites=True,
                           surrogate_metal='Cu') # Small cell: Cu, Large cell: Pd or Au
site = sas.get_site() # Use sas.get_sites() to get all sites
print(site)