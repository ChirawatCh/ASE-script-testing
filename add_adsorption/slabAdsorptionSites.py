from acat.adsorption_sites import SlabAdsorptionSites
from ase.visualize import view
from ase.io.vasp import read_vasp

atoms = read_vasp("Au-fcc100-4x4/POSCAR")
atoms.center()
# view(atoms)

sas = SlabAdsorptionSites(atoms, surface='fcc100',
                          allow_6fold=False, # False to 6-fold subsurf sites underneath fcc hollow sites.
                          composition_effect=False, # False for monometallics
                          both_sides=False, # Only consider sites on top of the slab.
                          label_sites=True,
                          surrogate_metal='Au') # Small cell: Cu, Large cell: Pd or Au
# sites = sas.get_site() # Use sas.get_sites() to get all sites

sites = sas.get_unique_sites() # Get unique sites

print(sites)
print(len(sites))