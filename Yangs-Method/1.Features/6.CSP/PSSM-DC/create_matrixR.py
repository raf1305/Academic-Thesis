import os
import sys

start = 1 #int(sys.argv[1])
end2 = 121
end = 709 #int(sys.argv[2])+1



os.system("python matrix_genration_in_text.py " +'PSSM-DC-Trainingset-DIV-new.csv' +' '+str(end))

for i in range(start, end):
    filename = str(i)+".txt"
    os.system("python before_average_R.py " + filename)

os.system("python after_average_R.py " + str(start) +' '+ str(end2)+' '+str(end)+ ' CSP-PSSM-DC-Trainingset-DIV-new.csv')


start = 1 #int(sys.argv[1])
end2 = 41
end = 237 #int(sys.argv[2])+1



os.system("python matrix_genration_in_text.py " +'PSSM-DC-Testingset-DIV-new.csv' +' '+str(end))

for i in range(start, end):
    filename = str(i)+".txt"
    os.system("python before_average_R.py " + filename)

os.system("python after_average_R.py " + str(start) +' '+ str(end2)+' '+str(end)+ ' CSP-PSSM-DC-Testingset-DIV-new.csv')

start = 1 #int(sys.argv[1])
end2 = 14
end = 65 #int(sys.argv[2])+1



os.system("python matrix_genration_in_text.py " +'PSSM-DC-Testingset-DIV.csv' +' '+str(end))

for i in range(start, end):
    filename = str(i)+".txt"
    os.system("python before_average_R.py " + filename)

os.system("python after_average_R.py " + str(start) +' '+ str(end2)+' '+str(end)+ ' CSP-PSSM-DC-Testingset-DIV.csv')



start = 1 #int(sys.argv[1])
end2 = 65
end = 305 #int(sys.argv[2])+1



os.system("python matrix_genration_in_text.py " +'PSSM-DC-Trainingset-DIV.csv' +' '+str(end))

for i in range(start, end):
    filename = str(i)+".txt"
    os.system("python before_average_R.py " + filename)

os.system("python after_average_R.py " + str(start) +' '+ str(end2)+' '+str(end)+ ' CSP-PSSM-DC-Trainingset-DIV.csv')





