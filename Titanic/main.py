import pandas
data = pandas.read_csv('titanic.csv')
sex_counts = data['Sex'].value_counts()
print('{} {}'.format(sex_counts['male'], sex_counts['female']))