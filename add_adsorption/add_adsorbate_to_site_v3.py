# Support 20 common surfaces: fcc100, fcc111, fcc110, fcc211, fcc221, fcc311, fcc322, fcc331, fcc332,
# bcc100, bcc111, bcc110, bcc210, bcc211, bcc310, hcp0001, hcp10m10t, hcp10m10h, hcp10m11, hcp10m12.
############################################################################################################
# Supported sites: the site type, support ‘ontop’, ‘bridge’, ‘longbridge’, ‘shortbridge’,
# ‘fcc’, ‘hcp’, ‘3fold’, ‘4fold’, ‘5fold’, ‘6fold’.
############################################################################################################
import os
import shutil
import numpy as np
import ase
from acat.adsorption_sites import SlabAdsorptionSites
from ase.visualize import view
from ase.io.vasp import write_vasp
from ase.io.vasp import read_vasp
from acat.build import add_adsorbate_to_site
from acat.utilities import get_mic
from acat.adsorption_sites import get_adsorption_site
from ase.build import molecule

def add_adsorbate(folder_name, adsorbate):
    strings = folder_name.split("-")
    atoms = read_vasp(folder_name + "/POSCAR")
    atoms.center()
    sas = SlabAdsorptionSites(atoms, surface=strings[1],  # Type of surface
                              allow_6fold=False,  # False to 6-fold sub-surface sites underneath fcc hollow sites.
                              composition_effect=False,  # False for monometallics, True for bimetallics
                              both_sides=False,  # Only consider sites on top of the slab.
                              label_sites=True,  # Label site
                              surrogate_metal='Au')  # Small cell: Cu, Large cell: Pd or Au

    # site = sas.get_site() # Return random site
    sites = sas.get_sites() # Return all sites
    usites = sas.get_unique_sites()  # Return unique sites
    site_list = []
    for site in usites:
        site_list.append(site['site'])
    print("Unique sites:", len(usites), "sites", site_list)

    # create a dictionary that maps site['site'] values to functions
    site_functions = {
        'ontop': lambda atoms, site: add_adsorbate_to_site(atoms, adsorbate=adsorbate, site=site,
                       orientation=ori),
        'bridge': lambda atoms, site: add_adsorbate_to_site(atoms, adsorbate=adsorbate, site=site,
                       orientation=ori),
        'longbridge': lambda atoms, site: add_adsorbate_to_site(atoms, adsorbate=adsorbate, site=site,
                       orientation=ori),
        'shortbridge': lambda atoms, site: add_adsorbate_to_site(atoms, adsorbate=adsorbate, site=site,
                       orientation=ori),
        '3fold': lambda atoms, site: add_adsorbate_to_site(atoms, adsorbate=adsorbate, site=site,
                       orientation=ori),
        '4fold': lambda atoms, site: add_adsorbate_to_site(atoms, adsorbate=adsorbate, site=site,
                       orientation=ori),
        '5fold': lambda atoms, site: add_adsorbate_to_site(atoms, adsorbate=adsorbate, site=site,
                       orientation=ori),
        '6fold': lambda atoms, site: add_adsorbate_to_site(atoms, adsorbate=adsorbate, site=site,
                       orientation=ori),
        'fcc': lambda atoms, site: add_adsorbate_to_site(atoms, adsorbate=adsorbate, site=site,
                       orientation=ori),
        'hcp': lambda atoms, site: add_adsorbate_to_site(atoms, adsorbate=adsorbate, site=site,
                       orientation=ori)
    }


    # iterate over the list of sites and execute the appropriate function for each site['site'] value
    for site in usites:
        atoms = read_vasp(folder_name + "/POSCAR")
        atoms.center()
        site_function = site_functions.get(site['site'], None)
        # Create directory
        sub_foleder_name = folder_name + '-' + adsorbate + '-' + site['site']
        if not os.path.exists("{}/{}/{}".format(folder_name, adsorbate, sub_foleder_name)):
            os.makedirs("{}/{}/{}".format(folder_name, adsorbate, sub_foleder_name))
        # Create POSCAR file
        if site_function is not None:
            i, ad_site = get_adsorption_site(atoms, indices=(site['indices']),
                                          surface=strings[1],
                                          return_index=True)
            print(i)
            print(ad_site)
            nbsites = sas.get_neighbor_site_list(neighbor_number=1)
            #print(site)
            nbsite = sites[nbsites[i][1]]
            pos1 = np.array([0.0, 0.0, 0.0])
            # pos2 = np.array([0.5, 0.5, 0.0])
            pos2 = np.array([1.0, 1.0, 0.0])
            ori = get_mic(pos1, pos2, atoms.cell)
            #print(site['position'])
            #print(nbsite['position'])
            #ori = get_mic(site['position'], nbsite['position'], atoms.cell)
            site_function(atoms, site)
            write_vasp("{}/{}/{}/POSCAR".format(folder_name, adsorbate, sub_foleder_name), atoms)
            view(atoms)
        # Copy INCAR, KPOINTS
        shutil.copy("{}/INCAR".format(folder_name), "{}/{}/{}".format(folder_name, adsorbate, sub_foleder_name))
        shutil.copy("{}/KPOINTS".format(folder_name), "{}/{}/{}".format(folder_name, adsorbate, sub_foleder_name))


if __name__ == '__main__':
    folder_name = "Au-fcc111-4x4"
    add_adsorbate(folder_name, "N2")

