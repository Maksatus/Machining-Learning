import pandas

data = pandas.read_csv('titanic.csv')
ages = data['Age'].dropna()

print("{:0.2f} {:0.2f}".format(ages.mean(), ages.median()))