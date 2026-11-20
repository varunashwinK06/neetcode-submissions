class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      s_array = defaultdict(int)
      for c in s:
        s_array[c]+=1
      t_array = defaultdict(int)
      for c in t:
        t_array[c]+=1
      if s_array == t_array:
        return True
      return False



        