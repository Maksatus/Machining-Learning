import pandas

data = pandas.read_csv('titanic.csv')
index_col = 'PassengerId'
suv = 0
non_suv = 0
sum = 0
for index_col, row in data.iterrows():
    if row[1] == 1:
        suv += 1
    else:
        non_suv += 1

sum = suv + non_suv
print(round((suv*100) / sum,2))