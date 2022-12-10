# FeO film on Pt (111)
from ase.visualize import view
from ase.build import root_surface , fcc111 , stack
primitive_substrate = fcc111('Pt', size=(1, 1, 4), vacuum=2)
substrate = root_surface(primitive_substrate , 84)
primitive_film = fcc111('Fe', size=(1, 1, 2), a=3.9, vacuum=1)
primitive_film[1].symbol = 'O'
film = root_surface(primitive_film , 67)
interface = stack(substrate, film, fix=0, maxstrain=None)

view(interface)