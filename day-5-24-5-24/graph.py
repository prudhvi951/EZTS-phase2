csalass graph:
    def __init__(self):
        self.d = {}
    def add(self,u,v):
        if u not in self.d:
            self.d[u] = []
            self.d[u].append(v)
        else:
            self.d[u].append(v)
    def bfs(self,root):
        queue = [root]
        visited = [root]
        while queue:
            curr = queue.pop(0)
            print(curr)
            for ele in self.d[curr]:
                if ele not in visited:
                    visited.append(ele)
                    queue.append(ele)
g = graph()
g.add(1,2)
g.add(1,3)
print(g.d)
