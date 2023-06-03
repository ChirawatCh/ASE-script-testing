from acat.adsorption_sites import SlabAdsorptionSites
from ase.visualize import view
from ase.io.vasp import write_vasp
from ase.io.vasp import read_vasp
from acat.build import add_adsorbate_to_site

name = "Au-fcc100-4x4"
atoms = read_vasp(name + "/POSCAR")
atoms.center()

sas = SlabAdsorptionSites(atoms, surface='fcc110', # Type of suface
                          allow_6fold=False,  # False to 6-fold sub-surface sites underneath fcc hollow sites.
                          composition_effect=False,  # False for monometallics, True for bimetallics
                          both_sides=False,  # Only consider sites on top of the slab.
                          label_sites=True, # Label site
                          surrogate_metal='Au')  # Small cell: Cu, Large cell: Pd or Au

# site = sas.get_site() # Return randim site
# sites = sas.get_sites() # Return all sites
usites = sas.get_unique_sites()  # Return unique sites
site_list = []
for site in usites:
    site_list.append(site['site'])
print("Unique sites:", len(usites), "sites", site_list)

for site in usites:
    atoms = read_vasp(name + "/POSCAR")
    atoms.center()
    if site['site'] == "ontop":
        add_adsorbate_to_site(atoms, adsorbate='H', height=1.5, site=site)
        write_vasp(name+'-H-ontop', atoms)
        view(atoms)
    elif site['site'] == "bridge":
        add_adsorbate_to_site(atoms, adsorbate='H', height=1.5, site=site)
        write_vasp(name+'-H-bridge', atoms)
        view(atoms)
    elif site['site'] == "4fold":
        add_adsorbate_to_site(atoms, adsorbate='H', height=1.5, site=site)
        write_vasp(name + '-H-4fold', atoms)
        view(atoms)


