import csv

f=open("babies-first-names-17-10-17.csv","r", encoding="latin-1")

with f as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip header
    data = [r for r in reader]

    num = 0
    name = ''
    for rank in range(len(data)):
        if data[rank][4] == '1':
            if int(data[rank][3]) > int(num):
                num = data[rank][3]
                name = data[rank][2]

    print('The most popular name was given to', num, 'children.')
    print(name)
