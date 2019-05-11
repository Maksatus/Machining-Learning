import pandas

data = pandas.read_csv('titanic.csv')
print(data.corr().to_string())