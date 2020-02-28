import sys
import pandas as pd
import numpy as np

arg = len(sys.argv)
outputfilename = sys.argv[len(sys.argv)-1]
filenames = []
li = []
columns = np.array([])
for i in range(1,arg-1):
    csv_file = pd.read_csv(sys.argv[i],delimiter=",")
    columns = np.array(csv_file.iloc[:,csv_file.columns == 'class'])
    csv_file = csv_file.drop(['class'],axis=1)
    li.append(csv_file)
columns = pd.DataFrame(data=columns)
columns.columns = ['class']
li.append(pd.DataFrame(data=columns))

dataset = pd.concat(li,axis=1)
dataset.to_csv(outputfilename,index=False)