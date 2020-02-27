import os
for i in range(0,9):
    os.system("python abc_10fold.py "+'smote_CSP-PSSM-bigram-Trainingset.csv' +' CSP-PSSM-bigram-Testingset.csv'+' smote_10fold_CSP_Bigram_results.txt')
for i in range(0,9):
    os.system("python abc_10fold.py "+'smote_CSP-PSSM-bigram-Trainingset-new.csv' +' CSP-PSSM-bigram-Testingset-new.csv'+' smote_10_fold_CSP_Bigram_results_new.txt')
