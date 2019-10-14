import csv
import matplotlib.pyplot as plt
import numpy as np

# csv file name
filename = "experiment1c.csv"

rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting each data row one by one
    for row in csvreader:
        rows.append([float(i) for i in row])


measured = []

dutyCycle = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]

for k in range(1,len(rows)):
    m = sum(rows[k]) / len(rows[k])

    total = 0
    for i in range(len(rows[k])):
        if rows[k][i] > m:
            total += 1

    measured.append(total/len(rows[k]))

x = dutyCycle
y = measured

m = (len(x) * np.sum(np.multiply(x,y)) - np.sum(x) * np.sum(y)) / (len(x)*np.sum(np.multiply(x,x)) - np.sum(x) ** 2)
b = (np.sum(y) - m * np.sum(x)) / len(x)

trend = []
for i in range(len(x)):

    trend.append(m*x[i] + b)

plt.plot(dutyCycle, measured, "bo")
plt.plot(dutyCycle, trend, "r")
plt.xlabel("Duty Cycle (%)")
plt.ylabel('On-Time (%)')
plt.title('On-Time vs Duty Cycle')

plt.ylim(0)
plt.grid(True)

plt.show()