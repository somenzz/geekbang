import sys
import heapq

max = sys.maxsize

vertices_number = 6
adjacency_matrix = [
    [0, 7, 9, -1, -1, 14],
    [7, 0, 10, 15, -1, -1],
    [9, 10, 0, 11, -1, 2],
    [-1, 15, 11, 0, 6, -1],
    [-1, -1, -1, 6, 0, 9],
    [14, -1, 2, -1, 9, 0],
]

cost = [max] * vertices_number
pq = []  # 优先级队列，最小堆


class Node(object):
    def __init__(self, vertex, distance):
        self.vertex = vertex
        self.distance = distance

    def __lt__(self, other):
        """
        为了进堆时比较大小，重写 __lt__ 方法
        """
        return self.distance < other.distance


def printpq(pq):
    ## debug 用，查看堆里面的数据
    for item in pq:
        print(item.vertex, item.distance, end="|")
    print("")


def dijkstra(from_vertex, dest_vertex):
    from_vertex = from_vertex - 1  # 转换为列表的下标，因此减 1
    dest_vertex = dest_vertex - 1
    visited = set()  # 定义已经确定最小距离的点，防止重复计算。

    # 起点入队
    heapq.heappush(pq, Node(from_vertex, 0))  # 按照距离比较大小进堆
    while pq and len(visited) < vertices_number:
        # printpq(pq)
        # 出队
        node = heapq.heappop(pq)
        from_vertex1 = node.vertex
        distance1 = node.distance
        if from_vertex1 in visited:
            # 如果改点已经确认了最小距离，直接抛弃。
            continue
        # 更新距离，已经确定时最小距离的点加入已访问集合。
        print(from_vertex1)
        cost[from_vertex1] = distance1
        visited.add(from_vertex1)
        # 取出 from_vertex1 的邻居节点，
        for index, distance in enumerate(adjacency_matrix[from_vertex1]):
            # 只选择与 from_vertex1 连通的点，也就是邻居，排除已经确定了最小值的点。
            if distance > 0 and index not in visited:
                heapq.heappush(pq, Node(index, distance + distance1))

    return -1 if cost[dest_vertex] == max else cost[dest_vertex]


if __name__ == "__main__":
    print(dijkstra(1, 5))
    print(cost)
    # assert 20 == dijkstra(1, 5)
