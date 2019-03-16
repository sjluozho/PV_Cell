import pandas as pd
# import descriptor calculator
from rdkit import Chem
from mordred import Calculator, descriptors
from multiprocessing import freeze_support


def ChemFeatures (data):
    """
        This function is used to extract chemical information from
molecular structures in the form of Smiles_str.

    Attributes:
        data: array or array like of SMILES_str. Input data to be
analysed

    """
    mols = [Chem.MolFromSmiles(mol) for mol in data]
    freeze_support()
    calc = Calculator(descriptors)
    print(list(calc.map(mols)))
    raw_data = calc.pandas(mols)
    features_df = pd.DataFrame(raw_data)
    return features_df
