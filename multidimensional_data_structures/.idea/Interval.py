class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f'({self.start}, {self.end})'


class Node:
    def __init__(self, interval):
        self.interval = interval
        self.max = interval.end
        self.left = None
        self.right = None


class IntervalTree:
    def __init__(self):
        self.root = None

    def insert(self, interval):
        self.root = self._insert(self.root, interval)

    def _insert(self, node, interval):
        if not node:
            return Node(interval)
        if interval.start < node.interval.start:
            node.left = self._insert(node.left, interval)
        else:
            node.right = self._insert(node.right, interval)
        node.max = max(node.max, interval.end)
        return node

    def search(self, interval):
        result = self._search(self.root, interval)
        if result:
            print("Intervals found:")
            for r in result:
                print(r)
        else:
            print("No intervals found.")

    def _search(self, node, interval):
        if not node:
            return []
        if node.interval.start <= interval.end and node.interval.end >= interval.start:
            return [node.interval] + self._search(node.left, interval) + self._search(node.right, interval)
        if node.left and node.left.max >= interval.start:
            return self._search(node.left, interval)
        return self._search(node.right, interval)

# Create an instance of the IntervalTree
tree = IntervalTree()

# Insert some intervals
tree.insert(Interval(1, 3))
tree.insert(Interval(2, 5))
tree.insert(Interval(4, 7))
tree.insert(Interval(6, 8))

# Search for an interval
tree.search(Interval(3, 6))
