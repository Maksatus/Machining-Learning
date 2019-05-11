import pandas

data = pandas.read_csv('titanic.csv')
index_col = 'PassengerId'
class_1 = 0
class_other = 0
sum = 0
for index_col, row in data.iterrows():
    if row[2] == 1:
        class_1 += 1
    else:
        class_other += 1

sum = class_1 + class_other
print(round(class_1 * (100 / sum), 2))