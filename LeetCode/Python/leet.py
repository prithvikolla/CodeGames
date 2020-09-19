  #Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

  #You may assume that each input would have exactly one solution, and you may not use the same element twice.

  #You can return the answer in any order.


# def twoSum(nums,target): 
#       pos = [ ]
#       for i in range(len(nums)):
#         j = i+1
#         for j in range(j,len(nums)):
#           if nums[i]+nums[j] == target:
#             pos.append(i)
#             pos.append(j)        
#       return pos
# print(twoSum(nums = [ 3, 2, 4],target = 6))

    # palindrome multiplication with three digit numbers in reverse order

class Node:
    def __init__(self, dataval= None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
        
list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Now link first node to the second one

list1.headval.nextval = e2

# Link second node to the third node

e2.nextval = e3
        
