import pandas

data = pandas.read_csv('titanic.csv')
b = data['Age'].mean()
m = data['Age'].median()
print(round(b, 2), m)