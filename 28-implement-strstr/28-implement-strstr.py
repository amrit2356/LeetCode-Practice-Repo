class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 0 and len(needle) == 0:
            return 0
        else:
            return haystack.find(needle)