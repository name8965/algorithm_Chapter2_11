class MyCircularQueue:

    def __init__(self, k: int):
        self.maxsize = k
        self.data = [None]*k
        self.head = 0
        self.tail = -1
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.tail = (self.tail+1)%self.maxsize
            self.data[self.tail] = value
            self.size+=1
            return True
        else:
            return False
    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.data[self.head] = None
            self.head = (self.head+1)%self.maxsize
            self.size-=1
            return True
        else:
            return False

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.tail]

    def isEmpty(self) -> bool:
        return self.size==0

    def isFull(self) -> bool:
        return self.size==self.maxsize

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

# MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue = MyCircularQueue(3)
# print(myCircularQueue.isFull())
print(myCircularQueue.enQueue(1) )
print(myCircularQueue.enQueue(2) )
print(myCircularQueue.enQueue(3) )
print(myCircularQueue.enQueue(4) )
print(myCircularQueue.Rear()    )
print(myCircularQueue.isFull()  )
print(myCircularQueue.deQueue() )
print(myCircularQueue.enQueue(4) )
print(myCircularQueue.Rear()   )
# m = MyCircularQueue(6)
# # print(myCircularQueue.isFull())
# print(m.enQueue(6))  #True
# print(m.Rear())      #6
# print(m.Rear())      #6
# print(m.deQueue())   #True
# print(m.enQueue(5))  #
# print(m.Rear())      #
# print(m.deQueue())   #
# print(m.Front())     #
# print(m.deQueue())   #
# print(m.deQueue())   #
# print(m.deQueue())   #
#
#
#
# m = MyCircularQueue(3)
# # print(myCircularQueue.isFull())
# print(m.enQueue(1))  #True
# print(m.enQueue(2))  #True
# print(m.enQueue(3))  #True
# print(m.Rear())      #6
# print(m.Rear())      #6
# print(m.deQueue())   #True
# print(m.enQueue(5))  #
# print(m.Rear())      #
# print(m.deQueue())   #
# print(m.Front())     #
# print(m.deQueue())   #
# print(m.deQueue())   #
# print(m.deQueue())   #
