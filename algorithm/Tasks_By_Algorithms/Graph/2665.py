import sys
from math import inf
from heapq import heappush,heappop

def solution():
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]
    distances=[[inf for _ in range(n)] for _ in range(n)]
    visited=[[False] * n for _ in range(n)]
    heap=[(0,0,0)]

    distances[0][0]=0
    visited[0][0]=True

    while heap:
        destroy_count,row,col=heappop(heap)

        if (row,col)==(n-1,n-1):
            print(destroy_count)
            break

        for dir in range(4):
            next_row=row + dy[dir]
            next_col=col + dx[dir]

            if next_row < 0 or next_row >=n or next_col<0 or next_col>=n:
                continue

            if visited[next_row][next_col]:
                continue

            visited[next_row][next_col]=True
            
            #흰 방인 경우
            if board[next_row][next_col] == "1":
                heappush(heap,(destroy_count,next_row,next_col))
            #검은 방인 경우
            else:
                heappush(heap,(destroy_count+1,next_row,next_col))

if __name__ == '__main__':
    sys.stdin=open("input2665.txt","r")
    n=int(input())
    board=[list(input()) for _ in range(n)]
    solution()
