# 스택을 이용한 큐 구현

# push() : 요소 x를 큐 마지막에 삽입한다.
# pop() : 큐 처음에 있는 요소를 제거한다.
# peek() : 큐 처음에 있는 요소를 조회한다.
# empty() : 큐가 비어 있는지 여부를 리턴한다.

# MyQueue queue = MyQueue()

# queue.push(1);
# queue.push(2);
# queue.peek() // 1 리턴
# queue.pop() // 1 리턴
# queue.empty() // false 리턴


# stack 은 후입 선출이다.
# queue 는 선입 선출이다.
#
# stack을 이용해서 queue를 구현할려면
#
# stack을 push를 여러번 하면 우물에 쌓이게 된다.
#
# 다른 stack 에 원래 stack 의 값을 거꾸로 담는다.
#
# stack 이 두개가 필요하겠다.
#
# stack1 에 push를 한다면 stack1의 값을 pop을 해와서 stack2에 담는다.


class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, val):
        self.input.append(val)

    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output.pop()

    def pop(self):
        self.peek()
        return self.output.pop()

    def empty(self):
        return self.input is None and self.output is None







