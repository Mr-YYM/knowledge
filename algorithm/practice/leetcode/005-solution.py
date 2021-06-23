class Solution:
    """
    动态规划
    """
    @staticmethod
    def get_longest_string(ss: set) -> str:
        longest_s = ""
        for each_s in ss:
            if len(each_s) > len(longest_s):
                longest_s = each_s
        
        return longest_s
    
    @staticmethod
    def isPalindrome(s: str) -> bool:
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        pass

print(Solution().longestPalindrome('ccbcc'))