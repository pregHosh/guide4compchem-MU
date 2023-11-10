#!/usr/bin/env python

import argparse
import glob
import shutil

parser = argparse.ArgumentParser(
    description="""
Create SCP jobs from opt/freq input file. \n
Replace the #opt freq line (first line of command, #) with {SCP_job} geom(check) guess(read) while retaining other settings (except for the level of theory if toggled)"""
)

parser.add_argument("-i", help="Input opt/freq pattern")
parser.add_argument("-all", help="Read all .gjf (default=n)", default="n")
parser.add_argument(
    "-j", help="Type of SCP job (solv/nbo/nbo_solv/TD-DFT/freq/spc and TS)"
)
parser.add_argument(
    "-d",
    "--dispersion",
    dest="dispersion",
    action="store_true",
    help="Flag to add Becke–Johnson Damping (D3-BJ)",
)
parser.add_argument(
    "-c",
    help="""Change the level of theory? (default=no), receive input as {functional}/{BS}
or {functional}/BS empiricalDispersion=...""",
    default="n",
)
parser.add_argument("-ncore", help="Change the number of cores")
parser.add_argument("--version", action="version", version="%(prog)s" + ": v5")
args = parser.parse_args()

spc_job = args.j
n_core = args.ncore
dispersion = args.dispersion

if args.all == "y":
    all_input = glob.glob("./*gjf")
    all_input.extend(glob.glob("./*gjf"))
    all_input.extend(glob.glob("./*inp"))
    print("Reading all input files")
else:
    all_input = glob.glob(f"{args.i}*")
    print("Reading ", all_input)
if len(all_input) == 0:
    print("No input files in the directory")


# Filtering out existing spc inputs
def filter_spc(inp):
    if "_solv" in inp:
        return False
    elif "_nbo" in inp:
        return False
    elif "_freq" in inp:
        return False
    elif "_spc" in inp:
        return False
    elif "_NboSolv" in inp:
        return False
    elif "_TDDFT" in inp:
        return False
    else:
        return True


all_input = list(filter(filter_spc, all_input))

for filename in all_input:
    print(filename)
    # Types of SCP
    if spc_job == "solv":
        solvent = input("Solvent: ")
        model = input("Solvent Model: ")
        cmd = f"#p geom(check) guess(read) scrf({model},solvent={solvent})"
    elif spc_job == "nbo":
        cmd = "#p geom(check) guess(read) pop=nboread"
    elif spc_job == "nbo_solv":
        solvent = input("Solvent: ")
        model = input("Solvent Model: ")
        cmd = f"#p geom(check) guess(read) pop=nboread scrf({model},solvent={solvent})"
    elif spc_job == "freq":
        cmd = "#p geom(check) guess(read) freq"
    elif spc_job == "TD-DFT":
        solvent = input("Solvent: ")
        model = input("Solvent Model: ")
        n_states = input("Number of states considered: ")
        cmd = f"#p geom(check) guess(read) td(singlets,nstates={n_states}) scrf({model},solvent={solvent})"
    else:
        cmd = "#p geom(check) guess(read)"

    if dispersion:
        cmd += " EmpiricalDispersion=GD3BJ"

    with open(filename, "r", encoding="utf-8") as f:
        content = f.readlines()

    if args.ncore:
        content[2] = (f"%CPU=0-{str(n_core-1)}\n",)

    content[0] = f"%chk={filename[:-4]}_{spc_job}\n"

    new_content = content[:3]
    new_content.append(cmd + "\n")

    x = 0
    for n, line in enumerate(content):
        token = line.split()
        for i in token:
            try:
                i = float(i)
            except Exception as e:
                token.remove(i)
        if len(token) == 3 and len(line.split()) == 4:
            x = n
            break

    if x == 0:
        print("No Cartesian coordinate data")
        for n, line in enumerate(content):
            token = line.split()
            for i in token:
                try:
                    i = float(i)
                except Exception as e:
                    token.remove(i)
        if len(token) == 2 and len(line.split()) == 2:
            x = n + 1
            break

    if args.c == "n":
        new_content.extend(content[4:x])
        new_content.append("\n")
    else:
        new_content.append(f"#p {args.c} gfinput scf=maxcycle=512\n")
        new_content.extend(content[5:x])
        new_content.append("\n")

    if spc_job == "ts":
        n = 0
        for i in content:
            try:
                if i[-2] == "F":
                    new_content.append(i[:-2] + "D\n")
                    n += 1
            except Exception as er:
                pass
        if n == 0:
            print("Warning, no modred detected in the input file")
        else:
            new_content.append("\n")

    try:
        sora = min([j for j, i in enumerate(content) if "****" in i]) - 2
        new_content.extend(content[sora:])
    except BaseException as err:
        print("No ECP data!")

    # NBO command line
    if spc_job == "nbo" or spc_job == "nbo_solv":
        new_content.extend(
            [
                "\n\n\n$NBO \n ARCHIVE\n ",
                "BNDIDX\n ",
                f"file={filename[2:-4]}_nbo\n$END \n\n\n\n",
            ]
        )
        
    if spc_job == "ts":
        shutil.move(filename, filename[:-4] + "_L.gjf")
        with open(filename, "w", encoding="utf-8") as f:
            print(f"Moved the original file to {filename[:-4]}_L.gjf")
            f.writelines(new_content)
    else:
        name_SCP = f"{filename[:-4]}_{spc_job}.gjf"
        with open(name_SCP, "w", encoding="utf-8") as f:
            f.writelines(new_content)
        try:
            shutil.copy(f"{filename[:-4]}.chk", f"{filename[:-4]}_{spc_job}.chk")
        except FileNotFoundError as e:
            print(f"Cannot find {filename[:-4]}.chk, make sure to copy {filename[:-4]}.chk" to f"{filename[:-4]}_{spc_job}.chk once it is available.")
