import sys
import pandas as pd
import operator

inputfilename = sys.argv[1]
numberOfFeatures = int(sys.argv[2])

data = pd.read_csv(inputfilename,delimiter=',')
amino_acids = "ARNDCEQGHILKMFPSTWYV"
dipeptides = []

features = data.columns
features = features.drop('class')
# for i in amino_acids:
	# for j in amino_acids:
		# di = i+j
		# dipeptides.append(di)

S = {}
for i in features:
	meui = data[i].mean()
	numerator = 0
	denominator = 0
	for j in range(0,2):
		meuij = data[data['class'] == j].mean()[i]
		nj = data[data['class'] == j].count()[i]
		sigmaij = data[data['class'] == j].std()[i]
		numerator += nj*(meuij-meui)*(meuij-meui)
		denominator += nj*sigmaij*sigmaij
	si = numerator/denominator
	S[i] = si

S_tuple = sorted(S.items(),key = operator.itemgetter(1),reverse = True)

_list = []
_len = 0;
for i,j in S_tuple:
	_len=_len+1
	_list.append(i)
	if _len==numberOfFeatures:
		break
_list.append('class')
selectedFeatures = data[_list]

if ("3gapDC".lower() in inputfilename.lower()) and ("smoted".lower() in inputfilename.lower()):
    featureFile = open("3gapDCSmotedSelectedFeatures.txt",'w+')
    outputfilename = "3gapDCSmotedSelectedFeaturesExisting"
elif ("bigram".lower() in inputfilename.lower()) and ("smoted".lower() in inputfilename.lower()):
    featureFile = open("bigramSmotedSelectedFeatures.txt",'w+')
    outputfilename = "bigramSmotedSelectedFeaturesExisting"
elif ("PAAC".lower() in inputfilename.lower()) and ("smoted".lower() in inputfilename.lower()):
    featureFile = open("PAACSmotedSelectedFeatures.txt",'w+')
    outputfilename = "PAACSmotedSelectedFeaturesExisting"
elif "3gapDC".lower() in inputfilename.lower():
    featureFile = open("3gapDCSelectedFeatures.txt",'w+')
    outputfilename = "3gapDCSelectedFeaturesExisting"
elif "bigram".lower() in inputfilename.lower():
    featureFile = open("bigramSelectedFeatures.txt",'w+')
    outputfilename = "bigramSelectedFeaturesExisting"
elif "PAAC".lower() in inputfilename.lower():
    featureFile = open("PAACSelectedFeatures.txt",'w+')
    outputfilename = "PAACSelectedFeaturesExisting"
    
if "testingset".lower() in inputfilename.lower():
    outputfilename += "Testingset.csv"
elif "trainingset".lower() in inputfilename.lower():
    outputfilename += "Trainingset.csv"
 
for i in _list:
	featureFile.write(i+",")
featureFile.close()

selectedFeatures.to_csv(outputfilename,index= None,header=True)
		

