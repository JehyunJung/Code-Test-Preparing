from heapq import heappush,heappop
from math import inf

def solution():
    count=0
    heap=[(graph[0][0],0,0)]
    distances[0][0]=graph[0][0]

    while heap:
        cost,row,col=heappop(heap)

        if cost > distances[row][col]:
            continue

        for dir in range(4):
            next_row=row+dy[dir]
            next_col=col+dx[dir]

            if next_row < 0 or next_row>=n or next_col < 0 or next_col>=n:
                continue

            new_distance=cost+graph[next_row][next_col]

            if new_distance < distances[next_row][next_col]:
                distances[next_row][next_col]=new_distance
                heappush(heap,(new_distance,next_row,next_col))
    
    return distances[n-1][n-1]

if __name__ == "__main__":
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]
    index=0
    with open("input4485.txt","r") as file:

        while True:
            n=int(file.readline())
            
            #n==0 이면 반복을 종료한다. 
            if n==0:
                break
            index+=1       
            graph=[list(map(int, file.readline().split())) for _ in range(n)]
            distances=[[inf] * n for _ in range(n)]
            print(f"Problem {index}: {solution()}")


