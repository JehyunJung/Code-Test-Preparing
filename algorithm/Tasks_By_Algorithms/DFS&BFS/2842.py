from math import inf
from collections import deque

def bfs(start_row,start_col,min_height,max_height):

    dy=[-1,-1,-1,0,1,1,1,0]
    dx=[-1,0,1,1,1,0,-1,-1]

    queue=deque([(start_row,start_col)])
    house_count=0
    visited=[[False] * n for _ in range(n)]

    #시작점이 최소,최대 높이 범위에 해당되지 않은 경우 바로 반환
    if heights[start_row][start_col] < min_height or heights[start_row][start_col] > max_height:
        return 0
    
    while queue:
        row,col=queue.popleft()

        #이전에 방문한 경우
        if visited[row][col]:
            continue
        visited[row][col]=True
        
        #집인 경우
        if board[row][col]=="K":
            house_count+=1

        for dir in range(8):
            next_row=row+dy[dir]
            next_col=col+dx[dir]

            #격자를 넘어서는 경우
            if next_row < 0 or next_row>=n or next_col < 0 or next_col>=n:
                continue
            #탐색하고자 하는 집의 높이가 최소, 최대 범위에 해당하지 않는 경우
            if heights[next_row][next_col] < min_height or heights[next_row][next_col] > max_height:
                continue

            queue.append((next_row,next_col))

    return house_count

def solution():
    houses=0
    answer=inf
    start_row,start_col=0,0
    height_list=set()
    for row in range(n):
        for col in range(n):
            height_list.add(heights[row][col])
            if board[row][col]=="P":
                start_row,start_col=row,col
            if board[row][col]=="K":
                houses+=1

    height_list=sorted(list(height_list))
    length_of_height_list=len(height_list)
    left,right=0,0
    while right < length_of_height_list:
        result=bfs(start_row,start_col,height_list[left],height_list[right])
        if result == houses:
            answer=min(answer,height_list[right]-height_list[left])
            left+=1
        elif right + 1 < length_of_height_list:
            right+=1
        else:
            break

    print(answer)

if __name__ == "__main__":
    with open("input2842.txt","r") as file:
        n=int(file.readline())
        board=[list(file.readline().strip()) for _ in range(n)]
        heights=[list(map(int,file.readline().split())) for _ in range(n)]
    solution()