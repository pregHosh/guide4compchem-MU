import argparse
import glob
import os

from smiles_2_3d_fun import multiple_smiles_2_3D, xtb_opt


def generate_3d_structure_from_smiles(
    smiles_txt, name, optimize_xtb, level, keep_ff_xyz
):
    """
    Generate 3D structures from SMILES strings and optionally perform xtb optimization.

    Parameters:
        smiles_txt (str): Path to a file containing SMILES strings.
        name (str): Name of the species.
        optimize_xtb (str): Perform xtb optimization (y/n, default: n).
        level (str): Hamiltonian level (0, 1, 2, default: 2).
        keep_ff_xyz (str): Keep force-field XYZ files (y/n, default: n).

    Returns:
        None
    """
    # Read SMILES strings from the input file
    with open(smiles_txt, "r", encoding="utf-8") as f:
        all_smiles = f.readlines()

    all_smiles = [
        smiles.split(" ")[0].replace("\n", "")
        for smiles in all_smiles
        if smiles.strip()
    ]
    all_smiles = list(filter(None, all_smiles))

    # Generate 3D structures from SMILES
    multiple_smiles_2_3D(all_smiles, name)
    print("3D structures generated from SMILES.")

    # Perform xtb geometry optimization for XYZ files
    if optimize_xtb == "y":
        print("Performing xtb optimization.")
        all_xyzs = glob.glob("./*xyz[!xtbopt]*")

        ntot = len(all_xyzs)
        for n, xyz in enumerate(all_xyzs, start=1):
            try:
                if level == "0":
                    xtb_opt(xyz, level=0)
                elif level == "1":
                    xtb_opt(xyz, level=1)
                elif level == "2":
                    xtb_opt(xyz)
                print(f"xtb optimization for {xyz} in progress: {n}/{ntot}")
            except Exception as e:
                print(f"xtb failed to optimize {xyz} due to {e}")

        if keep_ff_xyz == "n":
            print("Removing all force-field geometry files.")
            _ = [os.remove(xyz) for xyz in all_xyzs]


if __name__ == "__main__":
    # Instantiate the argument parser
    parser = argparse.ArgumentParser(description="Generate 3D structure from SMILES")
    parser.add_argument(
        "-s",
        "--smi",
        type=str,
        dest="smiles_path",
        default="smiles.txt",
        help="Path to a file containing SMILES strings",
    )
    parser.add_argument(
        "-n",
        "--name",
        type=str,
        dest="species_name",
        default="hoshiyomi",
        help="Name of the species",
    )
    parser.add_argument(
        "-o",
        "--opt",
        action="store_true",
        dest="xtb_opt",
        help="Perform xtb optimization? (y/n, default: n)",
        default="n",
    )
    parser.add_argument(
        "--l",
        "--level",
        type=int,
        dest="level",
        default=2,
        help="Hamiltonian level (0, 1, 2, default: 2)",
    )
    parser.add_argument(
        "-k",
        "--keep",
        action="store_true",
        dest="keep_ff_xyz",
        help="Keep the force-field XYZ files? (y/n, default: n)",
        default="n",
    )

    # Parse the command line arguments
    args = parser.parse_args()
    smiles_file = args.smiles_path
    species_name = args.species_name
    xtb_opt = args.xtb_opt
    level = args.level
    keep_ff_xyz = args.keep_ff_xyz

    # Call the function to generate 3D structures and perform xtb optimization
    generate_3d_structure_from_smiles(
        smiles_file, species_name, xtb_opt, level, keep_ff_xyz
    )
