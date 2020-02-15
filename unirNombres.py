#!/usr/bin/python
#-*-coding: utf-8-*-

import csv

print("Unir nombres? [s]í/[n]o")

action = raw_input('>>: ').lower()

print("Selecciona un formato para las palabras:")
print("u = mayúsculas")
print("l = minúsculas")
print("lu = mayúsculas y minúsculas")

caseF = raw_input('>>: ').lower()

file = '/home/promo/Escritorio/unir_nombres/nombres.csv'
file_new = '/home/promo/Escritorio/unir_nombres/nombresUnidos.csv'

datas = []
if action == 's':
    with open(file) as f:
        rows = csv.reader(f)
        for row in rows:
            name = ''
            if len(row) > 1:
                name =  row[0] + " " + row[1] if len(row) < 3 else row[0] + " " + row[1] + " " + row[2]
            if caseF == 'u':
                name = name.upper()
            elif caseF == 'l':
                name = name.lower()
            elif caseF == 'lu':
                name = name.title()
            else:
                name = name.title()
    
            datas.append([name])
    
    
    with open(file_new, "w") as ff:
        csvw = csv.writer(ff)
        for data in datas:
            csvw.writerow(data)

else:
    with open(file) as f:
        rows = csv.reader(f)
        for row in rows:
            for index, item in enumerate(row):
                if item:
                    if caseF == 'u':
                        row[index] = item.upper()
                    elif caseF == 'l':
                        row[index] = item.lower()
                    elif caseF == 'lu':
                        row[index] = item.title()
                    else:
                        row[index] = item.title()
            datas.append(row)
    

    with open(file_new, "w") as ff:
        csvw = csv.writer(ff)
        for data in datas:
            csvw.writerow(data)
