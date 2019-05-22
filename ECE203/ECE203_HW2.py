c = 0;
f = 0;

deg = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

f = open("ftoc1.txt","w+");
for i in deg:
    c = (5/9)*(i-32)
    f.write('%d   ' % (i))
    f.write('%d\n' % (c))

#---------------------------------

f2 = open("ftoc2.txt","w+");
for k in deg:
    c = (5/9)*(k-32)
    c2 = (1/2)*(k-30)
    err = c2 - c
    f2.write('%d   ' % (k))
    f2.write('%d   ' % (c))
    f2.write('%d   ' % (c2))
    f2.write('%d\n' % (err))

#--------------------------------

quest = str('Enter a number\n')
ans = input(quest)
m = int(ans)
s = 0

for i in range(1,m+1):
    s = s + 1/i

print(s)