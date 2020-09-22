'''
* 문제
두 연결리스트를 합친 연결리스트를 구하는 문제.
in) 1->5->5, 2->6->1
out) 3->1->7

* 풀이 방법
1) 전가산기 원리로 구현
2) 자료형 변환

* [x] 1회차
난이도가 별 두개임에도 어렵지는 않다.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # --- 1) 전가산기 원리로 구현
        # tmp = 0
        # ret = ret_head = ListNode(None)

        # while l1 or l2:
        #     if not l1 or not l2: # 둘 중에 하나만 있으면
        #         node_tmp = l1 or l2
        #         ret.val = node_tmp.val
        #         # ret.val = l1.val or l2.val # 이렇게는 안됨
        #     else: # 둘 다 있으면
        #         ret.val = l1.val + l2.val
        #     ret.val += tmp
        #     tmp = ret.val // 10
        #     ret.val = ret.val % 10
        #     if l1:
        #         l1 = l1.next
        #     if l2:
        #         l2 = l2.next
        #     if l1 or l2 or tmp:
        #         ret.next = ListNode(None)
        #         ret = ret.next
        
        # if tmp:
        #     ret.val = tmp
        
        # return ret_head

        # --- 1+) 보완
        # up = 0
        # ret = ret_head = ListNode(None)

        # while l1 or l2 or up:
        #     sum = 0
        #     if l1:
        #         sum += l1.val
        #         l1 = l1.next
        #     if l2:
        #         sum += l2.val
        #         l2 = l2.next
        #     sum += up
        #     up = sum // 10 # 몫
        #     sum = sum % 10 # 나머지
        #     ret.next = ListNode(sum)
        #     ret = ret.next
        
        # return ret_head.next

        # --- 2) 자료형 변환
        l1_str = ""
        l2_str = ""

        while l1:
            l1_str += str(l1.val)
            l1 = l1.next
        
        while l2:
            l2_str += str(l2.val)
            l2 = l2.next

        l1_str = l1_str[::-1]
        l2_str = l2_str[::-1]

        l1_int = int(l1_str)
        l2_int = int(l2_str)

        ret_str = str(l1_int + l2_int)[::-1]
        node = head = ListNode(None)

        for ret_char in ret_str:
            node.next = ListNode(int(ret_char))
            node = node.next
        
        return head.next

# ---
sol = Solution()

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# l1 = ListNode(1)
# l1.next = ListNode(8)
# l2 = ListNode(0)

ret = sol.addTwoNumbers(l1, l2)

while ret:
    print (ret.val)
    ret = ret.next