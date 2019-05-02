#!/usr/bin/python
# encoding=gbk

from __future__ import print_function
# Author: OMKAR PATHAK

# We can use Python's dictionary for constructing the graph

class AdjacencyList(object):
    def __init__(self):
        self.List = {}

    def addEdge(self, fromVertex, toVertex):
        # check if vertex is already present
        if fromVertex in self.List.keys():
            self.List[fromVertex].append(toVertex)
        else:
            self.List[fromVertex] = [toVertex]

    def printList(self):
        for i  in self.List:
            print(i,'->',' -> '.join([str(j) for j in self.List[i]]))
    
    def _generate_path(self,prev,fromVertex,toVertex):
        if fromVertex != toVertex:
            yield from self._generate_path(prev,fromVertex,prev[toVertex])
        yield str(toVertex)


    def bfs(self,fromVertex,toVertex):
        '''
        �������������Breadth-First-Search��
        '''

        if fromVertex == toVertex:
            return 

        #visited = {} #��¼�����Ƿ񱻷��ʣ�Ĭ��δ����
        #for v in self.List.keys():
        #    visited[v]=False
        visited = {fromVertex}
        queue = [fromVertex] #�����������洢ÿһ��Ľڵ�
        prev = {}
        while queue != []:
            f = queue.pop(0)
            for t in self.List[f]:
                if t not in visited:
                    prev[t] = f
                    if t == toVertex:
                        print("->".join(self._generate_path(prev,fromVertex,toVertex)))
                        #print(prev)
                        return
                    else:
                        visited.add(t)
                        queue.append(t)

    def dfs(self,fromVertex,toVertex):
        '''
        �������������Deep-First-Search��
        '''

        if fromVertex == toVertex:
            return 

        #visited = {} #��¼�����Ƿ񱻷��ʣ�Ĭ��δ����
        #for v in self.List.keys():
        #    visited[v]=False
        visited = {fromVertex}
        stack = [fromVertex] #�����������洢ÿһ��Ľڵ�
        prev = {}
        while stack != []:
            f = stack.pop()
            for t in self.List[f]:
                if t not in visited:
                    prev[t] = f
                    if t == toVertex:
                        print("->".join(self._generate_path(prev,fromVertex,toVertex)))
                        #print(prev)
                        return
                    else:
                        visited.add(t)
                        stack.append(t)
                

    def findNfriends(self,fromVertex,N):
        '''
        �������������Breadth-First-Search��
        ���� N ���ڵĺ���
        '''
        friends = {fromVertex:0} #friends[a] = 1 ��ʾ��ʼ����fromVertex ������ a �ľ���Ϊ 1
        visited = {fromVertex}
        queue = [fromVertex] #�����������洢ÿһ��Ľڵ�
        while queue != []:
            f = queue.pop(0)
            for t in self.List[f]:
                if t not in visited:
                    friends[t] = friends[f] + 1 
                    visited.add(t)
                    queue.append(t)
        print(f"{fromVertex} �� {N} ���ڵĺ����У�",end = '')
        for k,v in friends.items():
            if 0< v <=N:
                print(k,end=',')
        print("")








if __name__ == '__main__':
    al = AdjacencyList()
    al.addEdge(0, 3)
    al.addEdge(0, 1)
    al.addEdge(1, 0)
    al.addEdge(1, 4)
    al.addEdge(1, 2)
    al.addEdge(3, 4)
    al.addEdge(3, 0)
    al.addEdge(2, 5)
    al.addEdge(2, 1)
    al.addEdge(4, 6)
    al.addEdge(4, 5)
    al.addEdge(4, 3)
    al.addEdge(4, 1)
    al.addEdge(6, 7)
    al.addEdge(6, 4)
    al.addEdge(5, 7)
    al.addEdge(5, 4)
    al.addEdge(5, 2)
    al.addEdge(7, 6)
    al.addEdge(7, 5)
    #print(al.List)
    #al.printList()
    al.bfs(0,6)
    al.findNfriends(0,3)
    al.findNfriends(0,2)
    al.findNfriends(0,1)
    al.dfs(0,6)

