import pandas as pd
import operator

data = pd.read_csv("PAAC_smoted.csv",delimiter=",")
PAAC = []
for i in range(1,67):
	string = "PAAC"+str(i)
	PAAC.append(string)

S = {}
for i in PAAC:
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

list = ['class']
len = 0
for i,j in S_tuple:
	len=len+1
	list.append(i)
	if len==12:
		break
selected_features = data[list]

export_csv = selected_features.to_csv(r'PAACSelectedFeatures.csv',index= None,header=True)