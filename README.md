# MNA-PSS-Pred

## Overview
This repository contains supplementary materials for the article "Atom-Centric Prediction of Secondary Structures of Proteins Using Multilevel Neighborhoods of Atoms Descriptors"

The repository contains the following:

1. **datasets** - Contains the datasets used for training and validation
2. **pass_results** - Contains results of the MultiPASS software predictions
3. **webservice_results** - Contains results obtained from the MNA-PSS-Pred web application:
4. **split_merge.py** - A Python script used to handle the merging and splitting of SD files (GitHub does not allow files >=100mb to be uploaded).

## Usage
1. Clone repository: 
```
git clone https://github.com/rnrmu-bioinf/MNA-PSS-Pred.git
```

2. Navigate to the project directory:
```
cd MNA-PSS-Pred
```

3. Merge ASTRAL and training datasets:
```
python split_merge.py merge datasets/astral.sdf.part1
python split_merge.py merger datasets/final_training_0-2A_All_Types.sdf.part1
```
