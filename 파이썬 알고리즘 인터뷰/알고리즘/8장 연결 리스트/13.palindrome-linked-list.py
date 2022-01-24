# 팰린드롬 연결 리스트

# 연결 리스트가 팰린드롬 구조인지 판별하라

# 리스트 변환
import collections
from typing import List, Optional, Deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(head: Optional[ListNode]) -> bool:
    q: List = []

    if not head:
        return  True

    node = head

    # 리스트 변환

    while node is not None:
        q.append(node.val)
        node= node.next

    # 팰린드롬 판별

    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True

# 데크를 이용한 최적화

def solve2(head: ListNode) -> bool:
    # 데크 자료형 선언
    q: Deque = collections.deque()

    if not head:
        return True

    node = head

    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True
