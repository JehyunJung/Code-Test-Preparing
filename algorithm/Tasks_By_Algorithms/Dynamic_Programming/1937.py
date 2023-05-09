import sys
from os.path import dirname,join

def dfs(previous_row,previous_col):
    #이전에 방문한 경우
    if dp[previous_row][previous_col] != -1:
        return dp[previous_row][previous_col]

    dp[previous_row][previous_col] =0
    previous_value=board[previous_row][previous_col]

    max_distance=1
    for dir in range(4):
        next_row=previous_row+dy[dir]
        next_col=previous_col+dx[dir]

        #격자 범위를 벗어나는 경우
        if next_row < 0 or next_row >=n or next_col < 0 or next_col>=n:
            continue

        #이전 위치 보다 대나무 양이 적은 경우
        if board[next_row][next_col] < previous_value:
            continue
        
        max_distance=max(max_distance,dfs(next_row,next_col)+1)
    
    dp[previous_row][previous_col] =max_distance
    return max_distance

def solution():
    for row in range(n):
        for col in range(n):
            dfs(row,col)

    max_value=0
    for row in range(n):
        for col in range(n):
            max_value=max(max_value,dp[row][col])

    print(max_value)
    

if __name__ == "__main__":
    scriptpath = dirname(__file__)
    filename = join(scriptpath, 'input1937.txt')
    sys.stdin=open(filename, "r")
    n=int(input())

    board=[list(map(int,input().split())) for _ in range(n)]
    dp=[[-1]*n for _ in range(n)]

    dy=[-1,0,1,0]
    dx=[0,1,0,-1]
    solution()