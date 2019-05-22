# Implement an OPEN hash table with
# hash function hash(i,N)=i%n

class OpenHash:
    def __init__(self, n):
        self.rows = n
        self.table = [[]]*n

    def __str__(self):
        for i in range(self.rows):
            if self.table[i] == []:
                print('Row {} []'.format(i))
            else:
                print('Row {} {}' .format(i,self.table[i]))
        return ''
        # return 'Row %d []' % self.rows

    def hash(self, i):
        return i % self.rows

    def insert(self, num):
        if self.table[(num % self.rows)] == [num]:
            return
        elif self.table[(num % self.rows)] == []:
            self.table[(num % self.rows)] = [num]
        else:
            self.table[(num % self.rows)].append(num)

    def member(self, num):
        if self.table[(num % self.rows)] == []:
            return False
        elif num not in self.table[(num % self.rows)]:
            return False
        else:
            return True

    def delete(self, num):
        if num in self.table[(num % self.rows)] :
            self.table[(num % self.rows)].remove(num)




# print('Welcome to Open Hash Table Tests')
#
# n = int(input('How big would you like your hash table to be?'))
#
# r = int(input('Enter a seed for the random number generator:'))
#
# Q = OpenHash(n)
#
#
# print(str(Q))
#
# Q.insert(4)
# Q.insert(8)
#
# print(str(Q))