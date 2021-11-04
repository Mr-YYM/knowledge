"""
5. 最长回文子串
https://leetcode-cn.com/problems/longest-palindromic-substring/

问题描述:
给你一个字符串 s，找到 s 中最长的回文子串。

我的解体思路:
1. 使用中心扩散的思想解答
2. 注意这个中心包含以两个字符为中心

过程中遇到的问题:

执行用时：696 ms, 在所有 Python3 提交中击败了86.36%的用户内存消耗：15 MB, 
在所有 Python3 提交中击败了83.98%的用户
通过测试用例：180 / 180

"""

class Solution:
    """
    动态规划
    """
    def palindrome(self, s: str, l: int, r: int) -> str:
        """
        获取字符串 s，以 l,r 为中心的最长的回文串
        """
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        # s[l:r+1] 是不对的。因为只有当遇到不匹配的时候才会退出循环。
        # 就是说 l 是多减了一次 1 r 多加了一次 1
        return s[l+1:r]

    def longestPalindrome(self, s: str) -> str:
        result = ''
        for i in range(len(s)):
            # 以 s[i] 为中心
            pi = self.palindrome(s, i, i)
            # 以 s[i, i+1] 为中心
            pi1 = self.palindrome(s, i, i+1)

            if len(pi) > len(result):
                result = pi
            
            if len(pi1) > len(result):
                result = pi1
        
        return result

result = Solution().longestPalindrome('aaacccaaa')
print(result)
