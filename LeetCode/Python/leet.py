#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.


def twoSum(nums,target): 
     pos = [ ]
     for i in range(len(nums)):
       j = i+1
       for j in range(j,len(nums)):
         if nums[i]+nums[j] == target:
           pos.append(i)
           pos.append(j)        
     return pos
print(twoSum(nums = [ 3, 2, 4],target = 6))