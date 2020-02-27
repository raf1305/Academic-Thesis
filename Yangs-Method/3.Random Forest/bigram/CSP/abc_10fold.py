import pandas as pd
import numpy as np
import sys
import sklearn
import math
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict

#g=sys.argv[1]
#file.write(g)

ss=sys.argv[3]
file = open(ss,"a+")

filename_train=sys.argv[1]
filename_test=sys.argv[2]
train_data =pd.read_csv('C:\\Users\Avernus\\Desktop\\Thesis\\Random Forest\\bigram\\CSP\\'+filename_train)
test_data = pd.read_csv('C:\\Users\Avernus\\Desktop\\Thesis\\Random Forest\\bigram\\CSP\\'+filename_test)

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
y_pred=cross_val_predict(clf, X,Y, cv=10)
clf.fit(X,Y)

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

file.write('Accuracy : '+ str(accuracy1)+'\n')
file.write('Sensitivity : '+ str(sensitivity1)+'\n')
file.write('Specificity : '+ str(specificity1)+'\n')
file.write('MCC : '+ str(mcc)+'\n')
file.write('\n')
file.close()





