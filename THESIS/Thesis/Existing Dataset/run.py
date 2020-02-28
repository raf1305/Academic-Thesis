import os
import sys

arg = sys.argv[1]

trainingFile = arg+"ExistingTrainingset.csv"
if "SMOTED".lower() in arg.lower():
    testingFile = arg.rstrip("SMOTED")+"ExistingTestingset.csv"
else:
    testingFile = arg+"ExistingTestingset.csv"

os.system("python 10FoldCrossValidationTesting.py " + trainingFile + " " + arg)
os.system("python IndependentTesting.py "+ trainingFile + " " + testingFile)
os.system("python JackknifeTesting.py " + trainingFile)