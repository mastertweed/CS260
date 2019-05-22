import math


class heap:
    def __init__(self):
        self.data = []

    def __str__(self):
        res=""
        for x in self.data:
            res=res+str(x)+" "
        return res

    def makenull(self):
        self.data = []

    def insert(self,x):
        self.data.append(x)
        self.upheap(len(self.data)-1)

    def parent(self,index):
        return math.floor((index-1)/2)

    def left(self,index):
        return (index+1)*2-1

    def right(self,index):
        return (index+1)*2

    def swap(self,a,b):
        self.data[a], self.data[b] = self.data[b], self.data[a]

    def upheap(self,index):
        if index != 0:
            temp = self.parent(index)
            if self.data[index] < self.data[temp]:
                self.swap(index,temp)
                self.upheap(temp)

    def downheap(self,index):
        temp = self.left(index)
        if self.data[index] > self.data[temp]:
            self.swap(index,temp)
            self.downheap(temp)

    def inorder(self,index):
        if index < len(self.data):
            self.inorder(self.left(index))
            print(self.data[index],end=" ")
            self.inorder(self.right(index))
        return ''

    def preorder(self,index):
        if index < len(self.data):
            print(self.data[index],end=" ")
            self.preorder(self.left(index))
            self.preorder(self.right(index))
        return ''

    def postorder(self,index):
        if index < len(self.data):
            self.postorder(self.left(index))
            self.postorder(self.right(index))
            print(self.data[index],end=" ")
        return ''

    def min(self):
        return self.data[0]

    def deletemin(self):
        self.data[0] = self.data.pop(-1)
        self.downheap(0)

    def sort(self):
        self.data.sort()
        for i in range(len(self.data)):
            print(self.data[i])
