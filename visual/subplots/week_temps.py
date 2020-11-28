import csv

def read_data():
    with open("temps.csv") as f:
        r = csv.reader(f)
        row = next(r)
        weekList = [week.strip() for week in row]
        data = {weekList[0]:[], weekList[1]:[]}
        for row in r:
            data[weekList[0]].append(float(row[0].strip()))
            data[weekList[1]].append(float(row[1].strip()))
    return data

print(read_data())