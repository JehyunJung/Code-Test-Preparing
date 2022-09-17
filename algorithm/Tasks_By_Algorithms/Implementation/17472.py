from collections import deque
from math import inf
#component을 찾아서 고유한 번호 할당
def bfs(visited,start_row,start_col,index):
    global graph
    queue=deque([(start_row,start_col)])
    component=[]

    dy=[-1,0,1,0]
    dx=[0,1,0,-1]

    while queue:
        row,col=queue.popleft()

        if visited[row][col]:
            continue
        visited[row][col]=True
        component.append((row,col))

        for dir in range(4):
            next_row=row+dy[dir]
            next_col=col+dx[dir]

            if next_row < 0 or next_row>=n_rows or next_col < 0 or next_col >=n_cols:
                continue
            if graph[next_row][next_col]==1:
                queue.append((next_row,next_col))


    for row,col in component:
        graph[row][col]=index
    
    return component

#component을 바탕으로 간선들을 찾는다.
def find_edges(component,index,count):
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]

    distance_info=[inf]*count

    for row,col in component:
        for dir in range(4):
            for time in range(1,10):
                next_row=row+dy[dir]*time
                next_col=col+dx[dir]*time

                if next_row < 0 or next_row >=n_rows or next_col < 0 or next_col>=n_cols:
                    break

                #같은 component 내로는 검사 진행 하지 않는다.
                if graph[next_row][next_col]==index:
                    break

                if graph[next_row][next_col] !=0:
                    #항상 거리가 2이상이어야 한다.
                    if time==2:
                        break
                    #거리 정보를 최신화 시켜준다.
                    distance_info[graph[next_row][next_col]]=min(distance_info[graph[next_row][next_col]],time-1)
                    break
    edges=[]
    #구한 거리 정보를 바탕으로 간선을 만들어준다.
    for adj_vertex in range(count):
        if adj_vertex == index:
            continue
        if distance_info[adj_vertex] != inf:
            edges.append((index,adj_vertex,distance_info[adj_vertex]))
    return edges

#Multiple Disjoint Set
def find_parent_compressed(parents,x):
    if parents[x] != x:
        parents[x]=find_parent_compressed(parents,parents[x])
    return parents[x]

def union_parents(parents,x,y):
    pre_x=find_parent_compressed(parents,x)
    pre_y=find_parent_compressed(parents,y)

    if pre_x<pre_y:
        parents[pre_x]=pre_y
    else:
        parents[pre_y]=pre_x

def kruskal_alogirthm(edges,counts):
    parents=[i for i in range(counts)]
    min_cost=0
    n_edges=0
    for v1,v2,cost in edges:
        #사이클 존재
        if find_parent_compressed(parents,v1) == find_parent_compressed(parents,v2):
            continue
        else:
            union_parents(parents,v1,v2)
            min_cost+=cost
            n_edges+=1
    
    return min_cost,n_edges
    

def print_graph():
    print("GRAPH")
    for row in graph:
        print(row)

def solution():
    components=dict()
    counts=1
    visited=[[False]*n_cols for _ in range(n_rows)]
    #component 찾기
    for row in range(n_rows):
        for col in range(n_cols):
            if graph[row][col]==1 and not visited[row][col]:
                components[counts]=bfs(visited,row,col,counts)
                counts+=1
    
    #모든 edges을 구한다.
    edges=[]
    for index in range(1,counts):
        edges.extend(find_edges(components[index],index,counts))
    edges.sort(key=lambda x: x[2])

    #MST 알고리즘
    min_cost,n_edges=kruskal_alogirthm(edges,counts)

    #모든 섬을 연결할 수 있는 경우는 간선의 개수 = 노드의 개수 -1
    if n_edges==counts-2:
        return min_cost
    else:
        return -1

if __name__ =="__main__":
    n_rows,n_cols=0,0
    graph=[]

    with open("input17472.txt","r") as file:
        n_rows,n_cols=map(int,file.readline().split())
        graph=[list(map(int,file.readline().split())) for _ in range(n_rows)]
    
    print(solution())