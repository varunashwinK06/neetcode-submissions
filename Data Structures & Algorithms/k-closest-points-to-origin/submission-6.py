class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for point in points:
            point.insert(0, (point[0])**2 + (point[1])**2)
        heapq.heapify(points)
        k_closest=[]
        while len(k_closest) < k:
            new_num=heapq.heappop(points)
            k_closest.append(new_num[1:])
        return k_closest
            

        