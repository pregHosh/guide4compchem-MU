#!/usr/bin/env python

import argparse
import glob
import sys

#TODO polish argparse
#TODO allow for not specifying ncore
#TODO polish ts
#TODO allow for reading xyz from other directories
#TODO allow for moving generated files to other directories
parser = argparse.ArgumentParser(
    description="Generating Gaussian input files from XYZ files"
)
parser.add_argument("-i", "--input", help="XYZ file")
parser.add_argument(
    "-j", "--job", help="Type of job (ts/int/f/spc) (default=int)", default="int"
)
parser.add_argument(
    "-all",
    "--all",
    help="All XYZ files in the directory? (default=no) (y/n)",
    default="n",
)
parser.add_argument("-chk", help="Include CHK file? (default=y)", default="y")
parser.add_argument("-ncore", help="Number of cores (default=24)", default="24")
parser.add_argument(
    "-f", "--functional", help="Functional (default=wb97xd)", default="wb97xd"
)
parser.add_argument(
    "-d",
    "--dispersion",
    dest="dispersion",
    action="store_true",
    help="Flag to add Becke–Johnson Damping (D3-BJ)",
)
parser.add_argument("-b", help="Basis set (default=def2SVP)", default="def2SVP")
parser.add_argument("-solv", help="Include solvent model? (default=y)", default="n")
parser.add_argument("-sm", help="Solvent model (default=SMD)", default="SMD")
parser.add_argument("-s", help="Solvent (default=toluene)", default="toluene")
parser.add_argument("-c", help="Charge (default=0)", default="0")
parser.add_argument("-m", help="Multiplicity (default=1)", default="1")
parser.add_argument("-nbo", help="NBO calculation? (default=n) (y/n)", default="n")
parser.add_argument("-t", help="Temperature (default=298.15)", default="298.15")

args = parser.parse_args()
dispersion = args.dispersion

if args.all == "y":
    all_xyz = glob.glob("./*xyz")
    print("Reading all XYZ files")
else:
    all_xyz = glob.glob(f"{args.i}*")
    print("Reading", all_xyz)

if len(all_xyz) == 0:
    sys.exit("No XYZ files in the directory")

#TODO polish the name
for strc in all_xyz:
    with open(strc, "r") as f:
        content_xyz = f.readlines()

    n_tot = int(content_xyz[0])
    xyz = content_xyz[2 : n_tot + 2]

    if args.j == "f":
        name = strc[:-4] + "_freq." + "gjf"
    elif args.j == "ts2":
        name = strc[:-4] + "_L." + "gjf"
        name_full = strc[:-3] + "gjf"
    else:
        name = strc[:-3] + "gjf"

    n_core = int(args.ncore)
    functional = args.f
    basis_set = args.b
    solvent_model = args.sm
    solvent = args.s
    charge = args.c
    multiplicity = args.m

    if args.j == "int":
        top = [
            f"%mem=30GB\n",
            f"%CPU=0-{str(n_core-1)}\n",
            f"#p opt freq\n",
        ]
    elif args.j == "ts":
        print("Direct full TS optimization")
        top = [
            f"%mem=30GB\n",
            f"%CPU=0-{str(n_core-1)}\n",
            f"#p opt(noeigentest,ts,calcfc,modred) freq\n",
        ]
        print("Manually add modred later")
    elif args.j == "ts2":
        print("Constraint optimization then full TS optimization")
        top = [
            f"%mem=30GB\n",
            f"%CPU=0-{str(n_core-1)}\n",
            f"#p opt(loose,modred) freq\n",
        ]
        top2 = [
            f"%mem=30GB\n",
            f"%CPU=0-{str(n_core-1)}\n",
            f"#p opt(ts,noeigentest,readfc,nofreeze,modred) freq geom=check guess=read\n",
        ]
        print("Manually add modred later")
    elif args.j == "f":
        top = [
            f"%mem=30GB\n",
            f"%CPU=0-{str(n_core-1)}\n",
            f"#p freq\n",
        ]
    elif args.j == "spc":
        top = [
            f"%mem=30GB\n",
            f"%CPU=0-{str(n_core-1)}\n",
        ]
    else:
        sys.exit("Invalid job type (int, ts, ts2, f, spc")

    if dispersion:
        top.extend(
            [
                f"#p gfinput scf=maxcycle=512 temperature={args.t} {functional}/{basis_set} EmpiricalDispersion=GD3BJ\n",
                "\n",
            ]
        )
    else:
        top.extend(
            [
                f"#p gfinput scf=maxcycle=512 temperature={args.t} {functional}/{basis_set}\n",
                "\n",
            ]
        )

    if args.solv == "y":
        top[2] = top[2][:-1] + f"scrf({solvent_model}, solvent={solvent})\n"

    if args.nbo == "y":
        top[2] = top[2][:-1] + " pop=nboread\n"

    if args.chk == "y":
        top.insert(0, f"%chk={strc[2:-3]}chk\n")

    with open(name, "w") as f:
        f.writelines(top)
        f.write("Suichan wa~! Kyou mo kawaii!\n\n")
        f.write(f"{charge} {multiplicity}\n")
        for line in xyz:
            f.write(line)
        f.write("\n\n\n\n")

        if args.nbo == "y":
            nbo_line = [
                "$NBO\n",
                "   ARCHIVE\n",
                f"  file={strc[0:-4]}\n",
                "$END\n\n\n",
            ]
            f.writelines(nbo_line)

    if args.j == "ts2":
        with open(name_full, "w") as f:
            top2.insert(0, f"%chk={strc[2:-3]}chk\n")
            f.writelines(top2)
            f.write("Suichan wa~! Kyou mo kawaii!\n\n")
            f.write(f"{charge} {multiplicity}\n\n\n\n\n")

print("Done, peko!")
