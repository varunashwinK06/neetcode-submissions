class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new_s=sorted(s)
        new_t=sorted(t)
        if len(new_s) != len(new_t):
            return False
        for idx in range(len(s)):
            if new_s[idx]==new_t[idx]:
                continue
            else:
                return False
        return True
        