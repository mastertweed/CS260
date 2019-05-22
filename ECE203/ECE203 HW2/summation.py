quest = str('Enter a number\n')
ans = input(quest)
m = int(ans)
s = 0

for i in range(1,m+1):
    s = s + 1/i

f3 = open('summation.txt','w+')
f3.write('%d' % (s))
print(s)
