import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, matthews_corrcoef,accuracy_score, classification_report
from sklearn.model_selection import LeaveOneOut, KFold

TN = 0
TP = 0
FN = 0
FP = 0
acc =  0
sn = 0
sp = 0
mcc = 0
#balancing = "_SMOTED"
balancing = ""
outputFileName = "JackknifeExistingDataset"+balancing+".csv"
trainingFile = sys.argv[1]

outputFile = open(outputFileName,"a+")
outputFile.seek(0)
line = outputFile.readline()
if line == "" or line == "\n" or line == "\t" or line == "\w":
    outputFile.truncate(0)
    outputFile.write("Method,Acc,Sn,Sp,MCC\n")
    
if ("all".lower() in trainingFile.lower()) and ("smoted".lower() in trainingFile.lower()) and ("selected".lower() in trainingFile.lower()):
    outputFile.write("DPC+Bigram+SAAC (Fisher Selection) ")
elif ("all".lower() in trainingFile.lower()) and ("smoted".lower() in trainingFile.lower()):
    outputFile.write("DPC+Bigram+SAAC ")
elif "all".lower() in trainingFile.lower():
    outputFile.write("DPC+Bigram+SAAC ")
elif ("bigram".lower() in trainingFile.lower()) and ("DPC".lower() in trainingFile.lower()):
    outputFile.write("DPC+Bigram ")
elif ("bigram".lower() in trainingFile.lower()) and ("PAAC".lower() in trainingFile.lower()):
    outputFile.write("Bigram+SAAC ")
elif ("DPC".lower() in trainingFile.lower()) and ("PAAC".lower() in trainingFile.lower()):
    outputFile.write("DPC+SAAC ")
elif ("bigram".lower() in trainingFile.lower()) and ("smoted".lower() in trainingFile.lower()):
    outputFile.write("Bigram-PSSM ")
elif ("3gapDC".lower() in trainingFile.lower()) and ("smoted".lower() in trainingFile.lower()):
    outputFile.write("Di-Peptide Composition ")
elif ("PAAC".lower() in trainingFile.lower()) and ("smoted".lower() in trainingFile.lower()):
    outputFile.write("SAAC ")
elif "bigram".lower() in trainingFile.lower():
    outputFile.write("Bigram-PSSM ")
elif "3gapDC".lower() in trainingFile.lower():
    outputFile.write("Di-Peptide Composition ")
elif "PAAC".lower() in trainingFile.lower():
    outputFile.write("SAAC ")

trainingset = pd.read_csv(trainingFile,delimiter=",")
# print(trainingset)
x = trainingset.values
x_scaled = MinMaxScaler().fit_transform(trainingset)
trainingset = pd.DataFrame(x_scaled,columns=trainingset.columns,index=trainingset.index)
# print(trainingset)
trainingset = trainingset.sample(frac=1)
    
colnum = len(trainingset.columns)
max_k = math.ceil(math.sqrt(len(trainingset)))

X = trainingset.iloc[:,:-1].values
y = trainingset.iloc[:,colnum-1].values

#kf = KFold(n_splits = 10)

# match = []
# for i in range(1, max_k+1):
    # knn = KNeighborsClassifier(n_neighbors=i)
    # y_pred = np.array([])
    # tempMatch = []
    # for train_index, test_index in kf.split(X):
        # X_train, X_test = X[train_index], X[test_index]
        # y_train, y_test = y[train_index], y[test_index]
        # knn.fit(X_train,y_train)
        # y_pred = knn.predict(X_test)
        # print(y_pred)
        # print(y_test)
        # tempMatch.append(np.mean(y_pred == y_test))
    # match.append(np.mean(tempMatch))
    # print(i, " complete")
# print(match)
# max_match = max(match)
# maxmatch_k = len(match) - match[::-1].index(max_match)
# print("maxmatch_k = {}, match = {}" .format(maxmatch_k,max_match))
# k = maxmatch_k

# mccList = []
# for i in range(1, max_k+1):
    # knn = KNeighborsClassifier(n_neighbors=i)
    # y_pred = np.array([])
    # tempmcc = 0
    # for train_index,test_index in kf.split(X):
        # X_train, X_test = X[train_index], X[test_index]
        # y_train, y_test = y[train_index], y[test_index]
        # model = knn.fit(X_train, y_train)
        # y_pred = knn.predict(X_test)
        # tempmcc += accuracy_score(y_pred,y_test)
        # tempmcc = matthews_corrcoef(y_test,y_pred)
    # mccList.append(tempmcc/10)
    # print(i, " completed")

# max_mcc = max(mccList[1:])  
# maxmcc_k = len(mccList[1:]) - mccList[:0:-1].index(max_mcc)+1 
# print("maxmcc_k = {}, mcc = {}" .format(maxmcc_k,max_mcc))
# k = maxmcc_k

k = int(open("kValue.txt").readline().strip())
# print("k = {}" .format(k))
outputFile.write("k = {} ," .format(k))
loo = LeaveOneOut()
y_pred = np.empty([1],dtype=int)
y_pred = np.delete(y_pred,np.s_[:])
y_actual = np.empty([1],dtype=int)
y_actual = np.delete(y_actual,np.s_[:])
for train_index, test_index in loo.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    # scaler = StandardScaler()
    # scaler.fit(X_train)

    # X_train = scaler.transform(X_train)
    # X_test = scaler.transform(X_test)

    classifier = KNeighborsClassifier(n_neighbors = k)
    classifier.fit(X_train,y_train)
    
    y_actual = np.append(y_actual,int(y_test[0]))
    y_pred = np.append(y_pred,classifier.predict(X_test)[0].astype(dtype=int))

    # cfMatrix = confusion_matrix(y_test,y_pred)
    # if(len(cfMatrix) == 1):
        # if(y_pred[0] == 0):
            # TN += 1
        # else:
            # TP += 1
    # else:
        # TN += cfMatrix[0,0]
        # FP += cfMatrix[0,1]
        # FN += cfMatrix[1,0]
        # TP += cfMatrix[1,1]
    
# acc = (TP+TN)/(TP+FP+TN+FN)*100
# sn = TP/(TP+FN)*100
# sp = TN/(TN+FP)*100
# mcc = (TP*TN-FP*FN)/(math.sqrt((TP+FN)*(TP+FP)*(TN+FP)*(TN+FN)))
# print("TN = {}, FP = {}, FN = {}, TP = {}" .format(TN,FP,FN,TP))

acc = accuracy_score(y_actual,y_pred)*100
mcc = matthews_corrcoef(y_actual,y_pred)
report = classification_report(y_actual,y_pred,output_dict=True)
sn = report['1']["recall"]*100
sp = report['0']["recall"]*100

print("acc = {} , sn = {}, sp = {}, mcc = {}" .format(acc,sn,sp,mcc))
outputFile.write("{},{},{},{}\n" .format(acc,sn,sp,mcc))

# for i in error:
    # print(i, end = " ")
# print("\n")
# ax = plt.figure(figsize=(12, 6)).gca()
# print([i for i in range(0,len(mccList)) if i != (k-1)])
# ax.plot(range(1, max_k+1), mccList,markevery=[i for i in range(0,len(mccList)) if i != (k-1)],color='red', linestyle='dashed', marker='o',
         # markerfacecolor='blue', markersize=10)
# ax.plot(range(1, max_k+1), mccList, markevery=[k-1],linestyle="",marker='o',
         # markerfacecolor='red', markersize=10)
# plt.title('MCC vs K Value (DPC+Bigram+SAAC SMOTED Fisher Selection)')
# ax.xaxis.set_major_locator(MaxNLocator(integer=True))
# plt.title('MCC vs K Value')
# plt.xlabel('K Value')
# plt.ylabel('MCC')
# plt.show()
#plt.savefig("DPC+Bigram+SAAC.png")	