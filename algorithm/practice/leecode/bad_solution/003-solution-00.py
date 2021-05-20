class Solution:
    """
    暴力解法，超长字串超出了处理时间限制
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
        
        not_repeat_lengths = []

        for i in range(string_len):
            for j in range(i, string_len):
                sub_string = s[i:j+1]
                if not is_repeat(sub_string):  # 没有重复就...
                    not_repeat_lengths.append(len(sub_string))
        
        return max(not_repeat_lengths)
