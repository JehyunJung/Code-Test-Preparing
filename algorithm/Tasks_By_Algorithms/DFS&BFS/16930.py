from collections import deque
def solution():
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]
    checked=[[-1]*(col) for _ in range(row)]
    checked[start_row-1][start_col-1]=0
    queue=deque()
    queue.append((start_row-1,start_col-1))
    
    while queue:
        current_row,current_col=queue.popleft()

        if current_row == end_row-1 and current_col == end_col-1:
            break
          
        for dir in range(4):
            for times in range(1,k+1):
                new_row=current_row+dy[dir]*times
                new_col=current_col+dx[dir]*times

                if new_row <0 or new_row>=row or new_col<0 or new_col>=col:
                    break
                if graph[new_row][new_col]=="#":
                    break

                if checked[new_row][new_col]==-1:
                    checked[new_row][new_col]=checked[current_row][current_col]+1
                    queue.append((new_row,new_col))
                elif checked[new_row][new_col]==checked[current_row][current_col]+1:                           
                    continue #일단 쭉 가본다
                  
    for i in range(row):
        print(checked[i])
      
    return checked[end_row-1][end_col-1]
  
if __name__ == "__main__":
    row,col,k=0,0,0
    start_row,start_col,end_row,end_col=0,0,0,0
    graph=[]
    with open("input16930.txt","r") as file:
      row,col,k=map(int,file.readline().split())
      graph=[list(file.readline().strip()) for _ in range(row)]
      start_row,start_col,end_row,end_col=map(int,file.readline().split())
    
    print(solution())