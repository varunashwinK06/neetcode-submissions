class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts={}
        freq= [ [] for i in range(len(nums)+1)]
        for num in nums:
            counts[num]=counts.get(num, 0) +1 
        for n, c in counts.items():
            freq[c].append(n)
        
        end=[]
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                end.append(n)
                if len(end) == k:
                    return end


        
        
        
        
        