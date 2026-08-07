class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posindex=0
        negindex=1
        n=len(nums)
        ans=[0]*n
        for i in range(0,n):
            if nums[i]>=0:
                ans[posindex]=nums[i]
                posindex+=2
            else:
                ans[negindex]=nums[i]
                negindex+=2
        return ans
        