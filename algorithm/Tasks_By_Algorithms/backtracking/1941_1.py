from itertools import combinations,product
from collections import deque
import sys

def dfs(index,coordinates):
    global visited

    #Y의 갯수가 3개를 넘어서면 안된다.
    if "".join(board[coordinate//5][coordinate%5] for coordinate in coordinates).count("Y") >3:
        return

    #좌표 7개를 탐색한 경우
    if index == 7:
        visited.add("".join(map(str,sorted(coordinates))))
        return

    for coordinate in coordinates:
        row=coordinate // 5
        col=coordinate % 5

        for dir in range(4):
            next_row= row + dy[dir]
            next_col= col + dx[dir]
            #격자를 벗어나는 경우
            if next_row < 0 or next_row >=5 or next_col < 0 or next_col>=5:
                continue 
            next_coordinate=next_row *5 + next_col
            #이미 방문한 경우
            if next_coordinate in coordinates:
                continue

            coordinates.add(next_coordinate)
            dfs(index+1,coordinates)
            coordinates.remove(next_coordinate)

def solution():
    for i in range(25):
        coordinate_set=set([i])
        dfs(1,coordinate_set)

    print(len(visited))
if __name__ == "__main__":
    sys.stdin=open("input1941.txt","r")
    board=[list(input()) for _ in range(5)]
    visited=set()
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]
    
    solution()
    