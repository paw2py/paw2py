#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

 

#Example 1:

 #Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Output: Because nums[0] + nums[1] == 9, we return [0, 1]
   
   #Solution 1: using list
   def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []        
        for idx, val in enumerate(nums):
            # a+b = t --> b= t-a
            try:
                idy = nums.index(target - val,idx+1)
                result.extend([idx,idy])
                #print(result)
            except ValueError:
                i = 0
        return result 
        
    #Solution 2: using dictionary     
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        #print (nums)
        #print(target)
        for idx, val in enumerate(nums):
            # a+b = t --> b= t-a
            b = target - val
            if b in result:
                return[result[b],idx]
            result[val] = idx
    
###########################################
rud_feature: 1st commit    
