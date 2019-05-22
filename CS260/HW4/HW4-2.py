# Implement an Closed hash table with
# hash function hash(i,N)=i mod n
# Rehash Strategy: rehash(i,k,N)= (hash(i,N)+k) mod N

class ClosedHash:
    def __init__(self, n):
        self.rows = n
        self.table = [[]]*n

    def __str__(self):
        for i in range(self.rows):
            if self.table[i] == []:
                print('Row {} None'.format(i))
            else:
                print('Row {} {}' .format(i,self.table[i][0]))
        return ''

    def hash(self, i):
        return i % self.rows


    def rehash(self, i, k):
        return (self.hash(i) + k) % self.rows

    def insert(self, num):

        h = self.hash(num)
        if self.table[h] == [num]:
            return

        while self.table[h] != []:
            h += 1

        self.table[h] = [num]


    def member(self, num):
        for i in range(self.rows):
            if self.table[i] == [num]:
                return True
        return False

    def delete(self, num):
        for i in range(self.rows):
            if self.table[i] == [num]:
                self.table[i].remove(num)
        # if num in self.table[self.hash(num)]:
        #     self.table[self.hash(num)].remove(num)




