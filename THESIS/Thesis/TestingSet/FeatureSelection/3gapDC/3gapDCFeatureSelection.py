import pandas as pd
import operator

selectedFeatures = open('selectedFeatures.txt','r')
data = pd.read_csv('3gapDCTestingSet.csv',delimiter=',')

features = selectedFeatures.readline()
list = features.split(",")
list.remove(list[len(list)-1])

selected_features = data[list]

export_csv = selected_features.to_csv(r'3gapDCSelectedFeaturesTestingSet.csv',index= None,header=True)
		

