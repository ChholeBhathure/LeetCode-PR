class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        maximum=0
        for i in range (0,n):
            if nums[i]==1:
                count+=1
            else:
                if count>maximum:
                    maximum=count
                count=0
            
        if maximum<count:
            maximum=count
        return maximum
                

        