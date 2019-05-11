import pandas
import operator

data = pandas.read_csv('titanic.csv')
i = 0
res = data['Name'].get_values()
list_name = []
for name_row in res:
    is_woman = ("Miss." in name_row) or ("Mrs." in name_row)
    if is_woman:
        index_brace = name_row.find("(")
        if index_brace != -1:
            name_row = name_row[index_brace + 1:]
            index_space = name_row.find(" ")
            name_row = name_row[:index_space]
            list_name.append(name_row)
        else:
            index_point = name_row.find(".")
            name_row = name_row[index_point + 2:]
            index_space = name_row.find(" ")
            name_row = name_row[:index_space]
            list_name.append(name_row)
        i += 1

print(list_name)
dict_name = {}
dict_name["olo"] = 2
a = dict_name.get("olo")
for name in list_name:
    value = dict_name.get(name)
    if value is None:
        dict_name[name] = 1
    else:
        dict_name[name] = value + 1
sorted_x = sorted(dict_name.items(), key=operator.itemgetter(1))
print(sorted_x)