import pandas

data = pandas.read_csv('titanic.csv')
sisp = data['SibSp']
parch = data['Parch']
corr = sisp.corr(parch, method='pearson')
print(corr)