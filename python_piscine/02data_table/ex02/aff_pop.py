from matplotlib import pyplot
from load_csv import load
from numpy import arange

def aff_pop():
    data = load("/Users/theoke/Dev/python_piscine/02data_table/ressources/population_total.csv")
    france_data = data[data['country'] == 'France'].iloc[0, 1:]
    switzerland_data = data[data['country'] == 'Switzerland'].iloc[0, 1:]
    
    # Convert population data to integers
    france_data = france_data.str.replace('M', '').astype(float) * 1000000
    switzerland_data = switzerland_data.str.replace('M', '').astype(float) * 1000000

    switzerland_data.index = switzerland_data.index.astype(int)
    switzerland_data = switzerland_data[(switzerland_data.index >= 1800) & (switzerland_data.index <= 2050)]
    france_data.index = france_data.index.astype(int)
    france_data = france_data[(france_data.index >= 1800) & (france_data.index <= 2050)]
    
    xsw = switzerland_data.index
    ysw = switzerland_data.values
    x = france_data.index
    y = france_data.values
    selected_xvalues = x[::40]
    selected_yvalues = arange(0, max(y), 20000000)  # Set y-axis graduations from 20M to 20M

    pyplot.plot(x, y, label="France")
    pyplot.plot(xsw, ysw, label='Switzerland')
    pyplot.xlabel("Year")
    pyplot.xticks(selected_xvalues)
    pyplot.ylabel("Population")
    pyplot.yticks(selected_yvalues)
    pyplot.title("Population Projections")
    pyplot.legend(loc="lower right")
    pyplot.show()

aff_pop()