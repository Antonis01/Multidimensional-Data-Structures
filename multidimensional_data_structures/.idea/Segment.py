class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [0] * (4 * self.n)
        self.build(1, 0, self.n - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
            return

        mid = (start + end) // 2
        self.build(2 * node, start, mid)
        self.build(2 * node + 1, mid + 1, end)
        self.tree[node] = min(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return float('inf')

        if l <= start and end <= r:
            return self.tree[node]

        mid = (start + end) // 2
        left = self.query(2 * node, start, mid, l, r)
        right = self.query(2 * node + 1, mid + 1, end, l, r)
        return min(left, right)

    def stabbing_query(self, point):
        left = 0
        right = self.n - 1
        ans = None
        while left <= right:
            mid = (left + right) // 2
            if self.arr[mid] <= point:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1

        return ans


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = SegmentTree(arr)

# print the minimum value of the range [3, 6]
print(st.query(1, 0, len(arr) - 1, 3, 6))

print(st.stabbing_query(7))



