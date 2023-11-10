import logging
import os
import shutil
import subprocess as sp

from openbabel import pybel

logger = logging.getLogger(__name__)


def smiles_to_3d_structure(smiles: str, output: str):
    """
    Generate a 3D structure from a SMILES string using the UFF force field.

    Parameters:
        smiles (str): The SMILES representation of the molecule.
        output (str): The name of the output XYZ file.

    Returns:
        None
    """
    mymol = pybel.readstring("smi", smiles)
    mymol.addh()
    mymol.make3D(forcefield="UFF", steps=200)
    out = pybel.Outputfile("xyz", output, overwrite=True)
    out.write(mymol)
    out.close()


def smiles_to_3d_structure_alt(smiles: str, output: str, nconf: int = 500):
    """
    Generate a 3D structure from a SMILES string using the MMFF94 force field.

    Parameters:
        smiles (str): The SMILES representation of the molecule.
        output (str): The name of the output XYZ file.
        nconf (int): Number of conformers to generate.

    Returns:
        None
    """
    with open("tmp.smi", "w") as f:
        f.write(smiles)
    sp.call(
        [
            "obabel",
            "-ismi",
            "tmp.smi",
            "-oxyz",
            "-O",
            output,
            "--gen3d",
            "--conformer",
            "--nconf",
            str(nconf),
            "--score",
            "energy",
        ],
        stdout=sp.DEVNULL,
        stderr=sp.DEVNULL,
    )
    os.remove("tmp.smi")


def multiple_smiles_2_3D(smiles_list: list, species: str, method: str = "2"):
    """
    Generate 3D structures for a list of molecules using xtb module.

    Parameters:
        smiles_list (list of str): List of SMILES representations of molecules.
        species (str): The name of the species.
        method (str): Method for 3D structure generation (1 or 2).

    Returns:
        None
    """
    if not isinstance(smiles_list, list):
        raise TypeError("smiles_list must be a list")
    if not isinstance(species, str):
        raise TypeError("species must be a string")
    if method not in ["1", "2"]:
        raise ValueError("method must be either '1' or '2'")

    n_tot = len(smiles_list)
    logging.info(f"Reading {n_tot} SMILES strings")
    for n, smiles in enumerate(smiles_list):
        output = f"{species}_{n}.xyz"

        if method == "1":
            smiles_to_3d_structure(smiles, output)
        elif method == "2":
            smiles_to_3d_structure_alt(smiles, output)
        else:
            raise ValueError("method must be either '1' or '2'")
        print(f"Generated 3D for {smiles}. Progress: {n+1}/{n_tot}")
        n += 1


def xtb_opt(xyz, charge=0, unpaired_e=0, level=1):
    """
    Perform quick and reliable geometry optimization with xtb module
    Parameters:
    1. xyz: xyz file
    2. charge: (int)
    3. unpaired_e: number of unpaired electrons
    4. level: 0-2; Halmitonian level [gfn-1,2, gfnff], default=2

    Returns:
    none
    (filename_xtbopt.xyz)
    """

    execution = (
        ["xtb", "--gfnff", xyz, "--opt"]
        if level == 0
        else ["xtb", "--gfn", "1", xyz, "--opt"]
        if level == 1
        else ["xtb", "--gfn", "2", xyz, "--opt"]
    )
    if charge != 0:
        execution.extend(["--charge", str(charge)])
    if unpaired_e != 0:
        execution.extend(["--uhf", str(unpaired_e)])
    sp.call(execution, stdout=sp.DEVNULL, stderr=sp.STDOUT)

    name = xyz[:-4]

    if os.path.exists("xtbopt.xyz"):
        shutil.move("xtbopt.xyz", f"{name}_xtbopt.xyz")
    elif os.path.exists("xtblast.xyz"):
        shutil.move("xtblast.xyz", f"{name}_xtbopt.xyz")
    else:
        logger.info("xTB optimization failed")
