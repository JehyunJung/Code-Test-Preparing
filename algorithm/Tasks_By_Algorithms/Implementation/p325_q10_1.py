m,n=0,0
key=[]
lock=[]

with open("input10.txt","r") as file:
  m,n=map(int,file.readline().split())
  for _ in range(m):
    key.append(list(map(int,file.readline().split())))
  for _ in range(n):
    lock.append(list(map(int,file.readline().split())))

def rotation(graph,n):
  temp=[]
  for i in range(n):
    row=[]
    for j in range(n):
      row.append(graph[n-j-1][i])
    temp.append(row)
  return temp

def check_if_true(lock,n):
  for i in range(n):
    for j in range(n):
      if lock[i][j]!=1:
        return False
  return True
 
def solution(m,n,key,lock):
  for i in range(4):
    key=rotation(key,m)
    for shift_y in range(n):
      for shift_x in range(n):
          for i in range(m):
            for j in range(m):
              new_y=i+shift_y
              new_x=j+shift_x
              if new_y >=m or new_x>=m:
                continue
              lock[new_y][new_x]+=key[i][j]
                  
          result=check_if_true(lock,n)

          if result:
            return True

          for i in range(m):
            for j in range(m):
              new_y=i+shift_y
              new_x=j+shift_x
              if new_y >=m or new_x>=m:
                continue
              lock[new_y][new_x]-=key[i][j]
    
  return False

print(solution(m,n,key,lock))
    
 