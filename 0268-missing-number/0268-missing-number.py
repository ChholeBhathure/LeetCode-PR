class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        total=0
        sum=0
        for i in range(0,n+1):
            total=total+i
        for j in nums:
            sum=sum+j
        return total-sum
        