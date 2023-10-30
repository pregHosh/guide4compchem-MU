## Quantum-chemical machine learning (QML)


## Some theory stuffs

1. Data science
    - statistics
    - data visualization
    - machine learning
    - deep learning

2. Chemoinformatics 
    - text representation of molecules: **SMILES**, SELFIES, InChI
    - molecular descriptors
    - molecular fingerprints
    - molecular similarity

3. Quantum machine learning
    - representing molecules 
        - properties for molecular representation: unique, invariant, computationally efficient, and differentiable
        - text-based: SMILES, SELFIES, InChI
        - molecular graph
        - molecular descriptors
        - molecular fingerprints
        - electronic-structure-based (using 3D information)
    - machine learning
    - deep learning
    

## Practical stuffs
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
- molecular descriptor: (e.g., molecular weight, number of atoms, number of bonds, number of rings, etc. )
- Structure-based: SMILES, SELFIES, one-hot encoding, 1D/2D fingerprints
- Electronic structure-based (in QML/DScribe): 
    - Coulomb matrix (CM)
    - Bag of Bonds (BoB)
    - Smooth Overlap of Atomic Positions (SOAP)
    - Spectrum of London and Axillrod-Teller-Muto potential (SLATM) and the local (atomic) version of which (aSLATM)\
    - FCHL

- Benchmark dataset
    - QM9/QM7/QM7b

To read more about molecular representation
- [Molecular representations for machine learning applications in chemistry](https://onlinelibrary.wiley.com/doi/10.1002/qua.26870#:~:text=A%20molecular%20representation%2C%20also%20known,chemical%20composition%20and%20atomic%20configuration.)
- [A review of molecular representation in the age of machine learning](https://wires.onlinelibrary.wiley.com/doi/full/10.1002/wcms.1603?_gl=1*tq4t6z*_gcl_au*NjcxODk4NTkwLjE2OTYyMjI4MTM.)
- [Physics-Inspired Structural Representations for Molecules and Materials](https://pubs.acs.org/doi/10.1021/acs.chemrev.1c00021)
- [Quantum machine learning using atom-in-molecule-based fragments selected on the fly (SLATM)](https://www.nature.com/articles/s41557-020-0527-z)
- [SPAHM: the spectrum of approximated Hamiltonian matrices representations](https://pubs.rsc.org/en/content/articlelanding/2022/dd/d1dd00050k)

## Resource

### Machine learning

1. Check out Coursera (particularly, Andrew Ng), Youtube, and so on yourselves.
2. Very comprehensive ML (no need to learn all, just pick what you need in your project) [here](https://github.com/ujjwalkarn/Machine-Learning-Tutorials)
3. By P'Rangsiman (or Dr.Rangsiman already), in Thai, very detailed also, focus more on quantum chem [here](https://rangsimanketkaew.github.io/ml-qm-book?fbclid=IwAR0seoGzS3hDWuF0SzzQ1q-Zcqu1VIJFb4MEVwE-nlWbPQjgiF1e2Y0fYmk)
4. Deep learning [here](https://uvadlc-notebooks.readthedocs.io/)

### QML
LCMD at EPFL has an good tutorial to QML for beginner [here](https://github.com/lcmd-epfl/intro-to-qml) 

You can also learn from QML tutorial in which there are both practical (code) and theory stuffs [here](https://www.qmlcode.org/tutorial.html)   

#### Example previous work

1. [Learning the Exciton Properties of Azo-dyes](https://pubs.acs.org/doi/full/10.1021/acs.jpclett.1c01425)
2. [Data-Driven Advancement of Homogeneous Nickel Catalyst Activity for Aryl Ether Cleavage](https://pubs.acs.org/doi/full/10.1021/acscatal.0c00774)
3. [Selected machine learning of HOMO–LUMO gaps with improved data-efficiency](https://pubs.rsc.org/en/content/articlelanding/2022/ma/d2ma00742h)
4. [Reaction-based machine learning representations for predicting the enantioselectivity of organocatalysts](https://pubs.rsc.org/en/content/articlelanding/2021/sc/d1sc00482d)
5. [Electronic spectra from TDDFT and machine learning in chemical space](https://pubs.aip.org/aip/jcp/article/143/8/084111/73278/Electronic-spectra-from-TDDFT-and-machine-learning)
6. [SPAHM: the spectrum of approximated Hamiltonian matrices representations](https://pubs.rsc.org/en/content/articlelanding/2022/dd/d1dd00050k)


### Additional stuffs

1. [Chemoinfomatics tutorial](https://github.com/PatWalters/practical_cheminformatics_tutorials)
