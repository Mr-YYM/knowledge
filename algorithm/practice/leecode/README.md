# Leecode 算法解题

## 解题思路

- [1.两数之和](https://leetcode-cn.com/problems/two-sum/)

- [3.无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

    滑动窗口算法可以用以解决数组/字符串的子元素问题，它可以将嵌套的循环问题，转换为单循环问题，降低时间复杂度。

    - 思路

        先移动 right，再移动 left…… 直到 right 指针到达字符串 S 的末端，算法结束

- [836.矩形重叠](https://leetcode-cn.com/problems/rectangle-overlap/)

    使用题解提供的思路：投影法，找出所有不重叠的情况，not 一下就是重叠的情况了。

    [836-solution.py](https://github.com/Mr-YYM/knowledge/blob/main/algorithm/practice/leecode/836-solution.py)

    投影法图示：

    ![](https://pic.leetcode-cn.com/255e661fd9bedddd608546a12f10f0d83bab7092e7fc5cda0c76a58540d5b9b9.jpg)