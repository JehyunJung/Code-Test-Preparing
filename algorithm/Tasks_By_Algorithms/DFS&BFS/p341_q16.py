from collections import deque

n,m=0,0
data = []
with open("input16.txt","r") as file:
  n, m = map(int, file.readline().split())
  for i in range(n):
      data.append(list(map(int, file.readline().split())))

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
max_result = 0
                
def get_score(copy):
    count=0
    for i in range(n):
        for j in range(m):
            if copy[i][j]==0:
                count+=1
    return count         
    
def bfs():
    global max_result
    copy = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            copy[i][j] = data[i][j]

    queue = deque()
    for i in range(n):
        for j in range(m):
            if copy[i][j] == 2:
                queue.append((i, j))
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]

            if 0 <= new_y and new_y<n and 0<=new_x and new_x < m:
                if copy[new_y][new_x] == 0:
                    copy[new_y][new_x] = 2
                    queue.append((new_y,new_x))
    max_result = max(max_result, get_score(copy))
    
def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                wall(cnt + 1)
                data[i][j] = 0

wall(0)
print(max_result)