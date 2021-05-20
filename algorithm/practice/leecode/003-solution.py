class Solution:
    """
    滑动窗口
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
        
        window_left = 0
        window_right = 0
        max_string_length = 0

        for i in range(string_len):
            window_right = i
            sub_string = s[window_left:window_right+1]
            print(window_left, window_right, sub_string)
            if is_repeat(sub_string):  # 没有重复就...
                window_left += 1
                continue
            if len(sub_string) > max_string_length:
                max_string_length = len(sub_string)
            
        
        return max_string_length
