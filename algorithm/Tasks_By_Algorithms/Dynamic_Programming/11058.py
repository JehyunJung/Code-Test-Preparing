def solution(step,clipboard,count,path):
  global answer

  if step>n:
    return
    
  if step==n:
    if answer<count:
      answer=max(answer,count)
      print(path,answer)
    return

  #A
  solution(step+1,clipboard,count+1,path+['A'])
  
  #ctrl+A + ctrl+C
  if count>0:
      solution(step+2,count,count,path+['cltrA','cltrC'])   
    
  #ctrl+V
  solution(step+1,clipboard,count+clipboard,path+['cltrV'])

  


if __name__ =="__main__":
  n=0
  with open("input11058.txt","r") as file:
    n=int(file.readline())
  answer=0
  solution(0,0,0,[])
  print(answer)