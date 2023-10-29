# Guide for modern computational chemistry for Computational Chemistry Lab


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

4. Data analysis
    - statistics
    - data visualization
    - machine learning
    - deep learning

5. Chemoinformatics 
    - text representation of molecules: **SMILES**, SELFIES, InChI
    - molecular descriptors
    - molecular fingerprints
    - molecular similarity

### Practical stuff 

0. OS (that you will probably use)
    - Linux: 
        - WSL (Windows Subsystem for Linux)
        - Ubuntu (If you hate Windows)
        - CentOS (our servers)
    - Windows (preferably Windows 11)


1. Basic Linux commands
 
2. Quantum-chemical calculations, particularly
    - Gaussian16/09 
    - ORCA
    - GAMESS
3. Visualization of molecular structures and orbitals
    - GaussView 
    - Avogadro
    - VMD
    - Multiwfn
    - Jimp2
4. (optional) Pre- and post-processing of quantum-chemical calculations

5. (optinal) Coding skills
    - Code editors
        - Vim
        - Emacs
        - Notepad++
        - Visual Studio Code
        - PyCharm
    - Bash
    - Python (perhaps all you ever need)
        - Pip and conda
        - Numpy
        - Pandas
        - Matplotlib
        - Seaborn
        - Scikit-learn
        - SciPy
        - (advanced) PyTorch, TensorFlow, Jax
    - Git and GitHub for source code control
        - You should be able to use Git and GitHub to manage your source code and collaborate with others for reproducible and clean research.
        - and able to find stuffs (a lot of cool program as well as programming tutorial in Github) and install a package from GitHub.
    - (Advanced) Cython (C/C++ in Python)
    - (Advanced) Julia

### Quantum-chemical machine learning (QML)

1. Coding skills (refer to above)
2. Basis ML
    - Supervised learning/ Unsupervised learning/ Reinforcement learning
    - Regression/ Classification
    - Overfitting/ Underfitting
    - Feature engineering (feature selection, feature extraction): see [Molecular representation](#molrep) below
    - Data preprocessing (data cleaning, data normalization, data augmentation)
    - Data visualization (PCA, t-SNE, UMAP)
    - Algorithms
        - Linear regression
        - Logistic regression
        - Ensemble models: Random forest, XGBoost
        - Kernel methods: SVM, Gaussian process, Kernel ridge regression (KRR)
        - Neural network: MLP, CNN, RNN, LSTM, Transformer
        - Clustering: K-means, DBSCAN
        - Support vector machine
        - Dimensionality reduction: PCA, t-SNE, UMAP
    - Model evaluation: 
        - Cross-validation or Leave-one-out cross-validation
        - Metrics: R2, RMSE, MAE, accuracy, precision, recall, F1-score, ROC-AUC, PR-AUC, etc.   
    - Hyperparameter tuning (model selection)

(P.S. Most of the time, if you ever get to do QML, you will find yourself using molecular representation as below with Ensemble models and KRR)

#### Molecular representation
- Structure-based: SMILES, SELFIES, one-hot encoding, 1D/2D fingerprints
- Electronic structure-based (in QML/DScribe): 
    - Coulomb matrix (CM)
    - Bag of Bonds (BoB)
    - Smooth Overlap of Atomic Positions (SOAP)
    - SLATM ()
