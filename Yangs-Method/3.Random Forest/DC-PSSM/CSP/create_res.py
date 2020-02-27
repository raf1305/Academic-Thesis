import os
for i in range(0,9):
    os.system("python abc_10fold.py "+'smote_CSP-PSSM-DC-Trainingset-DIV.csv' +' CSP-PSSM-DC-Testingset-DIV.csv'+' smote_10fold_CSP_DC_results.txt')
for i in range(0,9):
    os.system("python abc_10fold.py "+'smote_CSP-PSSM-DC-Trainingset-DIV-new.csv' +' CSP-PSSM-DC-Testingset-DIV-new.csv'+' smote_10fold_CSP_DC_results_new.txt')
