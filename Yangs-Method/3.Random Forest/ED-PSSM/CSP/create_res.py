import os
for i in range(0,9):
    os.system("python abc_10fold.py "+'smote_CSP-PSSM-ED-Trainingset.csv' +' CSP-PSSM-ED-Testingset.csv'+' smote_10fold_CSP_ED_results.txt')
for i in range(0,9):
    os.system("python abc_10fold.py "+'smote_CSP-PSSM-ED-Trainingset-new.csv' +' CSP-PSSM-ED-Testingset-new.csv'+' smote_10_fold_CSP_ED_results_new.txt')
