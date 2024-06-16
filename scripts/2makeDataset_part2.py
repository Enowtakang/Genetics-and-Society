"""
Here, we build the genetic profiles of all male successors.
"""
import pandas as pd
import numpy as np


"""
1. Load data
"""
path = "C:/Users/HP/PycharmProjects/Gen_n_Soc/data/"
filename = "Genetics_and_Society_Dataset_ORIGIN.csv"
file_path = path + filename
data_origin = pd.read_csv(file_path)


"""
2. We create a function to mate any two individuals and 
    create the genetic profile of the offspring. 
"""


def mate(offspring, patriarch, matriarch):
    """
    randomly select 500 genes from the patriarch and
    500 genes from the matriarch
    """
    patriarch_500 = data_origin[
        patriarch].sample(n=500, random_state=1).tolist()
    matriarch_500 = data_origin[
        matriarch].sample(n=500, random_state=1).tolist()

    """combine the genes and SHUFFLE the combination"""
    combined_genes = patriarch_500 + matriarch_500
    np.random.seed(1)
    np.random.shuffle(combined_genes)

    """add offspring to the database"""
    data_origin[offspring] = combined_genes


"""
3. Build the genetic profiles of all male successors
"""
# list of lists of offspring, patriarch and matriarch triplets
nuclear_triplets = [
    ['P1', 'P0', 'M0'], ['P2', 'P1', 'M1'], ['P3', 'P2', 'M2'],
    ['P4', 'P3', 'M3'], ['P5', 'P4', 'M4'], ['P6', 'P5', 'M5'],
    ['P7', 'P6', 'M6'], ['P8', 'P7', 'M7'], ['P9', 'P8', 'M8'],
    ['P10', 'P9', 'M9'], ['P11', 'P10', 'M10'],
    ['P12', 'P11', 'M11'], ['P13', 'P12', 'M12'],
    ['P14', 'P13', 'M13'], ['P15', 'P14', 'M14'],]


def make_offsprings():
    for i in range(0, len(nuclear_triplets)):
        mate(
            nuclear_triplets[i][0],
            nuclear_triplets[i][1],
            nuclear_triplets[i][2])

    filename2 = "Genetics_and_Society_Dataset_COMPLETE.csv"
    file_path2 = path + filename2
    data_origin.to_csv(
        file_path2,
        index=False, index_label=False)


make_offsprings()
