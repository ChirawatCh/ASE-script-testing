import csv
from ase.io import read


def measure_bond_distances(filename, rows, element):
    atoms = read(filename, format='vasp')

    # List the index of all atoms
    all_atom_list = [atom.index for atom in atoms]

    # List atom symbol
    element_symbol_list = [atom.symbol for atom in atoms]

    # List the index of specific element
    specific_element_list = [atom.index for atom in atoms if atom.symbol == element]

    # Calculate bond distances
    bond_distances = []
    for specific_index in specific_element_list:
        for atom_index in all_atom_list:
            if atom_index != specific_index:
                distance = atoms.get_distance(specific_index, atom_index)
                symbol1 = element_symbol_list[specific_index]
                symbol2 = element_symbol_list[atom_index]
                bond_distances.append((specific_index, atom_index, f"{symbol1}-{symbol2}", f"{distance:.3f}"))

    # Sort bond distances by distance
    bond_distances.sort(key=lambda x: float(x[3]))

    # Print and save the 10 shortest bond distances
    print("Shortest bond distances from", element, "element")
    for i, (specific_index, atom_index, bond_symbols, distance) in enumerate(bond_distances[:rows]):
        print(f"Bond distance {i + 1}: Atom {specific_index} - Atom {atom_index} ({bond_symbols}): {distance} Å")

    # Save the 10 shortest bond distances in CSV format
    with open("bond_distances.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Atom 1", "Atom 2", "Bond Symbols", "Distance"])
        writer.writerows(bond_distances[:rows])


if __name__ == '__main__':
    filename = "Au-fcc111-4x4/H2/Au-fcc111-4x4-H2-ontop/POSCAR"
    element = "H"
    rows = 10

    measure_bond_distances(filename, rows, element)
