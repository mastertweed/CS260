#Complete Implementation of this class
class Node:
    def __init__(self,value,next):
        self.value = value
        self.next = next

    def __str__(self):
        return "[ %d ]" % self.value

    def getNext(self):
        return self.next

    def setNext(self,n):
        self.next = n

    def getValue(self):
        return self.value

    def setValue(self,v):
        self.value = v


head = Node(0,None)
pos = Node(1, None)
head.setNext(pos)

for i in range(2,10):
    temp = Node(i,None)
    pos.setNext(temp)
    pos = temp

v = head
while v.getNext() != None:
    print(str(v))
    v = v.getNext()

