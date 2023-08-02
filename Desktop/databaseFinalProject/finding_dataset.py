import csv
# select distinct
# table1.zip, table1.pop, table2.lat,table2.long,table2.name
# from table1 join table2 on table1.zip = table2.table1_zip

def city():
    with open('telecom_zipcode_population.csv','r') as file:
        reader = csv.reader(file)
        a = []
        for row in reader:
            if row[0] not in a:
                a.append(row[0])
        for row in reader:
            if row[6] in a:
                with open('telecom_zipcode_population.csv','r') as f:
                    for row1 in file:
                        if row1[0] == row[6]:
                            with open('city.csv', 'a', newline='') as file:
                                writer = csv.writer(file, delimiter=',')
                                writer.writerow((row[0], row[5], row[7], row[8], row1[1]))



with open('telecom_zipcode_population.csv','r') as file:
    reader = csv.reader(file)
    a = []
    for row in reader:
        a.append(row[0])

print(a)
seen = set()
dupes = []

for x in a:
    if x in seen:
        dupes.append(x)
    else:
        seen.add(x)

print(dupes)

