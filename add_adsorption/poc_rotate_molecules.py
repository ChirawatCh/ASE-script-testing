from acat.adsorption_sites import SlabAdsorptionSites
from acat.adsorption_sites import get_adsorption_site
from acat.build import add_adsorbate_to_site
from acat.utilities import get_mic
from ase.build import fcc111
from ase.visualize import view
atoms = fcc111('Pt', (4, 4, 4), vacuum=5.)
i, site = get_adsorption_site(atoms, indices=(54, 57, 58),
                               surface='fcc111',
                               return_index=True)
print(i)
print(site)
sas = SlabAdsorptionSites(atoms, surface='fcc111')
sites = sas.get_sites()
nbsites = sas.get_neighbor_site_list(neighbor_number=1)
print(nbsites)
nbsite = sites[nbsites[i][0]] # Choose the first neighbor site
print(nbsite)
print(site['position']), print(nbsite['position'])
ori = get_mic(site['position'], nbsite['position'], atoms.cell)
add_adsorbate_to_site(atoms, adsorbate='CH3OH', site=site,
                       orientation=ori)
#view(atoms)