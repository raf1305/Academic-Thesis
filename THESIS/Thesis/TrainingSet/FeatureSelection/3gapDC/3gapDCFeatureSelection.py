import sys
import pandas as pd
import operator

inputfilename = sys.argv[1]

data = pd.read_csv(inputfilename,delimiter=',')
amino_acids = "ARNDCEQGHILKMFPSTWYV"
dipeptides = []

features = data.colunms
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
	if _len==34:
		break
_list.append('class')

selectedFeatures = data[_list]

elif ("3gapDC".lower() in inputfilename.lower()) and ("smoted".lower() in inputfilename.lower():
    featureFile = open("3gapDCSmotedSelectedFeatures.txt",'w+')
    outputfilename = "3gapDCSmotedSelectedFeaturesExistingTrainingset.csv"
elif ("bigram".lower() in inputfilename.lower()) and ("smoted".lower() in inputfilename.lower():
    featureFile = open("bigramSmotedSelectedFeatures.txt",'w+')
    outputfilename = "bigramSmotedSelectedFeaturesExistingTrainingset.csv"
elif ("PAAC".lower() in inputfilename.lower()) and ("smoted".lower() in inputfilename.lower():
    featureFile = open("PAACSmotedSelectedFeatures.txt",'w+')
    outputfilename = "PAACSmotedSelectedFeaturesExistingTrainingset.csv"
elif "3gapDC".lower() in inputfilename.lower():
    featureFile = open("3gapDCSelectedFeatures.txt",'w+')
    outputfilename = "3gapDCSelectedFeaturesExistingTrainingset.csv"
elif "bigram".lower() in inputfilename.lower():
    featureFile = open("bigramSelectedFeatures.txt",'w+')
    outputfilename = "bigramSelectedFeaturesExistingTrainingset.csv"
elif "PAAC".lower() in inputfilename.lower():
    featureFile = open("PAACSelectedFeatures.txt",'w+')
    outputfilename = "PAACSelectedFeaturesExistingTrainingset.csv"
    
for i in _list:
	featureFile.write(i+",")
featureFile.close()

selectedFeatures.to_csv(outputfilename,index= None,header=True)
		

