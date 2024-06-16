"""
Here, we create the dataset with which we shall build the
genetic profiles of all MALE successors
"""
import pandas as pd


"""
1. Define column names
"""
column_names = [
    'P0', 'M0', 'M1', 'M2', 'M3', 'M4',
    'M5', 'M6', 'M7', 'M8', 'M9', 'M10',
    'M11', 'M12', 'M13', 'M14']


"""
2. Create a dictionary with column names and 
        their corresponding entries
"""
data_dictionary = {
    f"{name}": [f"{name}-g{i}" for i in range(
        1, 1001)] for name in column_names}


"""
3. Make pandas DataFrame and save data
"""
data = pd.DataFrame(data_dictionary)

path = "C:/Users/HP/PycharmProjects/Gen_n_Soc/data/"
filename = "Genetics_and_Society_Dataset_ORIGIN.csv"
file_path = path + filename

data.to_csv(file_path,
            index=False,
            index_label=False)
