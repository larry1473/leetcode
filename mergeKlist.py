# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
        def mergeKLists(self, lists):
            """
            :type lists: List[ListNode]
            :rtype: ListNode
            """
            if not lists:
               return None
            if len(lists) == 1:
                return lists[0]
            mid = len(lists) // 2
            left = self.mergeKLists(lists[:mid])
            right = self.mergeKLists(lists[mid:])
            return self.mergeSort(left, right)
                

            
            
        def mergeSort(self,res, mylist):
            resList = ListNode()
            resList_head = resList 
            if( not res):
                res = mylist
                return res 
            else:
                head_res = res
                head_list = mylist 
                
                while (head_res != None  and head_list != None):
                    if(head_res.val < head_list.val):
                        resList_head.next = ListNode(head_res.val)
                        resList_head = resList_head.next
                        head_res = head_res.next
                    elif(head_res.val > head_list.val):
                        resList_head.next = ListNode(head_list.val)
                        resList_head = resList_head.next
                        head_list = head_list.next
                    elif(head_res.val == head_list.val):
                        resList_head.next = ListNode(head_res.val)
                        resList_head = resList_head.next
                        resList_head.next = ListNode(head_list.val)
                        resList_head = resList_head.next
                        head_res = head_res.next
                        head_list = head_list.next
                if(head_res):
                    resList_head.next = head_res
                elif(head_list):
                    resList_head.next = head_list
                resList = resList.next
                return resList