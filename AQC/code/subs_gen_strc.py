import argparse
import glob
import logging
import os
import subprocess as sp

from AaronTools.geometry import Geometry
from smiles_2_3d_fun import xtb_opt


def add_carbene_template(template: str, new_L: str, M: str) -> None:
    """
    Replace the carbene in the template with a new carbene ligand.

    Args:
        template (str): Path to the template XYZ file.
        new_L (str): Name of the new carbene ligand.
        M (str): Metal center (e.g., Ni, Pd, Pt).

    Returns:
        None
    """
    geom = Geometry(template)
    M_all = geom.find(M)

    # Detecting carbon atoms connected to the metal center
    MLc = []
    for M in M_all:
        for i in M.connected:
            if i.element == "C" or i.element == "P":
                MLc.append(i)

    carbene_all = []
    for Lc in MLc:
        n = 0
        for i in Lc.connected:
            if i.element == "N":
                n += 1
        if n == 2 or Lc.element == "P":
            carbene_all.append(Lc)

    carbene_all = list(set(carbene_all))

    for carbene in carbene_all:
        try:
            geom.substitute(new_L, carbene, minimize=True, attached_to=M_all[0])
        except Exception as e:
            geom.substitute(new_L, carbene, minimize=True, attached_to=M_all[1])

    geom.write(outfile=f"{template[:-4]}_{new_L}.xyz")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create 3D structures by replacing the carbene ligand in a template."
    )
    parser.add_argument("-t", help="Template (containing Carbene ligand)")
    parser.add_argument(
        "-v",
        help="Text file containing names of new ligands (default=HDF_L.txt)",
        default="HDF_L.txt",
    )
    parser.add_argument("-m", help="Metal center (default=Ni)", type=str, default="Ni")
    parser.add_argument("-c", help="Charge", type=int, default=0)
    parser.add_argument("-u", help="Unpaired electron", type=int, default=0)
    parser.add_argument("-o", help="XTB optimization? (y/n, default: n)", default="n")
    parser.add_argument(
        "-k", help="Toggle to discard the original structure", action="store_true"
    )

    args = parser.parse_args()
    template = args.t
    metal_center = args.m
    optimize_flag = args.o
    charge = args.c
    unpaired_e = args.u
    keep_ff = args.k

    with open(args.v) as f:
        all_L = f.read().splitlines()

    for ligand in all_L:
        print(f"Replacing carbene in {template} with {ligand}")
        add_carbene_template(template, ligand, metal_center)

    all_variation = glob.glob(f"{template[:-4]}_*.xyz")

    if optimize_flag == "y":
        logging.info("Optimizing all generated geometries with xtb")
        for species in all_variation:
            try:
                xtb_opt(species, level=2, charge=charge, unpaired_e=unpaired_e)
                logging.info(f"{species} successfully optimized")
            except Exception as e:
                logging.error(f"{species} failed to optimize due to {e}")

        if keep_ff:
            print("Deleting the FF structure and the template")
            all_opt_xyz = glob.glob("*xtbopt.xyz")
            for opt_xyz in all_opt_xyz:
                os.rename(opt_xyz, opt_xyz[:-11] + ".xyz")

    if os.path.exists("clean.sh"):
        sp.call("./clean.sh", shell=True)
