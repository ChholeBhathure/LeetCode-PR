class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n=len(nums)
        non_zero=[]
        for i in range(0,n):
            if nums[i]!=0:
                non_zero.append(nums[i])
                nums[i]=0
        for j in range(0,len(non_zero)):
            nums[j]=non_zero[j]
        