Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[1] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        temp ={'res':[]}
        
        for i in range(len(nums)-1):
            if nums[i] not in temp or nums[i+1] not in temp:
                temp[nums[i]] = 1
                temp[nums[i+1]] = 1
            tgt1 = nums[i] + nums[i+1]
            z = 0 - tgt1
            if z in nums:
                if z not in temp: 
                    temp[z] = 1
                    temparr = [nums[i] ,nums[i+1],z]
                    temparr.sort()
                    temp['res'] += [temparr]
                else:
                    temparr = [nums[i] ,nums[i+1],z]
                    temparr.sort()
                    if temparr not in temp['res']:
                        temp['res'] += [temparr]
                    
                    
                
                
                
                
        return temp['res']  
            
            
        
        
