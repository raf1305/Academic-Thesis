import pandas as pd
import numpy as np
import sys
import sklearn
import math
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

file = open("smote_ED-PSSM-results.txt","a+")

filename_train='smote_PSSM-ED-Trainingset.csv'
filename_test='PSSM-ED-Testingset.csv'
train_data =pd.read_csv('C:\\Users\Avernus\\Desktop\\Thesis\\Random Forest\\ED-PSSM\\Normal\\'+filename_train)
test_data = pd.read_csv('C:\\Users\Avernus\\Desktop\\Thesis\\Random Forest\\ED-PSSM\\Normal\\'+filename_test)

test_Y= test_data['class'].values
test_X = test_data.drop(labels='class',axis=1)

train_data = pd.DataFrame(train_data)
Y = train_data['class'].values
X=  train_data.drop(labels='class',axis=1)
X=X.values

X_train=X
y_train=Y
#X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=1)
clf=RandomForestClassifier(n_estimators=100)
clf.fit(X_train,y_train)

y_pred =clf.predict(test_X)
#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
# Model Accuracy, how often is the classifier correct?
#print("Training Accuracy:",metrics.accuracy_score(y_test, y_pred))

test_pred =clf.predict(test_X)
#print("Testing Accuracy:",metrics.accuracy_score(test_Y,test_pred))


from sklearn.metrics import confusion_matrix    

cm1 = confusion_matrix(test_Y,test_pred)
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

file.write('Accuracy : '+ str(accuracy1)+'\n')
file.write('Sensitivity : '+ str(sensitivity1)+'\n')
file.write('Specificity : '+ str(specificity1)+'\n')
file.write('MCC : '+ str(mcc)+'\n')
file.write('\n')
file.close()





