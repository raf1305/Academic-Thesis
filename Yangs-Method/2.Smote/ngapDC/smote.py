import sys
import pandas  as pd
import matplotlib.pyplot as plt
import numpy as np
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split


inputfilename = sys.argv[1]
outputfilename = 'smote_'+inputfilename
data = pd.read_csv(inputfilename)

colnames = data.columns

X = np.array(data.iloc[:, data.columns != 'class'])
y = np.array(data.iloc[:, data.columns == 'class'])
# print('Shape of X: {}'.format(X.shape))
# print('Shape of y: {}'.format(y.shape))

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# print("Number transactions X_train dataset: ", X_train.shape)
# print("Number transactions y_train dataset: ", y_train.shape)
# print("Number transactions X_test dataset: ", X_test.shape)
# print("Number transactions y_test dataset: ", y_test.shape)

# print("Before OverSampling, counts of label '0': {} \n".format(sum(y==0)))

sm = SMOTE(random_state=2)
X_res, y_res = sm.fit_sample(X, y.ravel())

nparray = np.concatenate((X_res,np.array([y_res]).T),axis=1)
smotedDataset = pd.DataFrame(data=nparray)
smotedDataset.columns = colnames
smotedDataset.to_csv(outputfilename,index=False)
# print('After OverSampling, the shape of train_X: {}'.format(X_res.shape))
# print('After OverSampling, the shape of train_y: {} \n'.format(y_res.shape))

# print("After OverSampling, counts of label '1': {}".format(sum(y_res==1)))
# print("After OverSampling, counts of label '0': {}".format(sum(y_res==0)))
