class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s=0
        for i  in range(len(nums)):
            if(nums[i]!=0 and nums[s]==0):
                nums[s],nums[i]=nums[i],nums[s]
            if(nums[s]!=0):
                s+=1
       

        
        