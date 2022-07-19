#Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        lft = 0
        rht = len(height) - 1
        
        
        while lft <= rht:
            weidth = rht - lft
            area = max(area,min(height[lft],height[rht]) * weidth)
            if height[lft] <= height[rht]:
                lft += 1
            else:
                rht -= 1
        
        return area
