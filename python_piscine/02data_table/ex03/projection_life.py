from matplotlib import pyplot
from load_csv import load
from pandas import concat
from numpy import arange

def projection_life():
    life_expectency = load("/Users/theoke/Dev/python_piscine/02data_table/ressources/life_expectancy_years.csv")
    income = load("/Users/theoke/Dev/python_piscine/02data_table/ressources/income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    
    merged = concat([life_expectency["1900"], income["1900"]], axis=1)
    merged.columns = ['life_expectency', 'income']
    merged = merged.dropna()

    y = merged["life_expectency"].values.astype(float)
    x = merged["income"].values.astype(float)

    y_ticks = arange(20, 60, 5)
    x_ticks = arange(0, 10000, 1000)

    pyplot.scatter(x, y)
    pyplot.xlabel("Gross domestic product")
    pyplot.ylabel("Life Expectancy")
    pyplot.title("1900")
    pyplot.xticks(x_ticks)
    pyplot.yticks(y_ticks)
    pyplot.show()


projection_life()