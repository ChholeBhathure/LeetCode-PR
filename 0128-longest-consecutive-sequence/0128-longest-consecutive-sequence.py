class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result=set(nums)
        n=len(nums)
        longest=0
        for num in result:
            if num-1 not in result:
                x=num
                count=1
                while x+1 in result:
                    count+=1
                    x+=1
                longest=max(longest,count)
        return longest

        