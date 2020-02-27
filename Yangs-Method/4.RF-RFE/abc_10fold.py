import pandas as pd
import numpy as np
import sys
import sklearn
import math
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.feature_selection import RFE,f_regression
number_of_feature=sys.argv[1]
file = open('smote_10fold_3-gap+CSP-bigram+CSP-DC+CSP-ED-new.txt',"a+")
file1=open('Feature_num vs ACC.txt',"a+")
filename_train='smote_3-gap+CSP-bigram+CSP-DC+CSP-ED-training-new.csv'#sys.argv[1]
filename_test='3-gap+CSP-bigram+CSP-DC+CSP-ED-new.csv'#sys.argv[2]
train_data =pd.read_csv('C:\\Users\Avernus\\Desktop\\Thesis\\Random Forest\\RF-RFE\\'+filename_train)
test_data = pd.read_csv('C:\\Users\Avernus\\Desktop\\Thesis\\Random Forest\\RF-RFE\\'+filename_test)

test_Y= test_data['class'].values
test_X = test_data.drop(labels='class',axis=1)
test_X=test_X.values

train_data = pd.DataFrame(train_data)
Y = train_data['class'].values
X=  train_data.drop(labels='class',axis=1)
X=X.values

#X_train=X
#y_train=Y
#X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=1)
clf=RandomForestClassifier(n_estimators=100)
rfe = RFE(clf, n_features_to_select=int(number_of_feature))

rfe.fit(X,Y)
ranks=rfe.ranking_
y_pred=cross_val_predict(rfe, X,Y, cv=10)
#y_pred =clf.predict(test_X)
#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
# Model Accuracy, how often is the classifier correct?
#print("Training Accuracy:",metrics.accuracy_score(y_test, y_pred))

#test_pred =clf.predict(test_X)
#print("Testing Accuracy:",metrics.accuracy_score(test_Y,test_pred))


from sklearn.metrics import confusion_matrix    

cm1 = confusion_matrix(Y,y_pred )
#print('Confusion Matrix : \n', cm1)


total1=sum(sum(cm1))
#####from confusion matrix calculate accuracy
accuracy1=(cm1[0,0]+cm1[1,1])/total1
print ('Accuracy : ', accuracy1)

sensitivity1 = cm1[1,1]/(cm1[1,1]+cm1[1,0])
print('Sensitivity : ', sensitivity1 )

specificity1 = cm1[0,0]/(cm1[0,1]+cm1[0,0])
print('Specificity : ', specificity1)

TN = cm1[0,0]
FP = cm1[0,1]
FN = cm1[1,0]
TP = cm1[1,1]

mcc = (TP*TN-FP*FN)/(math.sqrt((TP+FN)*(TP+FP)*(TN+FP)*(TN+FN)))

print('MCC : ', mcc)

file1.write('('+str(number_of_feature)+','+str(accuracy1)+')')
file.close()





