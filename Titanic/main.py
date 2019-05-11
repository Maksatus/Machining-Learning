import pandas

data = pandas.read_csv('titanic.csv')
index_col = 'PassengerId'
guy = 0
women = 0
for index_col, row in data.iterrows():
    row[4] = str(row[4])
    if row[4] == "male":
        guy += 1
    else:
        women += 1
print(guy, '', women)