from collections import deque
from math import inf
import sys
from os.path import dirname,join

def solution(row,col):
    if (row,col) == (rows-1,cols-1):
        return 1

    if dp[row][col] != 0:
        return dp[row][col]

    for dir in range(4):
        next_row=row+dy[dir]
        next_col=col+dx[dir]

        if next_row < 0 or next_row >=rows or next_col < 0 or next_col>=cols:
            continue

        if graph[row][col] > graph[next_row][next_col]:
            dp[row][col]+=solution(next_row,next_col)

    
    return dp[row][col]


if __name__ == "__main__":
    scriptpath = dirname(__file__)
    filename = join(scriptpath, 'input.txt')
    
    with open(filename,"r") as file:
        rows,cols=map(int,file.readline().split())
        graph=[]
        for _ in range(rows):
            graph.append(list(map(int,file.readline().split())))

    dp=[[0] * cols for _ in range(rows)]
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]
    
    print(solution(0,0))
    print(dp)