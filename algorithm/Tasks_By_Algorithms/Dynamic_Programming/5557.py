def solution(step,temp):
  global answer
  if temp <0 or temp >20:
    return
  if step==num-1:
    if temp==target:
      answer+=1
    return
    

  solution(step+1,temp+numbers[step])
  solution(step+1,temp-numbers[step])
  
  
if __name__ == "__main__":
  num=0
  numbers=[]

  with open("input5557.txt","r") as file:
    num=int(file.readline())
    numbers=list(map(int,file.readline().split()))
  answer=0
  target=numbers[-1]
  solution(0,0)
  print(answer)