from collections import deque
from math import inf
def bfs(start_row,start_col):
    visited=[[-1] * N for _ in range(N)]

    queue=deque([(start_row,start_col)])
    visited[start_row][start_col]=0
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]

    while queue:
        row,col=queue.popleft()
        
        for dir in range(4):
            next_row=row+dy[dir]
            next_col=col+dx[dir]

            if next_row < 0 or next_row>=N or next_col < 0 or next_col>=N:
                continue

            if graph[next_row][next_col] ==1:
                continue

            if visited[next_row][next_col]!=-1:
                continue
            visited[next_row][next_col]=visited[row][col]+1
            queue.append((next_row,next_col))

    return visited

def find_candidate(visited_route):
    distance_graph=bfs(taxi_row,taxi_col)

    min_distance,index=inf,0
    #후보군 찾기
    for i in range(M):
        start_row,start_col,end_row,end_col=passengers[i]
        if visited_route[i]:
            continue
        

        distance=distance_graph[start_row][start_col]

        #도달할 수 없는 경로 인경우
        if distance == -1:
            continue

        if min_distance >distance:
            min_distance=distance
            index=i

    return min_distance,index
    
def solution():
    global fuel,taxi_row,taxi_col
    #해당 탑승객 처리 정보
    visited_route=[False] *M
    #거리 정보
    route_info=[]
    #거리정보 초기화
    for start_row,start_col,end_row,end_col in passengers:
        distance_graph=bfs(start_row,start_col)

        distance=distance_graph[end_row][end_col]

        #해당 경로를 접근할 수 없는 경우
        if distance == -1:
            return -1

        route_info.append(distance)
    
    for _ in range(M):

        #최단거리/행/열 고객 선택
        distance,index=find_candidate(visited_route)

        #가장 가까운 탑승자를 찾을 수 없는 경우
        if distance == inf:
            return -1

        #해당 손님을 태울 수 없는 경우(탐승객까지의 거리 + 경로 정보)
        if distance+route_info[index] > fuel:
            return -1
        
        visited_route[index]=True
        
        #기름 변화량, 택시 위치 이동
        fuel+=(route_info[index]-distance)
        taxi_row,taxi_col=passengers[index][2],passengers[index][3]
        
        
    if fuel < 0:
        return -1

    return fuel  

        

if __name__ == "__main__":
    N,M,fuel=0,0,0
    graph=[]
    taxi_row,taxi_col=0,0
    #각각의 고객에 대한 경로 정보
    passengers=[]

    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\DFS&BFS\\input19238.txt","r") as file:
        N,M,fuel=map(int,file.readline().split())
        graph=[list(map(int,file.readline().split())) for _ in range(N)]
        
        taxi_row,taxi_col=map(int,file.readline().split())
        taxi_row-=1
        taxi_col-=1

        for _ in range(M):
            start_row,start_col,end_row,end_col=map(int,file.readline().split())
            passengers.append((start_row-1,start_col-1,end_row-1,end_col-1))
        
    print(solution())

        