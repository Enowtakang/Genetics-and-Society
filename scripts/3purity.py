"""Here, we make a pie chart showing how much of the
first patriarch(P0)'s DNA is in every successor
"""
import pandas as pd
import matplotlib.pyplot as plt


"""
1. Load data
"""
path = "C:/Users/HP/PycharmProjects/Gen_n_Soc/data/"
filename = "Genetics_and_Society_Dataset_COMPLETE.csv"
file_path = path + filename
data = pd.read_csv(file_path)

path2 = "C:/Users/HP/PycharmProjects/Gen_n_Soc/results/"

"""
2. Make the purity plot
"""
columns = [
    'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8',
    'P9', 'P10', 'P11', 'P12', 'P13', 'P14', 'P15']


def plot_purity_values():
    # Set up the matplotlib figure and axes for a 3x5 grid of plots
    fig, axes = plt.subplots(3, 5, figsize=(15, 9))

    # Flatten the axes array for easy iteration
    axes = axes.flatten()

    # Loop through each column and create a pie chart
    for i, column in enumerate(columns):
        # Calculate the percentages
        with_P0 = data[column].apply(
            lambda x: str(x).startswith('P0')).mean()
        without_P0 = 1 - with_P0

        # Data for plotting
        to_plot = [with_P0, without_P0]
        labels = ['+P0', '-P0']

        # Create the pie chart
        axes[i].pie(
            to_plot, labels=labels,
            autopct='%1.1f%%', startangle=140)

        # Annotate the pie chart with the column name
        axes[i].set_title(column)

    img_name = "purities.png"
    filepath = path2 + img_name
    plt.savefig(filepath, dpi=2000, bbox_inches='tight')


plot_purity_values()
