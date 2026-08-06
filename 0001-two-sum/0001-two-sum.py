class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        present={}
        for i in range(0,n):
            remaining=target-nums[i]
            if remaining in present:
                return [present[remaining],i]
            present[nums[i]]=i
        