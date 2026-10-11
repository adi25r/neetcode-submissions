class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # max limit on number of hops is k
        # we want the cheapest cost subject to this number

        # ucs with depth limit?


        adj_list = defaultdict(list)
        for s, d, p in flights:
            adj_list[s].append((d, p))

        prices = [float("inf")] * n
        prices[src] = 0
        frontier = [(0, src, -1)]

        for _ in range(k+1):
            tmpPrices = prices.copy()
            for s, d, p in flights: 
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return prices[dst] if prices[dst] != float("inf") else -1




        

        # frontier = [(0, src, -1)] # cost, hops, node
        # distances = [[float("inf")] * (k + 2) for _ in range(n)]
        # distances[src][0] = 0

        # while len(frontier):
        #     cost, v, hops = heapq.heappop(frontier)

        #     if v == dst:
        #         return cost

        #     if hops == k or distances[v][hops + 1] < cost:
        #         continue

        #     for neigh, price in adj_list[v]:
        #         new_cost = cost + price
        #         next_stops = 1 + hops

        #         if distances[neigh][next_stops + 1] > new_cost:
        #             distances[neigh][next_stops + 1] = new_cost
        #             heapq.heappush(frontier, (new_cost, neigh, next_stops))
        
        # return -1
                    



        