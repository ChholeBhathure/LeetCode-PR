class Solution(object):
        def isPalindrome(self, x: int):
            s = str(x)
            num = len(s)
            left = 0
            right = num-1
            while left < right:
                    if s[left]!=s[right]:
                        return False
                    left += 1
                    right -= 1
            return True

        