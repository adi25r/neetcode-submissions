class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = [-cnt for cnt in counts.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # cnt and idle time

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time




        # counts = defaultdict(int)
        # for task in tasks:
        #     counts[task] += 1
        
        # max_heap = []
        # for key, val in counts.items():
        #     heapq.heappush(max_heap, (-val, key))

        # tick = 0
        # pending = [] # list of ttl, (left, task) pairs
        # while max_heap or pending: # while we still have elements
        #     i = 0
        #     while i < len(pending):
        #         ttl, (left, task) = pending[i]
        #         pending[i][0] -= 1
        #         if pending[i][0] == 0:
        #             pending.pop(i)
        #             heapq.heappush(max_heap, (left, task))
        #         else:
        #             i += 1
            
        #     if max_heap:
        #         left, task = heapq.heappop(max_heap)
        #         left += 1
        #         if left > 0: pending.append([n, (left, task)])
        #     tick += 1

        # return tick

        