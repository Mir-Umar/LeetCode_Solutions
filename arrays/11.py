"""
11. Container With Most Water
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height)-1
        area = 0
        for i in range(len(height)):
            area1= min(height[p1],height[p2]) * (p2-p1)
            if area1>area:
                area= area1
            if height[p1]>height[p2]:
                p2=p2-1
            else:
                p1 = p1+1
        return area
        
