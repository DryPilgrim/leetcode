class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# ————————————————version 1————————————————————

# #
# # 
# # @param head ListNode类 
# # @return bool布尔型
# #
# class Solution:
#     """
#     判断一个链表是否有环。
#     """
#     def hasCycle(self , head: ListNode) -> bool:
#         p = ListNode
#         # 假定各节点的值不重复
#         values = []

#         # p.next == null, exit
#         while p.next:
#             # p.nexy != null
#             if p.val in values:
#                 return True 
#             values.append(p.val)
#             p = p.next
#         return False

# ————————————————version 2————————————————————


# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         if not head:
#             return False
#         slow = head
#         fast = head.next
#         iter = 0
#         while slow != fast:
#             iter += 1
#             if not fast or not fast.next:
#                 return False
#             slow = slow.next
#             fast = fast.next.next
#         return True, iter

class Solution:
    """
    判断一个链表是否有环，如果有环，则返回环的起始点; 如果没有环, 则返回-1.
    快慢指针。
    ref: https://mp.weixin.qq.com/s/IrUnU3OcN_htEjEXw9Nwyg
    """
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            # 如果有环，一个指针从头开始，一个指针从相遇点开始
            if slow == fast:
                head = head.next
                slow = slow.next
                while head != slow:
                    head = head.next
                    slow = slow.next
                return slow
        return -1

# 创建链表节点
node0 = ListNode(0)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

# 构建循环：node5 -> node2
node5.next = node3

# 构建链表：1 -> 2 -> 3 -> 4 -> 5 -> 2 (循环)
head = node0
node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# 创建Solution对象
solution = Solution()
# 检测链表是否有循环
result= solution.hasCycle(head)
print( result.val)  # 输出 True
