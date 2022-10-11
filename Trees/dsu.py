class DSU(object):
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        rootA, rootB = self.find(x), self.find(y)
        if rootA != rootB:
            if self.size[rootA] > self.size[rootB]:
                rootA, rootB = rootB, rootA

            self.parents[rootA] = rootB
            self.size[rootB] += self.size[rootA]


dsu = DSU(5)
dsu.union(0, 1)
dsu.union(1, 2)

parents = set()

for i in range(5):
    parents.add(dsu.find(i))

print(f"The number of groups are: {parents.__len__()}")
