"""
A man and a woman together form a clan.
They are generation zero. There is only one man.
Together, they have 4 children, two boys and two girls.
They are generation 1.

The rule is that:
- the girls go off and marry outside the clan,
        while the boys marry and stay back in the clan.
- also, every child (girl or boy, within the clan or
        outside the clan) would have exactly 4 children,
        two boys and two girls.

Note that when the girls go away and marry,
        their sons are not members of the clan.
Only the boys issuing from boys which were already in the clan,
        can become members of the clan.

********************************
++++++++++++++++++++++++++++++++
********************************

Here, we compute and visualize the clan  and out-of-clan
    population in the context where only the boys stay behind
"""
import pandas as pd


"""
1. Loop through 15 generations, computing 'clan' and 
    out-of-clan populations.
"""


def compute_populations():
    pops = list()

    """
    Initialize variables for the number of boys in the clan 
        and people outside"""
    boys_in_clan = 1  # Starting with one man in generation 0
    people_outside_clan = 0  # Starting with no one outside the clan

    """Loop through 15 generations"""
    for generation in range(1, 16):
        # Each boy in the clan will have two boys who will
        # stay in the clan
        boys_in_clan *= 2

        # Each child (boy or girl) will have four children,
        # so we multiply by 4
        # Subtracting the boys_in_clan since they are already
        # counted in the clan
        people_outside_clan = (
                (people_outside_clan * 4) - boys_in_clan)

        # Add the data to the DataFrame
        datum = {'Generation': generation,
                 '+Clan': boys_in_clan,
                 '-Clan': abs(people_outside_clan)}
        pops.append(datum)

    data = pd.DataFrame(pops)

    """Save DataFrame"""
    path = "C:/Users/HP/PycharmProjects/Gen_n_Soc/results/"
    filename = "populations.csv"
    file_path = path + filename
    data.to_csv(file_path, index=False, index_label=False)


compute_populations()
