import collections
from typing import List


class CheckCycle(object):
    def __init__(self):
        self.vertex = set()  # 顶点集合
        self.edges = collections.defaultdict(
            set
        )  # 使用字典表示有向边 如 a -> {b,c,e} 表示 b,c,e 均依赖 a
        self.indegree = collections.defaultdict(int)  # 计算每个顶点的入度

    def add_edge(self, from_job: str, to_job: str) -> bool:
        """
        添加一条边
        """
        if from_job == to_job:
            return False

        if from_job:
            self.vertex.add(from_job)
            if not from_job in self.indegree:
                self.indegree[from_job] = 0  # 初始化入度为 0
        if to_job:
            self.vertex.add(to_job)
            if not to_job in self.indegree:  # 初始化入度为0
                self.indegree[to_job] = 0
        if from_job and to_job:
            if to_job not in self.edges[from_job]:  # 防止充分添加相同的边
                self.indegree[to_job] += 1  # 入度加 1
                self.edges[from_job].add(to_job)  # 防止充分添加相同的边

        return True

    def can_finish(self) -> bool:
        """
        广度优先遍历
        Returns:
            True: 表示没有环，任务可以完成
            False: 表示有环，任务不可以完成
        """

        q = collections.deque([u for u in self.indegree if self.indegree[u] == 0])
        visited = 0

        possible_sequence = []

        while q:
            visited += 1
            u = q.popleft()
            possible_sequence.append(u)
            for v in self.edges[u]:
                self.indegree[v] -= 1
                if self.indegree[v] == 0:
                    q.append(v)
        print(f'possible sequence: {"->".join(possible_sequence)}')
        return visited == len(self.vertex)

    def can_finish2(self) -> bool:
        """
        深度优先遍历
        Returns:
            True: 表示没有环，任务可以完成
            False: 表示有环，任务不可以完成
        """

        visited = collections.defaultdict(int)  # 保存每个顶点是否被访问过
        for job in self.vertex:
            visited[job] = 0  # 初始化，均未被访问过

        result = list()  # 模拟栈
        valid = True

        def dfs(from_job: str):
            nonlocal valid
            visited[from_job] = 1
            for to_job in self.edges[from_job]:
                if visited[to_job] == 0:
                    dfs(to_job)
                    if not valid:
                        return
                elif visited[to_job] == 1:
                    valid = False
                    return
            visited[from_job] = 2
            result.append(from_job)

        for job in self.vertex:
            if valid and not visited[job]:
                dfs(job)

        # print(result)
        return valid


if __name__ == "__main__":
    """
    a->b->c 
       b->d 
       True
    a->b->c
       b->d->a 
       False 
    """
    check_cycle = CheckCycle()
    check_cycle.add_edge(from_job="a", to_job="b")
    check_cycle.add_edge(from_job="b", to_job="c")
    check_cycle.add_edge(from_job="b", to_job="d")
    print(check_cycle.can_finish2())

    check_cycle = CheckCycle()
    check_cycle.add_edge(from_job="a", to_job="b")
    check_cycle.add_edge(from_job="b", to_job="c")
    check_cycle.add_edge(from_job="c", to_job="b")
    check_cycle.add_edge(from_job="d", to_job="f")
    print(check_cycle.can_finish2())
