class ListNode:
    def __init__(self, key: int = None, value: int = None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    #     key, value --> hashfunction key값을 conversion hashkey    0~9 % 10  --> 4, 14
    #  chaining  4 first --> second --> third
    #  openaddress  max_table 4(이미 있다) 5 6 7(이 곳에 new를 넣는다) 8(7new) 9 10
    #  들어가있는 키 개수 / 전체공간 ==> 로드팩터 (0.몇으로 제한) 성능이 보장되도록

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.table = collections.defaultdict(ListNode)
#         hashfunction : key % self.size --> hashkey

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hashkey = key % self.size
#         case1: hashkey 인덱스 위치에 값이 없는 경우
        if self.table[hashkey].value is None:
            self.table[hashkey] = ListNode(key, value)
            return

#         case2: hashkey 인덱스 위치에 값이 없는 경우
        node = self.table[hashkey]
        while node:
            if node.key == key:
                node.value = value
                return
            if node.next is None:
                break
            node = node.next

        node.next = ListNode(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        # hashkey = key % self.size
        # if self.table[hashkey].value is None:
        #     return -1

        node = self.table[hashkey]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        #         case1: hashkey 인덱스 위치에 값이 없는 경우
        hashkey = key % self.size
        if self.table[hashkey].value is None:
            return
#         case2: 값이 있는데, hasykey 인덱스 위치가 첫번째인 경우

        #         case3: hashkey 인덱스 위치에 값이 없는 경우
        node = self.table[hashkey]
        prev = None
        while node:
            if node.key == key:
                if prev is None:
                    self.table[hashkey] = node.next if (
                        node.next is not None) else (ListNode())
                    # node.next = (node.next is not None) ? (node.next) : (ListNode())
                else:
                    prev.next = node.next
                return
            prev, node = node, node.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
