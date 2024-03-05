import csv

with open('survey.csv', 'r') as f:
    csv_reader = csv.reader(f)
    header_row = next(csv_reader)
    print(header_row)
    
for i in range(len(header_row)):
    print (i, ':', header_row[i])