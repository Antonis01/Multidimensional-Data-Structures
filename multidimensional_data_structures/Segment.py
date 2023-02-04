class SegmentTree:
    def __init__(self, points):
        self.n = len(points)
        self.points = points
        self.tree = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.points[start][1]
            return self.tree[node]
        mid = (start + end) // 2
        self.tree[node] = max(self.build(2 * node + 1, start, mid),
                              self.build(2 * node + 2, mid + 1, end))
        return self.tree[node]

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        return max(self.query(2 * node + 1, start, mid, l, r),
                   self.query(2 * node + 2, mid + 1, end, l, r))

