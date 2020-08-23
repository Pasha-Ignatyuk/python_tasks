import csv
import datetime
import pytz
#import timestring
import dateutil.parser as dparser

results = []

with open('dates_task_10_3.csv') as File:
    reader = csv.DictReader(File)
    for line in reader:
        results.append(line['Dates'])
    print(results)

dt = dparser.parse(results[0],fuzzy=True)
earlier = dt

for i in results:
    i = dparser.parse(i,fuzzy=True)
    if i <= earlier:
        earlier = i
    else:
        continue
print(earlier)
