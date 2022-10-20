# TC: O(N^2), SC: O(N^2)
# Breadth-first search is on N nodes, and each node could have N edges

import collections
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0  # do not take any bus
        
        graph = collections.defaultdict(set) 
        for bus, route in enumerate(routes):
            for stop in route:
                 graph[stop].add(bus)
        # print(graph) # {stop: {bus}}
        if source not in graph or target not in graph:
            return -1
        # q: record all of the stops and number of buses to take
        queue = collections.deque([(source, 0)]) 
        visited_stops, visited_buses = set(), set()
        
        while queue:
            for _ in range(len(queue)):
                cur_stop, no_buses = queue.popleft()
                if cur_stop == target:
                    return no_buses 
                for bus in graph[cur_stop]:  
                    if bus not in visited_buses: # check 1
                        visited_buses.add(bus)
                        for stop in routes[bus]: # [1,2,7]
                            if stop not in visited_stops: # check 2
                                visited_stops.add(stop)
                                queue.append((stop, no_buses + 1))
        return -1
    

# Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# Output: 2
# Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.