'''
* 문제
연결리스트를 홀수번 먼저 나열한 후 짝수번 이어지게.
in) 2->1->3->5->6->NULL
out) 2->3->6->1->5->NULL

* 풀이
홀수 노드와 짝수 노드를 만들어서 이어줌

* [x] 1회차
시간복잡도를 O(n) 안에 했다는 것은 알겠는데, 공간복잡도 O(1)을 모르겠다.
내 풀이가 leetcode를 통과하긴 했는데, 공간복잡도는 아직 어떻게 구하는지...
책의 풀이가 더 우아하긴 하니(나는 배열처럼 품), 나중에 익숙해지면 더 나아지길 기대해보자.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd_root = odd = ListNode(None)
        even_root = even = ListNode(None)

        index = 1
        while head:
            if index % 2 == 1:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
            index += 1
        
        even.next = None # NULL이 안되네. c랑 다르게 마지막을 어떻게 해줘야하는지 헷갈림.
        odd.next = even_root.next

        return odd_root.next

# ---
sol = Solution()

head = ListNode(2)
head.next = ListNode(1)
head.next.next = ListNode(3)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(6)

ret = sol.oddEvenList(head)

while ret:
    print (ret.val)
    ret = ret.next