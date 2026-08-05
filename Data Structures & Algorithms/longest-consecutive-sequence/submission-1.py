class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number_map=set(nums)
        longest=0
        for num in number_map:
            if num-1 not in number_map:
                length=0
                while (num+length) in number_map:
                    length +=1
                if length > longest:
                    longest=length
        return longest

                

        
            