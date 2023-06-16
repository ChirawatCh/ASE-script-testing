# creates: io1.png io2.png io3.png

from ase import Atoms
from ase.build import fcc111, bcc100, add_adsorbate, molecule
from ase.io import write, read
from ase.visualize import view
from acat.adsorption_sites import SlabAdsorptionSites

adsorbate = Atoms('CO')
adsorbate[1].z = 1.1
a = 3.61
slab = bcc100('Ba', (2, 2, 5), a=a, vacuum=7.0)
slab = slab * (3, 3, 1)
# print(slab.get_all_distances())
# slab = read("POSCAR_Ag_fcc111", format='vasp')
# print(slab)
#slab.center(axis=(2))
sas = SlabAdsorptionSites(slab, surface='bcc100',
                           allow_6fold=False,
                           composition_effect=True,
                           label_sites=True)
usites = sas.get_unique_sites()  # Return unique sites
site_list = []
for site in usites:
    site_list.append(site['site'])
print("Unique sites:", len(usites), "sites", site_list)

#add_adsorbate(slab, molecule('NH3'), height=3.0, offset=(2, 2), position='ontop')


view(slab)
write('image1.png', slab )
# write('io1.png', slab * (3, 3, 1), rotation='10z,-80x')