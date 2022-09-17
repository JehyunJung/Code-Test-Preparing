from math import inf
from collections import deque
from itertools import combinations
def bfs(group):
    vertex=group[0]
    visited=set()
    #인구수 저장
    population=0
    queue=deque([vertex])
    visited.add(vertex)

    while queue:
        vertex=queue.popleft()
        population+=populations[vertex]
        for adj_vertex in graph[vertex]:
            if adj_vertex not in visited and adj_vertex in group:
                visited.add(adj_vertex)
                queue.append(adj_vertex)
    
    #해당 그룹내 인구수 합과 해당 그룹간의 방문 정보(이를 통해 서로 연결되어 있음을 확인가능)
    return population, len(visited)


def solution():
    areas=[i for i in range(n)]
    min_difference=inf
    for i in range(1,n//2+1):
        for combination in combinations(areas,i):
            popul1,length1=bfs(combination)
            popul2,length2=bfs(list(set(areas).difference(set(combination))))

            if length1 + length2 == n:
                min_difference=min(min_difference,abs(popul1-popul2))
    
    if min_difference==inf:
        return -1
    else:
        return min_difference

if __name__ == "__main__":
    n=0
    populations=[]
    graph=[]
    
    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\backtracking\\input17471.txt","r") as file:
        n=int(file.readline())
        populations=list(map(int,file.readline().split()))
        graph=[[] for _ in range(n)]
        for vertex in range(n):
            connected_vertices=list(map(int,file.readline().split()))

            for adj_vertex in connected_vertices[1:]:
                graph[vertex].append(adj_vertex-1)
            graph[vertex].sort()
    print(graph)
    print(solution())
    

