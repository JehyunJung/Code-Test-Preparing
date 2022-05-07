from collections import deque
def solution(n, computers):
    answer = 0
    visited=[False] * n
    for i in range(n):
        if not visited[i]:
            queue=deque([i])
            while queue:
                vertex=queue.popleft()
                visited[vertex]=True
        
                for j in range(n):
                    if vertex == j:
                        continue
                    if computers[vertex][j]==1 and not visited[j]:
                        queue.append(j)
            answer+=1
            
    return answer
  
if __name__ == "__main__":
    n=0
    computers=[]
    with open("level3_1.txt","r") as file:
        n=int(file.readline())
        computers=[list(map(int,file.readline().split())) for _ in range(n)]
    print(solution(n,computers))