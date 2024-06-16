import pandas as pd
import matplotlib.pyplot as plt


"""
1. Load data
"""
path = "C:/Users/HP/PycharmProjects/Gen_n_Soc/results/"
filename = "populations.csv"
file_path = path + filename
data = pd.read_csv(file_path)


"""
2. Plot the data.
        The y-axis is set to a logarithmic scale to accommodate 
            the exponential difference in values.
"""


def plot_populations():
    """
    Set up the matplotlib figure and axes for
    a 3x5 grid of plots
    """
    fig, axes = plt.subplots(3, 5, figsize=(15, 9))

    """Flatten the axes array for easy iteration"""
    axes = axes.flatten()

    # Loop through each generation and create a plot
    for i in range(15):
        # Get the data for the current generation
        generation_data = data.iloc[i]

        # Create the plot with a logarithmic scale on the y-axis
        axes[i].bar('+Clan', generation_data['+Clan'], color='blue')
        axes[i].bar('-Clan', generation_data['-Clan'], color='orange')
        axes[i].set_yscale('log')

        # Annotate the plot with the generation number
        axes[i].set_title(f'Gen. {generation_data["Generation"]}')

        # Add annotations for population values
        axes[i].text(
            0, generation_data['+Clan'],
            int(generation_data['+Clan']), ha='center')
        axes[i].text(
            1, generation_data['-Clan'],
            int(generation_data['-Clan']), ha='center')

    # Adjust layout to prevent overlap
    plt.tight_layout()

    img_name = "pop_plots.png"
    filepath = path + img_name
    plt.savefig(filepath, dpi=2000, bbox_inches='tight')


plot_populations()
