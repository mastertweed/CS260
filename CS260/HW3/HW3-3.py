# Complete Implementation of this class

# Copy your Node class from the previous problem
# Complete Implementation of this class
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


# Use your Node Class to Implement a Stack
class Stack:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = self.head

    def __str__(self):
        if self.head.getValue() is None:
            return "Stack Empty"
        else:
            return "[ %d ]" % self.head.getValue()

    def top(self):
        return self.head.getValue()

    def pop(self):
        if self.head.getNext() is None:
            self.head.setValue(None)
        else:
            self.head = self.head.getNext()

    def push(self, x):
        if x != list():
            if self.head.getValue() is None:
                self.head.setValue(x)
                self.pos = self.head
            else:
                self.head = Node(x,self.pos)
                self.pos = self.head
        else:
            for i in range(len(x)):
                if self.head.getValue() is None:
                    self.head.setValue(x[i])
                    self.pos = self.head
                else:
                    self.head = Node(x[i], self.pos)
                    self.pos = self.head


    def empty(self):
        if self.head.getValue() is None:
            return True
        else:
            return False