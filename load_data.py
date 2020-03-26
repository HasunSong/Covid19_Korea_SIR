# %%
import numpy as np
import csv


def load_csv(directory):
    data=[]
    with open(directory, newline='') as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

