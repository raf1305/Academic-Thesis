import os
import sys

start = 1 #int(sys.argv[1])
end2 = 121
end = 708 #int(sys.argv[2])+1



os.system("python matrix_genration_in_text.py " +'PSSM-ED-Trainingset-new.csv' +' '+str(end))

for i in range(start, end):
    filename = str(i)+".txt"
    os.system("python before_average_R.py " + filename)

os.system("python after_average_R.py " + str(start) +' '+ str(end2)+' '+str(end)+ ' CSP-PSSM-ED-Trainingset-new.csv')


start = 1 #int(sys.argv[1])
end2 = 41
end = 237 #int(sys.argv[2])+1



os.system("python matrix_genration_in_text.py " +'PSSM-ED-Testingset-new.csv' +' '+str(end))

for i in range(start, end):
    filename = str(i)+".txt"
    os.system("python before_average_R.py " + filename)

os.system("python after_average_R.py " + str(start) +' '+ str(end2)+' '+str(end)+ ' CSP-PSSM-ED-Testingset-new.csv')

start = 1 #int(sys.argv[1])
end2 = 14
end = 65 #int(sys.argv[2])+1



os.system("python matrix_genration_in_text.py " +'PSSM-ED-Testingset.csv' +' '+str(end))

for i in range(start, end):
    filename = str(i)+".txt"
    os.system("python before_average_R.py " + filename)

os.system("python after_average_R.py " + str(start) +' '+ str(end2)+' '+str(end)+ ' CSP-PSSM-ED-Testingset.csv')



start = 1 #int(sys.argv[1])
end2 = 65
end = 305 #int(sys.argv[2])+1



os.system("python matrix_genration_in_text.py " +'PSSM-ED-Trainingset.csv' +' '+str(end))

for i in range(start, end):
    filename = str(i)+".txt"
    os.system("python before_average_R.py " + filename)

os.system("python after_average_R.py " + str(start) +' '+ str(end2)+' '+str(end)+ ' CSP-PSSM-ED-Trainingset.csv')





