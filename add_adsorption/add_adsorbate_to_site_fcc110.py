from acat.adsorption_sites import SlabAdsorptionSites
from ase.visualize import view
from ase.io.vasp import write_vasp
from ase.io.vasp import read_vasp
from acat.build import add_adsorbate_to_site

name = "slab/Au-fcc-110-1x1"
atoms = read_vasp(name + "/POSCAR")
#atoms.center()
view(atoms)

# name = "Au-fcc110-4x4"
# atoms = read_vasp(name + "/POSCAR")
# atoms.center()
#view(atoms)

# sas = SlabAdsorptionSites(atoms, surface='fcc110', # Type of suface
#                           allow_6fold=False,  # False to 6-fold sub-surface sites underneath fcc hollow sites.
#                           composition_effect=False,  # False for monometallics, True for bimetallics
#                           both_sides=False,  # Only consider sites on top of the slab.
#                           label_sites=True, # Label site
#                           surrogate_metal='Au')  # Small cell: Cu, Large cell: Pd or Au
