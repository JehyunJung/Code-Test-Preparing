class Point:
  def __init__(self,row,col):
    self.row=row
    self.col=col

  def __eq__(self,other):
    if self.row==other.row and self.col==other.col:
      return True
    else:
      return False

  def row_boundary_check(self,n):
    if self.row < 0 or self.row>=n:
      return True
    else:
      return False

  def col_boundary_check(self,n):
    if self.col< 0 or self.col>=n:
      return True
    else:
      return False

      
  def __repr__(self):
        return "[%d,%d]" % (self.row, self.col)
    
      
def solution(state,head,tail):
  global count

  if head.row_boundary_check(n) or head.col_boundary_check(n) or tail.row_boundary_check(n) or tail.col_boundary_check(n):
    return

  #wall check
  if state !=2:
    if graph[tail.row][tail.col]==1:
      return
  else:
    if graph[tail.row-1][tail.col]==1 or graph[tail.row][tail.col-1]==1 or graph[tail.row][tail.col]==1:
      return
    
  if tail == Point(n-1,n-1):
    count+=1
    return
  
  if state==0:
    #move right
    solution(state,tail,Point(tail.row,tail.col+1))

    #rotate right
    solution(2,tail,Point(tail.row+1,tail.col+1))

  if state==1:
    #move down
    solution(state,tail,Point(tail.row+1,tail.col))

    #rotate left
    solution(2,tail,Point(tail.row+1,tail.col+1))

  if state==2:
    #rotate left
    solution(0,tail,Point(tail.row,tail.col+1))

    #rotate right
    solution(1,tail,Point(tail.row+1,tail.col))

    #move diagonal
    solution(state,tail,Point(tail.row+1,tail.col+1))

    
  


if __name__ == "__main__":
  n=0
  graph=[]

  with open("input17070.txt","r") as file:
    n=int(file.readline())
    for _ in range(n):
      graph.append(list(map(int,file.readline().split())))
  
  count=0
  #state 0:horizontal, 1:vertical,2:diagonal
  solution(0,Point(0,0),Point(0,1))

  print(count)