import  collections
import heapq
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        trips = collections.defaultdict(dict)
        for city_from, city_to, price in flights:
            trips[city_from][city_to] = price

        priority_queue = [(0, src, 0)]
        heapq.heapify(priority_queue)
        visited = [[float('inf')] * (k + 2) for _ in range(n)]
        while priority_queue:
            cur_price, cur_city, cur_trip_cnt = heapq.heappop(priority_queue)

            if cur_city == dst:
                return cur_price

            for new_city, next_price, in trips[cur_city].items():
                new_trip_cnt = cur_trip_cnt + 1
                if new_trip_cnt > k + 1:
                    continue

                new_price = cur_price + next_price
                if new_price < visited[new_city][cur_trip_cnt + 1]:
                    heapq.heappush(priority_queue, (new_price, new_city, new_trip_cnt))
                    visited[new_city][new_trip_cnt] = new_price
        return -1