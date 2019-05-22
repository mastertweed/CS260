user = input('Enter a Credit Card number:\n')
card_num = []

for i in range(len(user)):
    card_num.append(int(user[i]))

even, odd = card_num[::2], card_num[1::2]

sum = sum(odd)

even = [x * 2 for x in even]
even_str = ''
for i in even:
    even_str = even_str + str(i)

sum2 = 0
for i in range(len(even_str)):
    sum2 = sum2 + int(even_str[i])

final = str(sum + sum2)
if final[-1] == str(0):
    print('The Number is Valid')
else:
    print('The Number is Invalid')