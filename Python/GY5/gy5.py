class Stack:
    def __init__(self):
        self.__stk = []
        
    def push(self, val):
        self.__stk.append(val)
    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val
    
class CountingStack(Stack):
    def __init__(self):
        super().__init__()
        self.__pop_counter = 0

    def get_counter(self):
        return self.__pop_counter
    
    def pop(self):
        super().pop()
        self.__pop_counter += 1
    
stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())


class QueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.queue = []
        
    def put(self, elem):
        self.queue.insert(0,elem)
        
    def get(self):
        if not self.__queue:
            raise QueueError("Queue is empty.")
        return self.__queue.pop()
    
que = Queue()
que.put(1)
que.put("dog")
que.put(False)

try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
    
import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y
    def getx(self):
        return self.__x
    def gety(self):
        return self.__y
    def distance_from_xy(self, x, y):
        return math.hypot(self.__x - x, self.__y - y)
    def distance_from_point(self, point):
        return math.hypot(self.__x - point.getx(), self.__y - point.gety())
    
point1 = Point(0, 0)
point2 = Point(1, 1)

print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))