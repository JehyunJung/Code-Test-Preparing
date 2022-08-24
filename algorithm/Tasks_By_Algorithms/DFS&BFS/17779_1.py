from collections import deque
from math import inf
def bfs(start_row,start_col,visited,election_graph):
    election_number=election_graph[start_row][start_col]

    dy=[-1,0,1,0]
    dx=[0,1,0,-1]

    queue=deque([(start_row,start_col)])
    count=0
    while queue:
        row,col=queue.popleft()

        if visited[row][col]:
            continue
        visited[row][col]=True
        count+=graph[row][col]
        for dir in range(4):
            next_row=row+dy[dir]
            next_col=col+dx[dir]

            if next_row < 0 or next_row>=num or next_col < 0 or next_col >=num:
                continue
        
            if election_graph[next_row][next_col]!=election_number:
                continue

            queue.append((next_row,next_col))

    return count

def allocate_election_number(top_left,top_right,bottom_left,bottom_right,d1,d2):
    election_graph=[[0] * num for _ in range(num)]

    for row in range(num):
        for col in range(num):
            if 0<=row<bottom_left[0] and 0<=col<=top_left[1]:
                election_graph[row][col]=1
            elif 0 <= row <= top_right[0] and top_left[1] < col <num:
                election_graph[row][col]=2
            elif bottom_left[0] <= row <num and 0 <= col < bottom_right[1]:
                election_graph[row][col]=3
            elif top_right[0] < row <num and bottom_right[1] <= col < num:
                election_graph[row][col]=4

    #경계선 표시
    for i in range(d1+1):
        election_graph[top_left[0]+i][top_left[1]-i]=5
        election_graph[top_right[0]+i][top_right[1]-i]=5
    for i in range(d2+1):
        election_graph[top_left[0]+i][top_left[1]+i]=5
        election_graph[bottom_left[0]+i][bottom_left[1]+i]=5
    

    return election_graph
            

def solution():   
    
    min_count=inf
    for start_row in range(num):
        for start_col in range(num):
            for d1 in range(1,num-1):
                for d2 in range(1,num-1):
                    #경계를 넘어서는지 여부 판단
                    top_left=(start_row,start_col)
                    top_right=(start_row+d2,start_col+d2)
                    bottom_left=(start_row+d1,start_col-d1)
                    bottom_right=(start_row+d1+d2,start_col+d2-d1)

                    if top_right[0] < 0 or top_right[0]>=num or top_right[1] < 0 or top_right[1] >=num:
                        continue
                    if bottom_left[0] < 0 or bottom_left[0]>=num or bottom_left[1] < 0 or bottom_left[1] >=num:
                        continue
                    if bottom_right[0] < 0 or bottom_right[0]>=num or bottom_right[1] < 0 or bottom_right[1] >=num:
                        continue
                    
                    #기준선을 따라서 선거구역 할당
                    election_graph=allocate_election_number(top_left,top_right,bottom_left,bottom_right,d1,d2)

                    visited=[[False] * num for _ in range(num)]
                    #각각의 선거구역의 인구수를 파악하기 위한 배열
                    election_counts=[]
                    #각 꼭짓점 부분과, 기준선상의 점 하나를 이용해서 선거구역에 대한 bfs component을 구할 수 있도록 한다.
                    for row,col in [(0,0),(0,num-1),(num-1,0),(num-1,num-1)]:
                        election_counts.append(bfs(row,col,visited,election_graph))

                    election_counts.append(sum_of_citizen-sum(election_counts))
                    min_count=min(min_count,max(election_counts)-min(election_counts))

    
    return min_count


if __name__ == "__main__":
    num=0
    graph=[]
    sum_of_citizen=0
    with open("E:\\Codes\\Code-Test-Preparing\\algorithm\\Tasks_By_Algorithms\\DFS&BFS\\input17779.txt","r") as file:
        num=int(file.readline())
        for _ in range(num):
            row=list(map(int,file.readline().split()))
            graph.append(row)
            sum_of_citizen+=sum(row)
    
    print(solution())