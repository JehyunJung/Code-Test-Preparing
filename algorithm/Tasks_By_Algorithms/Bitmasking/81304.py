from math import inf
from heapq import heappush,heappop
from collections import deque


def solution(n, start, end, roads, traps):
    answer = 0
    graph=[[] for _ in range(n+1)]
    reversed_graph=[[] for _ in range(n+1)]
    
    trap_nodes={node:index for index,node in enumerate(traps)}
    
    #트랩을 밟은 상태
    state=0
    
    for src,dest,cost in roads:
        graph[src].append((dest,cost))
        graph[dest].append((src,-cost))
    
    #노드 * 트랩상태에 따른 distance 배열 초기화
    distances=[[inf]*(1024) for _ in range(n+1)]
    distances[start][0]=0
    heap=[(0,0,start)]
    
    while heap:
        cost,state,vertex=heappop(heap)
        
        #마지막 노드를 도달한 경우 반복을 종료한다.
        if vertex == end:
            return cost
          
        if distances[vertex][state] < cost:
            continue
            
        reverse_check=1
        
        #시작점이 트랩인 경우
        if vertex in trap_nodes and state & 1 << trap_nodes[vertex]:
            reverse_check *=-1
      
        # 검사        
        for adj_vertex,adj_cost in graph[vertex]:
            #끝점이 트랩인 경우
            if adj_vertex in trap_nodes and state & 1 << trap_nodes[adj_vertex]:
                reverse_check *= -1
            adj_cost *= reverse_check
            if adj_cost > 0:
                new_state=state
                if adj_vertex in trap_nodes:
                    new_state=state ^ 1 << trap_nodes[adj_vertex]
                
                #일반 노드인 경우
                if distances[adj_vertex][new_state] > cost+adj_cost:
                    distances[adj_vertex][new_state]=cost+adj_cost
                    heappush(heap,(distances[adj_vertex][new_state],new_state,adj_vertex))
            
if __name__ =="__main__":
    n,start,end=4,1,4
    roads=[[1, 2, 1], [3, 2, 1], [2, 4, 1]]
    traps=[2,3]
    print(solution(n,start,end,roads,traps))