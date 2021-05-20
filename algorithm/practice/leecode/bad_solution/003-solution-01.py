class Solution:
    """
    暴力解法，相比 00 写法优化了一下，这次不会超时，但是依然慢
    """
    def lengthOfLongestSubstring(self, s: str) -> int:

        def is_repeat(s: str) -> bool:
            """
            判断字符 s 是否存在重复字符
            """
            if len(set(s)) == len(s):
                return False
            else:
                return True

        string_len = len(s)
        if not string_len:
            return 0
        
        max_string_length = 0

        for i in range(string_len):
            for j in range(i, string_len):
                sub_string = s[i:j+1]
                if is_repeat(sub_string):  # 没有重复就...
                    break
                if len(sub_string) > max_string_length:
                    max_string_length = len(sub_string)
        
        return max_string_length
