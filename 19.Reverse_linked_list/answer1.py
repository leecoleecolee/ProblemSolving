# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # start와 end 포인트노드를 두고 생각해보자.
        # 만약 m = 3, n = 5 으로 들어오면 아래처럼 움직인다.
        # 1 - 2(start) - 3(end) - 4 - 5 - 6 - Null
        # 1 - 2(start) - 4 - 3(end) - 5 - 6 - Null
        # 1 - 2(start) - 5 - 4 - 3(end) - 6 - Null
        # m번째 node의 prev node를 start 노드로, start 노드 바로 다음 노드를 end 노드라고 생각하면, start 노드의 next로 end 노드의 next 노드를 m-n번 반복해서 이어붙이면 된다.

        if not head or m == n:
            return head

        root = start = ListNode(None, head)
        for _ in range(m - 1):
            start = start.next
        end = start.next

        for _ in range(n - m):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next
