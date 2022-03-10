def solution(height,width,blocks):
  value=0
  for i in range(1,width-1):
      left=max(blocks[:i])
      right=max(blocks[i+1:])
      
      max_height=min(left,right)
      
      if max_height > blocks[i]:
          value+=(max_height-blocks[i])
  return value
    
  
  
if __name__ == "__main__":
  width,height=0,0
  blocks=[]

  with open("input14719.txt","r") as file:
    width,height=map(int,file.readline().split())
    blocks=list(map(int,file.readline().split()))
  print(solution(height,width,blocks))