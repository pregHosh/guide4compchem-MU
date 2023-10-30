# Guide for modern computational chemistry for Computational Chemistry Lab

Welcome to the Compchem@MU! You will be working under Prof. Panida for here on. Trust me, she is a kind-soul and you will not find yourself under a better supervisor. 

You will also get a lot of opportunities to collaborate with others, inside and outside the university as she has a pretty good networking. Particularly, with the Japanese, under the Sakura exchange program and others.

***DISCLAMER*** You don't need to know everything below. Essentially, being able to perform first-principle calculations (mostly DFT) is enough to conduct a research in this group. Although, the advanced topics are highly recommended if you want to go above and beyond, particularly in this age of digitalization and the rise of big data and ML. Also, it is more elegant to work more efficiently by having automated workflow/pipeline in your projects.

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
    - basis set

2. Theoretical background and ability to apply electronic wavefunction analysis methods
    - Natural bond orbital (NBO) analysis
    - Energy decomposition analysis (EDA)
    - and many more (please refer to [Multiwfn](http://sobereva.com/multiwfn/))])

3. Chemistry
    - organic chemistry: structure and reactivity
    - organometallic chemistry
    - catalysis

4. Data science (optional, advanced topic, see `quantum_machine_learning` folder for more detail)

5. Chemoinformatics (optional, advanced topic, see `quantum_machine_learning` folder for more detail)


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

