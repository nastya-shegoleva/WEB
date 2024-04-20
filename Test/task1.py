import csv
import json

with open("subjects.csv") as fp:
    reader = csv.reader(fp, delimiter=',', quotechar='"')
    sp = []
    for index, row in enumerate(reader):
        if index:
            if row[2] != row[3]:
                row[2:4] = list(map(int, row[2:4]))
                print(row)
                sp.append(dict(zip(keys[1:-1], row[1:-1])))
                print(sp)
        else:
            keys = row

with open('changes.json', 'w') as cat_file:
    json.dump(sp, cat_file)
