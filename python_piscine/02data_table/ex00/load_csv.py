from pandas import read_csv

def load(path: str):
    return read_csv(path)


print(load("/Users/theoke/Dev/python_piscine/02data_table/ressources/income_per_person_gdppercapita_ppp_inflation_adjusted.csv"))
