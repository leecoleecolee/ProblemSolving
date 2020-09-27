# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []
        
        for i in range(len(lists)):
            if lists[i]:
                # haep[0] = [li.val, index, li.next]
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        print(heap)
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2] # result는 ListNode
            
            result = result.next
            #print("result: ", result)
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))
                #print(heap)
                
        return root.next
