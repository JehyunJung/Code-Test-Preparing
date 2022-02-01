from math import inf

def solution():
  min_time=inf
  result=0

  for block_count in range(257):
    required_blocks=0
    trash_blocks=0
    current_inventory=b

    for block_point in block_map:
      difference=block_point - block_count
      if difference>0:
        trash_blocks+=difference
      else:
        required_blocks+=abs(difference)

    current_inventory=b+trash_blocks
    if current_inventory < required_blocks:
      break
    required_time=trash_blocks*2 + required_blocks
    if min_time >= required_time:
      min_time=required_time
      result=block_count
    
  return min_time,result



n,m,b=0,0,0
block_map=[]

with open("input18111.txt","r") as file:
  n,m,b=map(int,file.readline().split())
  for _ in range(n):
    block_map.extend(list(map(int,file.readline().split())))

print(block_map)
block_map.sort(reverse=True)

print(solution())