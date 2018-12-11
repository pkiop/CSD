import csv

f = open('csvfile/inclinedata.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

dic = {}
for line in rdr:
    dic[line[0]] = line[1]

print(dic['744'])
f.close()