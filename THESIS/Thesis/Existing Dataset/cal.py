import pandas as pd

data = pd.read_csv("3gapDCTestExistingTrainingset.csv",delimiter=",")
data2 = pd.read_csv("3gapDCTestExistingTestingset.csv",delimiter=",")
columns = data.columns

tempColumns = columns
print(tempColumns)
for i in columns:
    print(data[i].sum())
    if data[i].sum() <= 1:
        print(i)
        tempColumns = tempColumns.drop(i)
print(tempColumns)
data = data[tempColumns]
data2 = data2[tempColumns]

data.to_csv("3gapDCTestModifiedExistingTrainingset.csv")
data2.to_csv("3gapDCTestModifiedExistingTestingset.csv")