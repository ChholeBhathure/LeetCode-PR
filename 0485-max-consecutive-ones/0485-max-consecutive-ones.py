class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        maximum=0
        for i in range (0,n):
            if nums[i]==1:
                count+=1
            else:
                maximum=max(maximum,count)
                count=0
            
        return max(maximum,count)
                

        