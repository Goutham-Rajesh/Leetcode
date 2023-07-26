class Solution:
    def maxArea(self, height: List[int]) -> int:
        m=0
        i,j= 0, len(height) - 1
        while i<j:
            a=min(height[i],height[j])*(j-i)
            m=max(m,a)
            if(height[j]>height[i]):
                i+=1
            else:
                j-=1
        return m
                
        