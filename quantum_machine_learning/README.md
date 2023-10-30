## Quantum-chemical machine learning (QML)


### Some theory stuffs

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
    

### Practical stuffs
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
    - Spectrum of London and Axillrod-Teller-Muto potential (SLATM) and the local (atomic) version of which (aSLATM)\
    - FCHL
- Benchmark dataset
    - QM9/QM7/QM7b
