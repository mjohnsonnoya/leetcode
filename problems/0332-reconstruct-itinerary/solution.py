from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjlist = defaultdict(list)
        for k, v in tickets:
            adjlist[k].append(v)
        
        for k in adjlist:
            adjlist[k].sort(reverse=True)
        
        path = []

        def dfs(node):
            if len(path) == len(tickets) + 1:
                return True
            while adjlist[node]:
                next_node = adjlist[node].pop()
                dfs(next_node)
            path.append(node)


        dfs("JFK")
        return path[::-1]


