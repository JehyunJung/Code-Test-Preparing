def checkIfTrue():
  dy=[-1,0,1,0]
  dx=[0,1,0,-1]

  for row,col in teacher_locations:
    for dir in range(4):
      for times in range(n):
        new_row=row+dy[dir]*times
        new_col=col+dx[dir]*times

        if new_row < 0 or new_row >=n or new_col < 0 or new_col >=n:
          continue
          
        if map_data[new_row][new_col] == 'O':
          break
          
        elif map_data[new_row][new_col] == 'S':
          return False

  return True

def dfs(count):
  global answer
  for row in range(n):
    for col in range(n):
      if count==3:
          if checkIfTrue():
            answer='YES'
            return
          else:
            return

      if map_data[row][col]=='X':
        map_data[row][col]='O'
        dfs(count+1)
        map_data[row][col]='X'   


map_data=[]
teacher_locations=[]
answer='NO'
with open("input20.txt","r") as file:
  n=int(file.readline())
  for row in range(n):
    map_data.append(list(map(str,file.readline().split())))
    for col in range(n):
      if map_data[row][col] == 'T':
        teacher_locations.append((row,col))

dfs(0)
print(answer)
  
