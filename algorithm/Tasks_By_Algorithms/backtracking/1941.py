from itertools import combinations,product
from collections import deque
import sys

def check(coordinates):
    
    #이다솜파의 우세 여부
    y_count=0

    for row,col in coordinates:
        if board[row][col] == "Y":
            y_count+=1
    if y_count >=4:
        return False
    

    dy=[-1,0,1,0]
    dx=[0,1,0,-1]
    
    #연결 여부
    visited=set()
    queue=deque([(coordinates[0])])
    
    coordinates=set(coordinates)
    while queue:
        row,col=queue.popleft()

        for dir in range(4):
            next_row=row+dy[dir]
            next_col=col+dx[dir]

            if (next_row,next_col) in coordinates and (next_row,next_col) not in visited:
                visited.add((next_row,next_col))
                queue.append((next_row,next_col))

    if visited != coordinates:
        return False
    
    return True


def solution():
    count=0
    coordinates=list(product(range(0,5),range(0,5)))
    for combination in combinations(coordinates,7):     
        if check(combination):
            count+=1

    print(count)
if __name__ == "__main__":
    sys.stdin=open("input1941.txt","r")
    board=[list(input()) for _ in range(5)]
    solution()
    