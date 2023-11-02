# Guide for automated quantum-chemical calculations 


Basically, work smart (and hard at the same time).

Keep in mind, this is just how I do things. You may find your own way of doing things which might even be more efficient than mine.


I also assume you use Window10 or Window11 on your personal machine.

### What you need

1. WSL
2. Ubuntu 
3. Conda or Miniconda
4. Maybe code editor as well (e.g., VSCode, Sublime Text, Atom, etc.)

These should open up the possibility of cool stuffs you can do with your computer. These are cool stuffs you should definitely check out:

1. [xTB](https://xtb-docs.readthedocs.io/), [CREST](https://crest-lab.github.io/crest-docs/)
2. [Goodvibes](https://github.com/patonlab/GoodVibes)
3. [AaronTools](https://github.com/QChASM/AaronTools)
4. [Multiwfn on linux](http://sobereva.com/multiwfn/)
5. [Volcanic](https://github.com/lcmd-epfl/volcanic/) and [mikimo](https://github.com/lcmd-epfl/mikimo/)
6. etc.

### How to start

1. Install WSL and Ubuntu on your machine. You can find many tutorials on the internet yourselves, maybe use [this](https://www.youtube.com/watch?v=28Ei63qtquQ) one.

2. Install [Anaconda or Miniconda](https://www.anaconda.com/download#downloads) on your Ubuntu [Basically use the linux version], look up for the tutorial on how to do it yourselves.

3. After all these, you should be able to open the terminal by right-clicking on the folder and select *Open in Terminal*. Install my conda environment (in `suisei.yml` file) by running `conda env create -f environment.yml`

4. Activate the environment by running `conda activate suisei` or go to the .bashrc file and add `conda activate suisei` at the end of the file. This will automatically activate the environment when you open the terminal.

5. You can start using xTB, GoodVibes, Aarontools, and others after this. You can also install additional programs of your interest with conda or pip.

### Workflow example 1: Virtual Screening

1. Create a library of ligands, each represented as SMILES string.
2. Add ligands to the Aarontools library by converting all SMILES to xyz files with OpenBabel.
3. Prepare the template structures of intermediates and transition states whose ligands are to be replaced by those in the library.
4. Use Aarontools to generate structures of intermediates and transition states with ligands from the library from the template structures. 
5. Optimize (clean up) these structures with xTB for more efficient and (maybe faster) DFT geometry optimization later.
6. Have a code to generate input files for DFT geometry optimization (e.g., Gaussian, Orca, etc.) from the xTB-optimized structures.
7. Run DFT geometry optimization (most-time consuming part, nothing I can help here ¯\_(ツ)_/¯).
8. Use GoodVibes to automatically extract thermochemical data from the output files of DFT geometry optimization and single-point calculation.

From step 1-4, *you get to generate a lot of structures with different ligands with just a single line of command*. This is the power of automation. Again, I cannot help with the DFT part, but afterward, GoodVibes is your best friend by helping you extract the data you need from the output files of DFT calculation, again with just a single line of command.

You can also use Aarontools to extract optimized geometry coordinates from the output files of DFT calculation...maybe for the SI.

and then, maybe...

9. Construct molecular volcano plots/activity maps with a single line of command using volcanic or mikimo.

<span style="color:red">**If you organize the codes and stuffs well, besides for the DFT part, you will need perhaps 2-3 python files to do all of these and perhaps 3 lines of command.**</span>.

Of course, you can adapt this workflow to study the substrate scope as well.

### Workflow example 2: Finding TS quicker with xTB

1. Instead of performing PES scan with DFT, you can use xTB to find TS quicker (not always work but you can just try as it is computationally cheap to do anyway (~1-3 min)).
2. With the saddle-point structure from the xTB PES scan, you can use it as a starting point for DFT TS optimization later.