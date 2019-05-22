# Complete Implementation of this file

# Copy in your Node Class from the previous question.
class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
        return

    def __str__(self):
        return "[ %d ]" % self.value

    def getNext(self):
        return self.next

    def setNext(self, n):
        self.next = n

    def getValue(self):
        return self.value

    def setValue(self, v):
        self.value = v


# You MUST implement using your node class
class Queue:
    def __init__(self):
        self.head = Node(None,None)
        self.tail = self.head

    def __str__(self):
        if self.head.getValue() is None:
            return "Queue Empty"
        else:
            return "[ %d ]" % self.head.getValue()

    def front(self):
        return self.head.getValue()

    def empty(self):
        if self.head.getValue() is None:
            return True
        else:
            return False

    def enqueue(self, x):
        if self.head.getValue() is None:
            self.head.setValue(x)
        else:
            if self.head.getNext() is None:
                self.pos = Node(x, None)
                self.head.setNext(self.pos)
                self.tail = self.pos
            else:
                self.pos = Node(x, None)
                self.tail.setNext(self.pos)
                self.tail = self.pos

    def dequeue(self):
        if self.head.getNext() is None:
            self.head.setValue(None)
        else:
            self.head = self.head.getNext()


print('The Josephus Problem')
n = int(input('Enter the Number of People in the Group:\n'))
m = int(input('Enter value for Mth Person to be killed:\n'))


Q = Queue()
for i in range(n):
    Q.enqueue(i)

killed = []

for num in range(n):
    for i in range(m-1):
        Q.enqueue(Q.head.getValue())
        Q.dequeue()


    # print(str(Q.head.getValue()))
    killed.append(Q.head.getValue())
    Q.dequeue()

print('Order in which people are killed:')
for i in range(len(killed)):
    if i < len(killed)-1:
        print(killed[i], end=' ')
    else:
        print(killed[i], end='\n')