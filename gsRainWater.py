"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        l_maxht = 0
        r_maxht = 0
        l = 0
        r = len(height) - 1
        wt_unit = 0
        
        while l < r:
            if height[l] < height[r]:
                if height[l] >= l_maxht:
                    l_maxht = height[l]
                else:
                    wt_unit += l_maxht - height[l]
                l +=1  
            else:
                if height[r] >= r_maxht:
                    r_maxht = height[r]
                else:
                    wt_unit +=  r_maxht - height[r]
                r -= 1
        return wt_unit        
