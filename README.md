# Guide for modern computational chemistry for Computational Chemistry Lab

Welcome to the Compchem@MU! You will be working under Prof. Panida for here on. Trust me, she is a kind-soul and you will not find yourself under a better supervisor. 

You will also get a lot of opportunities to collaborate with others, inside and outside the university as she has a pretty good networking. Particularly, with the Japaneses, under the Sakura exchange program and others. So if you are a degerate weeb like myself, again, there is no better advisor than her.

***DISCLAMER*** You don't need to know everything below. Essentially, being able to perform first-principle calculations (mostly DFT) is enough to conduct a research in this group. Although, the advanced topics are highly recommended if you want to go above and beyond, **particularly knowing how to code to automate your routine tasks**. In this age of digitalization and the rise of big data and ML, you will find these advanced topics creeping into your realm of study. Also, it is just more elegant to work more efficiently by having automated workflow/pipeline in your projects.


## How to use this guide

Essential stuffs are on the main page here.

For the advanced topics, you can find them in the respective folders.
- `coding`: coding skills
- `quantum_machine_learning`: quantum-chemical machine learning
- `chem_design`: chemical design
- `AQC`: automated quantum-chemical calculations


## General research topics 

### 1. Homogenous catalytic reactions:
- Mechanistic study of catalytic reactions: to reveal the free energy profile   
- Electronic structure elucidation: to rationalize the reactivity and selectivity
- Catalyst design and substrate scope
    - virtual screening over a library of catalysts or substrates
    - machine learning 
    - exploration of chemical compound space 

### 2. Photochemical and photophysical properties
Mostly collaboration with experimentalists to validate their experimental results and to provide a theoretical explanation.


## Typical Quantum-Chemical Calculations


**DFT calculation**
- Geometry optimization
- Frequency calculation
- Single point energy calculation
- Transition state search
    - saddle point optimization
    - QST2/QST3
    - IRC calculation
- TD-DFT calculation
- NBO analysis
- Energy decomposition analysis

**Semiempirical Tight Binding (xTB)**
With xTB, you can obtain a better guess geometry for optimization at DFT later, possible making the calculation more efficient. You can also do various stuffs with xTB, such as


## Essential Skills and Knowledge

### Theory stuff
1. Basic theoretical background behind the electronic structure methods and able to apply a right method to a specific problem
    - Hartree-Fock theory
    - Density functional theory
    - Post-HF methods
        - Moller-Plesset perturbation theory (MP)
        - Coupled cluster theory (CC)
        - Configuration interaction theory (CI)
        - Complete active space self-consistent field theory (CASSCF)
        - Complete active space second-order perturbation theory (CASPT2)
    - Basis set
    - Semiempirical methods
    - Solvation models

2. Theoretical background and ability to apply electronic wavefunction analysis methods
    - Natural bond orbital (NBO) analysis
    - Energy decomposition analysis (EDA)
    - Quantum theory of atoms in molecules (QTAIM)
    - and many more (please refer to [Multiwfn](http://sobereva.com/multiwfn/))])

3. Chemistry
    - organic chemistry: structure and reactivity
    - organometallic chemistry
    - catalysis

4. Data science (optional, advanced topic, see `quantum_machine_learning` folder for more detail)

5. Chemoinformatics (optional, advanced topic, see `quantum_machine_learning` folder for more detail)

6. Chemical design (optional, advanced topic, see `chem_design` folder for more detail)


### Practical stuff 

0. OS (that you will probably use)
    - Linux: 
        - WSL (Windows Subsystem for Linux)
        - Ubuntu (If you hate Windows)
        - CentOS (our servers)
    - Windows (preferably Windows 11)


1. Basic Linux commands
 
2. Quantum-chemical calculations, particularly
    - **Gaussian16/09** (most used, household program here) 
    - ORCA (used sometimes, CASSCF, CASPT2, complicate spin stuffs)
    - GAMESS (for NEDA)
3. Visualization of molecular structures and orbitals
    - ArgusLab/Molden
    - GaussView 
    - Avogadro
    - VMD
    - Multiwfn
    - Jimp2
4. Pre- and post-processing of quantum-chemical calculations (optional, see `AQC` folder)

5. Coding skills (optional, see `coding` folder)

6. Presentation skills
    - Sadly, people would rarely care about your work, so you need to steal their attention.
    - please use LaTex more [Overleaf](https://www.overleaf.com/), better for collaboration, more elegant and all. Nowadays, it has become much easier also. (Well, except you are working with the experimentalists)
    - able to make attention-grabbing figures
        - [matplotlib](https://matplotlib.org/) and [seaborn](https://seaborn.pydata.org/)
        - [Inkscape](https://inkscape.org/) or others
        - [Blender](https://www.blender.org/)

## Resource

### Quantum-chemical calculations
- [Computational Chemistry from Laptop to HPC](https://kthpanor.github.io/echem/docs/title.html)
- [Best-Practice DFT Protocols for Basic Molecular Computational Chemistry](https://onlinelibrary.wiley.com/doi/full/10.1002/ange.202205735)
- [Perspective: Fifty years of density-functional theory in chemical physics](https://pubs.aip.org/aip/jcp/article/140/18/18A301/149389/Perspective-Fifty-years-of-density-functional)
- [Jacob’s ladder of density functional approximations for the exchange-correlation energy](https://pubs.aip.org/aip/acp/article-abstract/577/1/1/573973/Jacob-s-ladder-of-density-functional?redirectedFrom=fulltext)
- [A Chemist's Guide to Density Functional Theory](https://onlinelibrary.wiley.com/doi/book/10.1002/3527600043)
- Modern Quantum Chemistry


### Electronic wavefunction analysis methods
- [Multiwfn](http://sobereva.com/multiwfn/): read the manual which contains both theory and practical stuffs
- Read NBO tutorial [here](https://nbo6.chem.wisc.edu/nboman.pdf)
- [What is NBO analysis and how is it useful?](https://www.tandfonline.com/doi/full/10.1080/0144235X.2016.1192262?casa_token=14eEfX6HHpoAAAAA%3AchCGBsbKa7NuSj0FhYhZLysHmXKS6ZT198SNbBKBJTQDPRuS4DEEsygq2g8iRCOx0mSTWEOlON3w)
- [](https://onlinelibrary.wiley.com/doi/abs/10.1002/jcc.23060?casa_token=ad9kysiure4AAAAA:PcD8PKSpylgmrf4ZJB8XHwj7SR_pU9LsrLKx-C_X_TwewsRl6cCAZs8T9u5MbFO5taO0mNb0YcGp-hM)
- [The Quantum Theory of Atoms in Molecules: From Solid State to DNA and Drug Design](https://onlinelibrary.wiley.com/doi/book/10.1002/9783527610709)
