from pandas import read_csv

def load(path: str):
    return read_csv(path)