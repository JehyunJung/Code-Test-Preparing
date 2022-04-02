from collections import deque
def solution():
    global count,answer
    queue=deque()
    queue.append(A)
    visited[A]=0
  
    while queue:
        temp=queue.popleft()
      
        print(temp)
      
        if temp==B:
            break
            
        if 0 <= temp-1 <= 100000 and visited[temp-1]==-1:
            visited[temp-1]=visited[temp]+1
            queue.append(temp-1)
              
        if 0<=temp*2 <=100000 and visited[temp*2] == -1:
            visited[temp*2]=visited[temp]
            queue.append(temp*2)
            
        if 0<=temp+1 <=100000 and visited[temp+1]==-1:
            visited[temp+1]=visited[temp]+1
            queue.append(temp+1)
          
  
if __name__ == "__main__":
    A,B=0,0
    with open("input12851.txt","r") as file:
      A,B=map(int,file.readline().split())
    visited=[0]*100001
    solution()
    print(visited[B])
