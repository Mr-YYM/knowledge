import time

def count_time(func):
    count_time.level = 0
    def wrap(*args, **kwargs):
        count_time.level += 1

        start_time  = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print(f' {func.__name__} in depth {count_time.level} total_time:', end_time - start_time)

        return result
    
    return wrap


class Solution:
    """
    暴力解法
    """
    
    @staticmethod
    def get_loggest_string(ss: set) -> str:
        loggest_s = ""
        for each_s in ss:
            if len(each_s) > len(loggest_s):
                loggest_s = each_s
        
        return loggest_s
    
    @staticmethod
    def isPalindrome(s: str) -> bool:
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:        
        s_length = len(s)
        if s_length < 2:
            return s

        all_palindrom = set()
        # 找出所有字串
        for i in range(s_length):
            for j in range(i, s_length):
                if self.isPalindrome(s[i:j+1]):
                    all_palindrom.add(s[i:j+1])
        return self.get_loggest_string(all_palindrom)

print(Solution().longestPalindrome("adb"))