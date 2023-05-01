from collections import deque
from itertools import permutations
from math import inf
import sys

def find_distances(length,areas):
    distances=[[inf] * length for _ in range(length)]

    dy=[-1,0,1,0]
    dx=[0,1,0,-1]
    for i in range(length):
        start_row,start_col=areas[i]
        queue=deque([(start_row,start_col,0)])
        visited=[[inf] * n_cols for _ in range(n_rows)]

        #각 점에 대해 bfs을 수행해서 각 좌표까지 도달 가능한 거리 탐색
        while queue:
            row,col,distance=queue.popleft()
            #저장되어 있는 최소 거리보다 크면 해당 점을 탐색할 필요가 없으니 다음 경우 조사
            if distance > visited[row][col]:
                continue

            visited[row][col]=distance

            for dir in range(4):
                next_row=row+dy[dir]
                next_col=col+dx[dir]

                #격자 범위를 벗어나는 경우
                if next_row < 0 or next_row >=n_rows or next_col < 0 or next_col>=n_cols:
                    continue
                #벽이 있는 경우
                if board[next_row][next_col] == "x":
                    continue

                if (distance + 1) < visited[next_row][next_col]:
                    visited[next_row][next_col]=distance+1
                    queue.append((next_row,next_col,distance+1))
        
        #각 위치 좌표에 도달하는 거리 초기화
        for j in range(i+1,length):
            next_row,next_col=areas[j]
            distances[i][j]=visited[next_row][next_col]
            distances[j][i]=visited[next_row][next_col]

    return distances


def solution():
    areas=[]
    start_row,start_col=0,0
    
    #지나가야하는 좌표 구하기
    for row in range(n_rows):
        for col in range(n_cols):
            if board[row][col] == "o":
                start_row,start_col=row,col
            
            if board[row][col] == "*":
                areas.append((row,col))
    
    #초기 좌표도 포함시킨다.
    areas.insert(0,(start_row,start_col))
    length=len(areas)
    distances=find_distances(length,areas)
    shortest_distance=inf
    
    #더러운 좌표에 대한 순열을 구해서 좌표 순서에 따른 총 이동 거리를 구한다.
    for permutation in permutations(range(1,length)):
        distance=0
        previous_index=0
        #시작 좌표를 기점으로 더러운 좌표의 순열을 탐색한다.
        for next_index in permutation:
            distance+=distances[previous_index][next_index]
            previous_index=next_index
        
        shortest_distance=min(shortest_distance,distance)
    
    if shortest_distance == inf:
        print(-1)
    else:
        print(shortest_distance)
if __name__ == "__main__":
    sys.stdin=open("input4991.txt","r") 
    while True:
        n_cols,n_rows=map(int,input().split())

        #입력의 끝
        if (n_rows,n_cols)==(0,0):
            break

        board=[list(input()) for _ in range(n_rows)]
        solution()