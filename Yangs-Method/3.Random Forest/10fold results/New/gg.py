import sys
from decimal import Decimal


file_name = sys.argv[1]

accuracy = []
sensitivity = []
specificity = []
mcc = []
file = open('average_'+file_name,"a+")
strline= []
with open(file_name) as fp: 
    lines = fp.readlines() 
    for line in lines: 
    	strline.append(line.strip())


for data in strline:
    temp = data.split(' : ')
    if temp[0] == 'Accuracy':
        accuracy.append(temp[1])
    elif temp[0] == 'Sensitivity':
        sensitivity.append(temp[1])
    elif temp[0] == 'Specificity':
        specificity.append(temp[1])
    elif temp[0] == 'MCC':
        mcc.append(temp[1])


total_accuracy = 0
for a in accuracy:
    total_accuracy = total_accuracy + Decimal(a)
mean_accuracy = total_accuracy / len(accuracy)
print("accuracy :", mean_accuracy)

total_sensitivity = 0
for a in sensitivity:
    total_sensitivity = total_sensitivity + Decimal(a)
mean_sensitivity = total_sensitivity / len(sensitivity)
print("sensitivity :", mean_sensitivity)

total_specificity = 0
for a in specificity:
    total_specificity = total_specificity + Decimal(a)
mean_specificity = total_specificity / len(specificity)
print("specificity :", mean_specificity)

total_mcc = 0
for a in mcc:
    total_mcc = total_mcc + Decimal(a)
mean_mcc = total_mcc / len(accuracy)
print("mcc :", mean_mcc)
file.write("accuracy :"+ str(mean_accuracy)+'\n')
file.write("sensitivity :"+str(mean_sensitivity)+'\n')
file.write("specificity :"+str(mean_specificity)+'\n')
file.write("mcc :"+str(mean_mcc)+'\n')
file.close()
