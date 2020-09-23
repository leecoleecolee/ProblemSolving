'''
* 문제
연결리스트를 m부터 n까지 뒤집어라.
in) 1->2->3->4->5->NULL, m=2, n=4
out) 1->4->3->2->5->NULL

* [x] 1회차
연결리스트가 약간 이해는 된 상태라 시도는 해볼 수 있었지만, 정확하게 풀어낼 수는 없었다.
문제 해설을 보고 공부해서 나중에 다시 시도해야.

* [ ] 2회차
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        # 1 2 3 4 5, m=2, n=4
        # 1(s) 2(e) 3 4 5

        root = start = ListNode(None)
        start.next = head

        for _ in range(m - 1):
            start = start.next
        
        end = start.next

        # 시작 전: 1 2(e) 3 4 5
        # 1(s) 3 2(e) 4 5
        # 1(s) 4 3 2(e) 5

        for _ in range(n - m):
            tmp, tmp.next, end.next = end.next, start.next, end.next.next
            start.next = tmp # 일부러 책과 다르게 end.next를 tmp로 해봄. # 이 부분이 제일 헷갈리고 중요함.

        return root.next

# ---
sol = Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

ret = sol.reverseBetween(head, m=2, n=4)

while ret:
    print(ret.val)
    ret = ret.next