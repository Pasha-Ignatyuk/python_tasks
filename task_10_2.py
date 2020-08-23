import csv

results = []
speed = []

with open('weather.csv') as File:
    reader = csv.DictReader(File)
    for line in reader:
        results.append(int(line['temp']))
    print(results)

with open('weather.csv') as File:
    reader = csv.DictReader(File)
    for line in reader:
        speed.append(int(line['speed']))
    print(speed)

average_temp = sum(results) / len(results)
print('Average temp:', average_temp)

average_speed = sum(speed) / len(speed)
print('Average speed:', average_speed)
