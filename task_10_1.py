import csv

results = []
with open('age_groups.csv') as File:
    reader = csv.DictReader(File)
    for line in reader:
        results.append(line['age'])
    print(results)

lst =[]

g = {'1-12': 0, '13-18': 0, '19-25': 0,'26-40': 0,'>=41': 0}

for i in results:
    i = int(i)
    if 1 <= i <= 12:
        g['1-12'] += 1
    elif 13 <= i <= 18:
        g['13-18'] += 1
    elif 19 <= i <= 25:
        g['19-25'] += 1
    elif 26 <= i <= 40:
        g['26-40'] += 1
    elif i >= 41:
        g['>=41'] += 1

lst.append(g)
print(lst)

with open('age_groups_rapt.csv', 'w') as file:
    fieldnames = ['1-12', '13-18', '19-25', '26-40', '>=41']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(lst)

print("writing complete")


