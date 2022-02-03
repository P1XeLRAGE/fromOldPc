import pandas as pd
import numpy as np
import math


# Пример на константное время выполнения O(1)

"""
def is_odd(n):
    if n % 2 == 0:
        return 'n is odd'
    else:
        return "n isn't odd"


print(is_odd(int(input())))
"""


# Пример на дважды логарифмическое время O(log(log(n)))

"""
def Newton_root(n):
    x = n
    c = 0
    l = 0.00001
    while True:
        c += 1
        ans = 0.5 * (x + (n / x))
        if abs(ans - x) < l:
            break
        x = ans

    return ans


def from_num_to_zero(n, k):
    l = 1.001
    if n <= l:
        return k
    else:
        k += 1
        from_num_to_zero(math.sqrt(n), k)


k = 0
print(from_num_to_zero(int(input()), k))
"""


# Хороший примерчик на логарифмическое время
# самый быстрый способ засортить что-то -- это использовать
# mergesort алгоритм, который заключается в рекурсивной
# сортировке путем деления листа на две части и проверки
# каждой части по отдельности, когда длина каждой достигнет
# 1. Время выполнения такого алгоритма O(log(n)). Реализация
# этого алгоритма будет происходить с помощью библиотеки
# operator. Function operator.lt is equivalent to <.


"""
import operator

def merge_sotring(l, comp=operator.lt):
    if len(l) < 2:
        return l[:]
    else:
        mid = int(len(l)/2)
        left = merge_sotring(l[:mid], comp)
        right = merge_sotring(l[mid:], comp)
        return merge(left, right, comp)


def merge(l, r, c):
    ans = []
    i, j = 0, 0
    while i < len(l) and j < len(r):
        if c(l[i], r[j]):
            ans.append(l[i])
            i += 1
        else:
            ans.append(r[j])
            j += 1

    while i < len(l):
        ans.append(l[i])
        i += 1
    while j < len(r):
        ans.append(r[j])
        j += 1
    return ans

array = [78, 41, 4, 27, 3, 27, 8, 39, 19, 34, 6, 41, 13, 52, 16]
print(merge_sotring(array))"""


# Пример для Ленейно-логарифмисекого времни выполнения O(nlog(n))
# Также быстрым способом сортировки является алгоритм quick_sort,
# который отличается от merge_sort и реализацией, и временем
# выполнения. Его принцип заключается в рекурсивном делении
# листа на половинки до тех пор, пока мы не дойдем до 0 или 1,
# но в этот раз мы по-другому делим эти массивы. Берем первый
# элемент, а затем составляем два списка. Первый меньше этого
# члена, второй больше. Затем то же самое с этими двумя и тд.

"""
def partition(a, b, e):
    p = b
    for i in range(b + 1, e + 1):
        if a[i] <= a[b]:
            p += 1
            a[i], a[p] = a[p], a[i]
    a[p], a[b] = a[b], a[p]
    return p


def quick_sort(a, b=0, e=None):
    if e is None:
        e = len(a) - 1

    def _quicksort(array, b, e):
        if b >= e:
            return
        p = partition(array, b, e)
        _quicksort(array, b, p - 1)
        _quicksort(array, p + 1, e)

    return _quicksort(a, b, e)

array = [29,19,47,11,6,19,24,12,17,23,11,71,41,36,71,13,18,32,26]
print(quick_sort(array))
"""


# 75 LeetCode problems for coding interview


# 1. Two sum:

"""
class Solution(object):
    def twoSum(self, nums, target):
        dicy = dict()
        for i in range(len(nums)):
            n = nums[i]
            differ = target - n
            if n in dicy:
                return [dicy[n], i]
            else:
                dicy[differ] = i


nums = [2, 7, 5, 2, 2]
diff = 7
nums_as_dict = dict(zip(nums, range(0, len(nums))))
print(nums_as_dict)
"""


# 2. Longest substring without repeating characters:
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         set_s = set()
#         max_i = 0
#         maxi_i = 0
#         if len(s) == 1:
#             return 1
#         for i in range(len(s)):
#             if s[i] in set_s:
#                 if maxi_i > max_i:
#                     max_i = maxi_i
#                 maxi_i = 1
#                 set_s.clear()
#                 set_s.add(s[i])
#             else:
#                 maxi_i += 1
#                 set_s.add(s[i])
#                 if maxi_i > max_i:
#                     max_i = maxi_i
#         return max_i


# LeetCode: Palindrome Number
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         l = []
#         if x < 0:
#             return False
#         else:
#             while True:
#                 c = x % 10
#                 l.append(c)
#                 x = x // 10
#                 if x == 0:
#                     break
#
#         for n in range(len(l) // 2):
#             if l[n] != l[len(l) - n - 1]:
#                 return False
#         return True


# LeetCode: Roman to Integer
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         ans = 0
#         for x in range(len(s)):
#             if s[x] == "M":
#                 if x != 0 and s[x - 1] == "C":
#                     ans += 900
#                 else:
#                     ans += 1000
#             elif s[x] == "D":
#                 if x != 0 and s[x - 1] == "C":
#                     ans += 400
#                 else:
#                     ans += 500
#             elif s[x] == "C":
#                 if x != 0 and s[x - 1] == "X":
#                     ans += 90
#                 elif x != len(s) - 1 and (s[x + 1] == "M" or s[x + 1] == "D"):
#                     pass
#                 else:
#                     ans += 100
#             elif s[x] == "L":
#                 if x != 0 and s[x - 1] == "X":
#                     ans += 40
#                 else:
#                     ans += 50
#             elif s[x] == "X":
#                 if x != 0 and s[x - 1] == "I":
#                     ans += 9
#                 elif x != len(s) - 1 and (s[x + 1] == "L" or s[x + 1] == "C"):
#                     pass
#                 else:
#                     ans += 10
#             elif s[x] == "V":
#                 if x != 0 and s[x - 1] == "I":
#                     ans += 4
#                 else:
#                     ans += 5
#             elif s[x] == "I":
#                 if x != len(s) - 1 and (s[x + 1] == "X" or s[x + 1] == "V"):
#                     pass
#                 else:
#                     ans += 1
#         return ans



# LeetCode: Longest Common Prefix
# class Solution:
#     def longestCommonPrefix(self, strs: list[str]) -> str:
#         ans = {}
#         s = list(strs[0])
#         d = {x: x for x in range(len(s))}
#         for i in range(len(s)):
#
#
#         return ''.join(ans)
#
# def longestCommonPrefix(strs: list[str]):
#     ans = []
#     s = strs[0]
#     for i in range(len(s)):
#         for j in range(1, len(strs)):
#             if i == len(strs[j]) - 1:
#                 if s[i] == strs[j][i]:
#                     ans.append(s[i])
#                     return ''.join(ans)
#                 else:
#                     return ''.join(ans)
#             if s[i] == strs[j][i]:
#                 pass
#             else:
#                 return ''.join(ans)
#         ans.append(s[i])
#
#     return ''.join(ans)
#
# print(longestCommonPrefix(["ab", "a"]))


# LeetCode: Add Two Numbers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: list[int], l2: list[int]) -> list[int]:
        def list_to_num(l: list[int]) -> int:
            n = 0
            for i in reversed(range(len(l))):
                n += (l[i] * 10 ** i)
            return n

        def num_to_list(n: int) -> list[int]:
            l = []
            while True:
                l.append(n % 10)
                n = n // 10
                if n == 0:
                    break
            return l

        s = list_to_num(l1) + list_to_num(l2)
        return num_to_list(s)


# LeetCode: Zigzag Conversion




# Второй этап собеса в Яндекс:



# def is_palindrome(s: str) -> bool:
#     # your code here
#     b, e = 0, len(s) - 1
#
#     #s = 'abcabc'
#     # b = 0, e = 5
#     k = e // 2
#     i = 0
#     s = s.lower()
#     while b < e:
#         if s[b] == s[e]:
#             b += 1
#             e -= 1
#         else:
#             return False
#         i += 1
#         if k == i:
#             return True




# Дано целое число (int), нужно посчитать сумму цифр.
# Input: 123 Output: 6
# Input: 23 Output: 5



# def sum_digits(value: int) -> int:
#     s = 0
#     while True:
#         s += value % 10
#         value = value // 10
#         if value == 0:
#             break
#
#     return s

# s = "au"
# print(lengthOfLongestSubstring(s))

# 3. Longest palindromic substring:


# 4. Container with most water:


# 5. 3Sum:


# 6. Remove Nth node from end of list:


# 7. Valid parentheses:


# 8. Merge two sorted lists:


# 9. Merge k sorted lists:


# 10. Search in rotated sorted array:


# 11. Combination sum:


# 12. Rotate image:


# 13. Group anagrams:


# 14. Maximum subarray:


# 15. Spiral matrix:


# 16. Jump game:


# 17. Merge intervals:


# 18. Insert interval:


# 19. Unique paths:


# 20. Climbing stairs:
