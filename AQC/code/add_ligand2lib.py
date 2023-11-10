import argparse
import glob
import os
import shutil
import subprocess as sp

from rdkit import Chem


def find_directory(directory_name, start_path="/"):
    start_path = os.path.abspath(start_path)

    for root, dirs, _ in os.walk(start_path):
        if directory_name in dirs:
            return os.path.join(root, directory_name)

    return None


def add_lig2lib(xyz_file: str, ligand_atom: str) -> None:
    """
    Add a carbene ligand to the Aaron library.

    Args:
        xyz_file (str): The path to the XYZ file containing the carbene or phosphine ligand.
        ligand_atom (str): The atom symbol of the ligand (e.g., "C" (for carbene) or "P" (for phosphine)).

    Returns:
        None
    """

    with open(xyz_file) as file:
        content = file.readlines()

    new_content = content[1:3] + content[9:]

    with open("tmp.xyz", "w") as file:
        file.writelines(new_content)

    mol = Chem.MolFromMolFile("tmp.xyz")

    metal_atom = mol.GetAtomWithIdx(0)

    ligand = None
    for neighbor in metal_atom.GetNeighbors():
        if neighbor.GetSymbol() == ligand_atom:
            ligand = neighbor
            break

    m_idx = metal_atom.GetIdx()
    ligand_idx = ligand.GetIdx()

    sp.run(
        [
            "libaddSubstituent.py",
            "-n",
            str(xyz_file[:-4]),
            "-s",
            str(ligand_idx),
            "-a",
            str(m_idx),
            "-c",
            "1000",
            "2",
            "tmp.xyz",
        ],
        stderr=sp.DEVNULL,
        check=True,
    )

    os.remove("tmp.xyz")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Adding ligands to the Aaron library")
    parser.add_argument(
        "-i",
        "--input",
        default="NHC",
        type=str,
        dest="lig",
        help="ligand family (for example, NHC(default), P",
    )
    parser.add_argument(
        "-a",
        "--atom",
        default="C",
        type=str,
        dest="atom",
        help="ligand atom (default=C)",
    )
    parser.add_argument(
        "-p",
        "--path_aaron",
        default="/home/pregabalin/Aaron_libs/",
        type=str,
        dest="path_aaron_lib",
        help="path to Aaron library (default=/home/pregabalin/Aaron_libs/)",
    )

    args = parser.parse_args()
    lig_name = args.lig
    lig_atom = args.atom
    path_Aaron = args.path_aaron_lib

    lig_xyzs = glob.glob(f"{lig_name}*")
    lig_xyzs = sorted([nhc for nhc in lig_xyzs if "xyz" in nhc])

    for ligand in lig_xyzs:
        try:
            add_lig2lib(ligand, lig_atom)
            print(f"Added {ligand} to the library")
        except Exception as e:
            print(f"Cannot add {ligand} to library due to {e}")

    if not (os.path.exists(path_Aaron)) or path_Aaron is None:
        path_Aaron = find_directory("Aaron_libs", "/")

    all_xyz = glob.glob(f"{path_Aaron}*.xyz")

    subs_directory = os.path.join(path_Aaron, "Subs")

    for xyz_file in all_xyz:
        destination = os.path.join(subs_directory, os.path.basename(xyz_file))
        shutil.move(xyz_file, destination)
