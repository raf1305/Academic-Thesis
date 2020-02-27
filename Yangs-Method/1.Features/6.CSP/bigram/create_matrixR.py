import os
import sys

start = 1 #int(sys.argv[1])
end2 = 121
end = 709 #int(sys.argv[2])+1



os.system("python matrix_genration_in_text.py " +'PSSM-bigram-Trainingset-new.csv' +' '+str(end))

for i in range(start, end):
    filename = str(i)+".txt"
    os.system("python before_average_R.py " + filename)

os.system("python after_average_R.py " + str(start) +' '+ str(end2)+' '+str(end)+ ' CSP-PSSM-bigram-Trainingset-new.csv')


start = 1 #int(sys.argv[1])
end2 = 41
end = 237 #int(sys.argv[2])+1



os.system("python matrix_genration_in_text.py " +'PSSM-bigram-Testingset-new.csv' +' '+str(end))

for i in range(start, end):
    filename = str(i)+".txt"
    os.system("python before_average_R.py " + filename)

os.system("python after_average_R.py " + str(start) +' '+ str(end2)+' '+str(end)+ ' CSP-PSSM-bigram-Testingset-new.csv')

start = 1 #int(sys.argv[1])
end2 = 14
end = 65 #int(sys.argv[2])+1



os.system("python matrix_genration_in_text.py " +'PSSM-bigram-Testingset.csv' +' '+str(end))

for i in range(start, end):
    filename = str(i)+".txt"
    os.system("python before_average_R.py " + filename)

os.system("python after_average_R.py " + str(start) +' '+ str(end2)+' '+str(end)+ ' CSP-PSSM-bigram-Testingset.csv')



start = 1 #int(sys.argv[1])
end2 = 65
end = 305 #int(sys.argv[2])+1



os.system("python matrix_genration_in_text.py " +'PSSM-bigram-Trainingset.csv' +' '+str(end))

for i in range(start, end):
    filename = str(i)+".txt"
    os.system("python before_average_R.py " + filename)

os.system("python after_average_R.py " + str(start) +' '+ str(end2)+' '+str(end)+ ' CSP-PSSM-bigram-Trainingset.csv')

start = 1 #int(sys.argv[1])
end2 = 88
end =  305#int(sys.argv[2])+1


#smoted training
os.system("python matrix_genration_in_text.py " +'smote_PSSM-bigram-Trainingset.csv' +' '+str(end))

for i in range(start, end):
    filename = str(i)+".txt"
    os.system("python before_average_R.py " + filename)

os.system("python after_average_R.py " + str(start) +' '+ str(end2)+' '+str(end)+ ' smote_CSP-PSSM-bigram-Trainingset.csv')



start = 1 #int(sys.argv[1])
end2 = 65
end = 305 #int(sys.argv[2])+1


#smoted training-new
os.system("python matrix_genration_in_text.py " +'smote_PSSM-bigram-Trainingset-new.csv' +' '+str(end))

for i in range(start, end):
    filename = str(i)+".txt"
    os.system("python before_average_R.py " + filename)

os.system("python after_average_R.py " + str(start) +' '+ str(end2)+' '+str(end)+ ' smote_CSP-PSSM-bigram-Trainingset-new.csv')




