class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracker_dict=defaultdict(int)
        for num in nums:
            if tracker_dict[num] == 1:
                return True
            else:
                tracker_dict[num] += 1
        return False
        
    
        