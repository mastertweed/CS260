c = 0;
f = 0;

deg = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

f2 = open("ftoc2.txt","w+");
f2.write('Farenheight | Celcius | Est Celcius | Error\n')
for k in deg:
    c = round((5/9)*(k-32), 2)
    c2 = round((1/2)*(k-30), 2)
    err = round(c2 - c, 2)

    f2.write('%-8s %12s %10s %10s\n' % (k, c, c2, err))