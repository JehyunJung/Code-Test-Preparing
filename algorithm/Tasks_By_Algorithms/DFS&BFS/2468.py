from collections import deque
def solution():
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]
    max_count=0

    for height in range(max_height+1):
        visited=[[False] *(num) for _ in range(num)]
        count=0
        for start_row in range(num):
            for start_col in range(num):
                if graph[start_row][start_col] <= height or visited[start_row][start_col]:
                    continue
                queue=deque([(start_row,start_col)])
                while queue:
                    row,col=queue.popleft()

                    if visited[row][col]:
                        continue
                    visited[row][col]=True

                    for dir in range(4):
                        next_row=row+dy[dir]
                        next_col=col+dx[dir]

                        if next_row < 0 or next_row>=num or next_col < 0 or next_col>=num:
                            continue

                        if graph[next_row][next_col] <= height:
                            continue
                        queue.append((next_row,next_col))
                count+=1
        max_count=max(max_count,count)
    
    return max_count


    
if __name__ == "__main__":
    num=0
    max_height=0
    graph=[]

    with open("input2468.txt","r") as file:
        num=int(file.readline())
        for _ in range(num):
            row=list(map(int,file.readline().split()))
            graph.append(row)
            max_height=max(max_height,max(row))
    
    print(solution())