import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("3gapDCExistingTrainingset.csv",delimiter=",")

length = len(data.columns)

for i in data.columns.drop('class'):
    _sum = data[i].sum()
    if _sum == 0:
        print(1)
