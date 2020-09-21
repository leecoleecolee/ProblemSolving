import collections

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ---
# class Solution: # 리스트와 슬라이싱을 이용한 방법
#     def isPalindrome(self, head: ListNode) -> bool:
#         # deque = collections.deque()
#         lst = []
#         curr = head

#         while curr:
#             # deque.append(curr.val)
#             lst.append(curr.val)
#             curr = curr.next

#         return lst == lst[::-1] # 뒤집지 않고 하나씩 꺼내서 비교하려면 deque가 효율적.

# ---
class Solution: # 런너를 이용한 방법: 런너 기법은 연결리스트에서 자주 쓰이므로, 이 문제에서는 오히려 어렵더라도 연습해둬야.
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        rev = None
        
        # 역순 연결리스트 rev 생성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
            # slow = slow.next를 다른 줄로 분리하면 틀림. rev = slow로 같은 객체를 참조하게 돼서?

        # 노드 홀수개면 slow를 한칸 전진
        if fast:
            slow = slow.next

        # 팬린드롬 검사
        while slow and (slow.val == rev.val): # slow나 rev 아무거나 상관 없는 듯.
            slow, rev = slow.next, rev.next

        return not slow # 여기도 마찬가지.

# ---
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(2)
# head.next.next.next = ListNode(1)

head = ListNode(1)
head.next = ListNode(2)

sol = Solution()
print (sol.isPalindrome(head))