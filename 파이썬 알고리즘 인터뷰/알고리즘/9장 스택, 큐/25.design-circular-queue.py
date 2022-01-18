# 원형 큐 디자인

# 원형 큐를 디자인하라


# MyCircularQueue(5) // 크기를 5로 지정
#
# enQueue(10) // true 리턴
# enQueue(20) // true 리턴
# enQueue(30) // true 리턴
# enQueue(40) // true 리턴
#
# Rear() // 40 리턴
#
# isFull() // false 리
#
# deQueue() // true 리턴
# deQueue() // true 리턴
#
# enQueue(50) // true 리턴
# enQueue(60) // true 리턴
#
# Rear() // 60
#
# Front() // 30

class MyCircularQueue:
    # 큐는 선입선출
    # 원형 큐의 크기, 리어포인트, 프론트포인트

    def __init__(self, k:int):
        self.queue = k*[None]
        self.maxlen = k
        self.rear = 0
        self.front = 0

    #  enQueue를 하면 rear값이 val로 옮겨진다.
    def enQueue(self, val:int) -> bool:
        if self.queue[self.rear] is None:
            self.queue[self.rear] = val
            self.rear = (self.rear + 1) % self.maxlen
            # self.rear +=1 을 했었는데 무한으로 늘어나서 어떻게 해야 될지 몰랐다.
            # if self.rear < self.maxlen:
            #     self.rear += 1
            # else:
            #     self.rear = 0
            # 이 방법도 안되서... 답을 보니 나머지 값으로 구했다.
            return True
        else:
            return False


    #  deQueue를 하면 맨 처음 값을 지우고 front 값이 된다
    def deQueue(self) -> bool:
        if self.queue[self.front] is None:
            return False
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.maxlen
            # self.front +=1
            return True

    def Front(self) ->int:
        return -1 if self.queue[self.front] is None else self.queue[self.front]

    def Rear(self) -> int:
        return -1 if self.queue[self.rear - 1] is None else self.queue[self.rear - 1]

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.queue[self.front] is None

    def isFull(self) -> bool:
        return self.front == self.rear and self.queue[self.front] is not None

