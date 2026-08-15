class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_array=defaultdict(int)
        for c in s:
            s_array[c]+=1
        t_array=defaultdict(int)
        for c in t:
            t_array[c]+=1
        for key in t_array:
            if s_array[key] == 0 or t_array[key] != s_array[key]:
                return False
        for key in s_array:
            if t_array[key] == 0 or t_array[key] != s_array[key]:
                return False
        return True



        