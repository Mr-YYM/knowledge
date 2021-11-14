"""
990. 等式方程的可满足性
https://leetcode-cn.com/problems/satisfiability-of-equality-equations/

问题描述:
给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，
并采用两种不同的形式之一："a==b" 或 "a!=b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。

只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。 

"""

from typing import  List


class UF:
    """
    并查集
    """
    def __init__(self, node_count: int) -> None:
        """
        :n 节点个数
        """
        self.count = node_count  # 连通量
        # 节点 x 的节点是 parent[x]
        self.parent = [-1] * node_count  # 不同的节点
    
    def find(self, x: int):
        """
        寻找根节点
        """
        while x != self.parent[x]:  # 指向自己就是「根节点」
            x = self.parent[x]

        return x

    def union(self, p: int, q: int):
        """
        将 p 和 q 连接
        """
        root_p = self.find(p)
        root_q = self.find(q)

        # 如果他们是同一个根就不需要 union 了
        if root_p == root_q:
            return
        
        self.parent[root_p] = root_q
        
        # 通量 - 1
        self.count -= 1

    def is_connected(self, p: int, q: int) -> bool:
        """
        判断 p 和 q 是否连通
        """
        root_p = self.find(p)
        root_q = self.find(q)

        return root_p == root_q


def word_to_num(word: str) -> int:
    """
    a-z 转换成一个数字，方便存到数组中
    """
    return ord(word) - 97


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UF(node_count=26)  # 26 个字母
        # 初始化 uf
        for each_equation in equations:
            word1_num = word_to_num(each_equation[0])
            word2_num = word_to_num(each_equation[3])
            uf.parent[word1_num] = word1_num
            uf.parent[word2_num] = word2_num

        # 先处理 == 算式
        for each_equation in equations:
            if each_equation[1] == '=':
                word1_num = word_to_num(each_equation[0])
                word2_num = word_to_num(each_equation[3])
                uf.union(word1_num, word2_num)

        # 处理 != 算式，检查不等关系是否破坏了相等关系的连通性
        for each_equation in equations:
            if each_equation[1] == '!':
                word1_num = word_to_num(each_equation[0])
                word2_num = word_to_num(each_equation[3])

                # 如果他们本来相等的, 突然来一个 ! 那就返回 False
                if uf.is_connected(word1_num, word2_num):
                    return False
        
        return True


result = Solution().equationsPossible(["a==b","b!=a"])
# result = Solution().equationsPossible(["c==c","b==d","x!=z"])
print(result)
