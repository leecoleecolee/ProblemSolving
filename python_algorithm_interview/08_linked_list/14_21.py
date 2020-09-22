'''
* 문제
정렬되어 있는 두 연결리스트를 병합하라.
in) 1->2->4, 1->3->4
out) 1->1->2->3->4->4

* 풀이 방법
1) 재귀
2) 반복

* [x] 1회차
책의 재귀 풀이는 이해가 직관적으로 와닿지는 않는다. https://leetcode.com/problems/merge-two-sorted-lists/discuss/321108/21python-omn-time-omn-space-solution 링크의 재귀 풀이는 꽤 직관적이라 연습하기 좋다. (이런건 백트래킹이 아닌가?)
다른 방법으로도 풀어보고 싶은 문제. 특히 반복으로...

* [ ] 2회차
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # --- 책의 풀이. 노드를 스왑한다는 개념이 생소해서 재귀가 더 어려움.
        # if not l1 or l2 and l1.val > l2.val:
        #     l1, l2 = l2, l1
        # if l1:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        #     # self.mergeTwoLists(l1.next, l2) # 이렇게 하면 1->2->4
        # return l1

        # --- 반복으로 풀려는 시도. 다른 방법으로는 못 푸니까, 아직 100퍼센트 이해가 아님.
        # head = l1
        # while l1:
        #     if l2 and l1.val > l2.val:
        #         l1, l2 = l2, l1
        #     l1 = l1.next
        # return head

        # --- https://leetcode.com/problems/merge-two-sorted-lists/discuss/321108/21python-omn-time-omn-space-solution 의 두번째(재귀) 풀이. 책의 재귀보다 이해가 쉽다.
        if not l1 or not l2:
            output = l1 or l2
            return output
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next) # 이해 돕기 위해, 사이트의 코드를 약간 수정.
            return l2 # 리턴을 바로바로 해줘서 이해가 수월하다.

# ---
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(4)

head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)

sol = Solution()
ret = sol.mergeTwoLists(head1, head2)

while ret:
    print (ret.val)
    ret = ret.next

# ---
# 아직 100퍼센트 이해가 아니므로 공부가 필요함.
# https://leetcode.com/problems/merge-two-sorted-lists/discuss/321108/21python-omn-time-omn-space-solution