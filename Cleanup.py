import csv
import os


filenames = []
for file in os.listdir('.'):
    if os.path.splitext(file)[1] == ".csv" and os.path.splitext(file)[0][:7] == "JC-2018":
        filenames.append(file)

fields = []
rows = []
for file in filenames:
    with open(file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields.append(next(csvreader))

        for row in csvreader:
            rows.append(row)
        
        print("No. of rows: %d"%(csvreader.line_num))

print(len(rows))
#print(fields[0])

outputfile = 'citybikedata2018.csv'

with open(outputfile, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(fields[0])

    csvwriter.writerows(rows)


with open(outputfile, 'r') as out:
    #print("No. of rows in merged file: %d"%(sum(1 for line in out)))
    
    csvreader = csv.reader(out)
    i = 0
    for row in csvreader:
        print(row)
        if i == 10:
            break
        else:
            i += 1