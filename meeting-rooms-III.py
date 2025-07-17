class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = list(range(n))
        heapq.heapify(available)
        occupied = []
        count = [0] * n
        curr_time = 0
        
        for start, end in meetings:
            while occupied and occupied[0][0] <= max(start, curr_time):
                end_time, room = heapq.heappop(occupied)
                heapq.heappush(available, room)
                curr_time = max(curr_time, end_time)
            
            if available:
                room = heapq.heappop(available)
                count[room] += 1
                heapq.heappush(occupied, (max(start, curr_time) + (end - start), room))
            else:
                end_time, room = heapq.heappop(occupied)
                count[room] += 1
                curr_time = max(curr_time, end_time)
                heapq.heappush(occupied, (curr_time + (end - start), room))
        
        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i
        return 0
