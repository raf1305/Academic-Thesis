import sys
import pandas as pd
import numpy as np

inputfile = open("selectedFeatures.txt","+r")
line = inputfile.readline()
features = line.split(",")
testingfile = pd.read_csv("allExistingTestingset.csv",delimiter=",")
testingfile = testingfile[features]
testingfile.to_csv("allSelectedFeaturesExistingTestingset.csv",index=False)
print(features)