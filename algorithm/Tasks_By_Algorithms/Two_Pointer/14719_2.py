import re
def solution(height,width,blocks):
  max_height=max(blocks)
  block_map=[["0"] *width for _ in range(max_height)]

  index=0
  for block in blocks:
    for j in range(block):
      block_map[max_height-j-1][index]="1"
    index+=1
  value=0

  for block_segment in block_map:
    print(block_segment)
  
  for block_segment in block_map:
      block_segment_str="".join(block_segment)
      for groups in re.findall("1[0]+1",block_segment_str):
        value+=groups.count("0")
  return value
    
  
  
if __name__ == "__main__":
  width,height=0,0
  blocks=[]

  with open("input14719.txt","r") as file:
    height,width=map(int,file.readline().split())
    blocks=list(map(int,file.readline().split()))
  print(solution(height,width,blocks))