import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        str1 = collections.Counter(s)
        str2 = collections.Counter(t)

        return str1 == str2

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         if sorted(s) == sorted(t):
#             return True


