class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1


        freq = [[] for i in range(len(nums) + 1)]

        for key, value in hashmap.items():
            freq[value].append(key)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result


        # heap = []
        # for key in hashmap.keys():
        #     heapq.heappush(heap, (hashmap[key], key))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        
        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        
        # return res

        


        # res = []
        # for i in range(k):
        #     curr_max = -float('inf')
        #     curr_key = None
        #     for key, value in hashmap.items():
        #         if curr_max < value:
        #             curr_max = value
        #             curr_key = key

        #     res.append(curr_key)
        #     del hashmap[curr_key]
        # return res