c = 0;
f = 0;

deg = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

f = open("ftoc1.txt","w+");
f.write('Farenheight    ')
f.write('Celcius\n')

for i in deg:
    c = round((5/9)*(i-32),2)
    i = round(i, 2)
    f.write('%-8s %12s\n' % (i, c))