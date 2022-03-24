def solution():
  n=1
  while n*(n+1) <= 2*S:
    n+=1
  return n-1
    
    
if __name__ =="__main__":
  S=0
  with open("input1789.txt","r") as file:
    S=int(file.readline())

  print(solution())