# Question 1: Merge k Sorted Lists 
# You are given an array of k linkedlist heads, each list being sorted in ascending order. Write a function to merge all the lists into one sorted linked list and return its head. 

# Example: 

# Input: lists = [[1->4->5],[1->3->4],[2->6]] 

# Output: 1->1->2->3->4->4->5->6 

# Explanation: The merged linked list in ascending order.

import heapq

class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
    def __str__(self):
        result=[]
        curret=self
        while current:
            result.append(str(current.val))
            current=current.next 
        return result       
    
def mergeList(lists):
    min_heap=[]
    for i,node in enumerate(lists):
        if node:
            heapq.heappush(min_heap,(node.val,i,node))
    dummy=Node(0)
    current=dummy
    
    while min_heap:
        val,i,node = heapq.heappop(min_heap)
        current.next=node
        current=current.next
        if node.next:
            heapq.heappush(min,(node.next.val,i,node.next))
    return dummy.next                

def create_linked_list(lists):
    dummy=Node(0)
    current=dummy
    for num in lists:
        current.next=Node(num)
        current=current.next
    return dummy.next


lists = [[1,4,5],[1,3,4],[2,6]]
list1=create_linked_list(lists)    
merge_list=(mergeList(lists))

print("The merge lists are : ",mergeList)    

# print(mergeList(lists))        