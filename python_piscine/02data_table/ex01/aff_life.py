from matplotlib import pyplot
from load_csv import load

def aff_life():
    data = load("/Users/theoke/Dev/python_piscine/02data_table/ressources/life_expectancy_years.csv")
    france_data = data[data['country'] == 'France']
    x = france_data.columns[1:] 
    y = france_data.iloc[0, 1:]
    selected_values = x[::40]
    pyplot.plot(x, y)
    pyplot.xlabel("Year")
    pyplot.xticks(selected_values)
    pyplot.ylabel("Life expectency")
    pyplot.title("France life expectency Projections")
    pyplot.show()

aff_life()