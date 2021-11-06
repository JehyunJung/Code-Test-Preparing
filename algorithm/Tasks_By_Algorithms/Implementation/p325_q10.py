m,n=0,0
key=[]
lock=[]
new_lock=[]

with open("input10.txt","r") as file:
  m,n=map(int,file.readline().split())
  for _ in range(m):
    key.append(list(map(int,file.readline().split())))
  for _ in range(n):
    lock.append(list(map(int,file.readline().split())))

new_lock=[[0]*(n*3) for _ in range(n*3)]

for i in range(n):
  for j in range(n):
    new_lock[n+i][n+j]=lock[i][j]

def rotation(graph,n):
  temp=[]
  for i in range(n):
    row=[]
    for j in range(n):
      row.append(graph[n-j-1][i])
    temp.append(row)
  return temp

def check_if_true(new_lock,n):
  for i in range(n,n*2):
    for j in range(n,n*2):
      if new_lock[i][j]!=1:
        return False
  return True
 
def solution(m,n,key,new_lock):
  for i in range(4):
    key=rotation(key,m)
    for shift_y in range(n*2):
      for shift_x in range(n*2):
          for i in range(m):
            for j in range(m):
              new_lock[i+shift_y][j+shift_x]+=key[i][j]
                  
          result=check_if_true(new_lock,n)
          if result:
            return True

          for i in range(m):
            for j in range(m):
              new_lock[i+shift_y][j+shift_x]-=key[i][j]
    
  return False

print(solution(m,n,key,new_lock))
    
 