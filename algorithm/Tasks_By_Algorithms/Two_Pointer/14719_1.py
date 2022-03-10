import re
def solution(height,width,blocks):
  max_height=max(blocks)
  block_map=[[0] *width for _ in range(max_height)]

  index=0
  for block in blocks:
    for j in range(block):
      block_map[max_height-j-1][index]=1
    index+=1
  value=0
  
  for block_segment in block_map:
    prev_data=block_segment[0]
    check=False
    temp=0
    for block_point in block_segment[1:]:
      if prev_data==1 and block_point==0:
        check=True
        temp+=1
      elif check:
        if block_point==0:
          temp+=1
        else:
          value+=temp
          temp=0
          check=False
      prev_data=block_point
      
  return value
    
  
  
if __name__ == "__main__":
  width,height=0,0
  blocks=[]

  with open("input14719.txt","r") as file:
    height,width=map(int,file.readline().split())
    blocks=list(map(int,file.readline().split()))
  print(solution(height,width,blocks))