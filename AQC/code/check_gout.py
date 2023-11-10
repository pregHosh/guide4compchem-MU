#!/usr/bin/env python

import argparse
import glob
import re

parser = argparse.ArgumentParser(description="Check the status of Gaussian log files")
parser.add_argument(
    "-d", "--dir", default=None, type=str, dest="directory", help="subdirectory"
)
args = parser.parse_args()


def extract_num(token):
    """Extracting a number from a line"""
    for word in token.split():
        try:
            return float(word)
        except ValueError as e:
            pass


sub_dir = args.directory
if sub_dir:
    print(f"Reading log files from the '{sub_dir}' subdirectory")
    all_log = glob.glob(f"{sub_dir}/*log")
else:
    print("Reading log files from the current directory")
    all_log = glob.glob("./*log")

done_opt = []
done_spc = []
fail = []
running = []

for log in all_log:
    with open(log, "r", encoding="utf-8") as f:
        contents = f.readlines()
        if "Normal termination of Gaussian" in contents[-1]:
            Freq_all = []
            SCF_Done_all = []
            job_type_spc = []

            for line in contents:
                if re.search("Frequencies", line):
                    Freq_all.append(extract_num(line))

                if re.search("SCF Done", line):
                    SCF_Done_all.append(extract_num(line))

                if re.search("scrf", line) or re.search("pop=nboread", line):
                    token = line.split(" ")
                    for item in token:
                        if ("scrf(" in item) or ("pop=nboread" in item):
                            job_type_spc.append(item)

            Freq_all = [Freq for Freq in Freq_all if Freq is not None]
            SCF_Done_all = [SCF_D for SCF_D in SCF_Done_all if SCF_D is not None]

            if len(Freq_all) > 0:
                name_file = log.split("/")[-1]
                done_opt.append(
                    f"{name_file}: opt/freq job\nLowest frequency = {Freq_all[0]}\nSCF Energy = {SCF_Done_all[-1]}"
                )
            else:
                name_file = log.split("/")[-1]
                job_type = " ".join(e for e in job_type_spc[:-1])
                done_spc.append(
                    f"{name_file}: {job_type}\nSCF Energy = {SCF_Done_all[-1]}"
                )

        elif "Error" in contents[-4]:
            fail.append(f"{log}: {contents[-5]}")
        else:
            running.append(log)

print("Normally terminated jobs:")
print("\nOpt/Freq jobs:")
[print(f"{j+1}. {i}\n") for j, i in enumerate(done_opt)]
[print("\n")]

print("\nSPC jobs:")
[print(f"{j+1}. {i}\n") for j, i in enumerate(done_spc)]
print("-------------------------\n")
print("\nFail jobs:")
[print(f"{j+1}. {i}\n") for j, i in enumerate(fail)]
print("-------------------------\n")
print("\nJobs running or ended abruptly:")
[print(f"{j+1}. {i}\n") for j, i in enumerate(running)]
