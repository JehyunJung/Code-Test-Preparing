start_location=0
with open("input.txt","r") as file:
  start_location=file.readline()

move_types=[(-2,-1),(-2,1),(-1,2),(1,2),(2,-1),(2,1),(-1,-2),(1,-2)]
start_y=int(start_location[1])
start_x=ord(start_location[0])-ord("a") + 1

count=0

for move_y,move_x in move_types:
  
  ny=start_y+move_y
  nx=start_x+move_x

  if ny < 1 or ny > 8 or nx < 1 or nx > 8:
    continue
  count+=1
      
print(count)

