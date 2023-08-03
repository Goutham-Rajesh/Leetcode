class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        c=1
        for r in range(len(nums)):
            if nums[r]==0:
                c-=1
            if c<0:
                if(nums[l]==0):
                    c+=1
                l+=1
        return r-l


        
        