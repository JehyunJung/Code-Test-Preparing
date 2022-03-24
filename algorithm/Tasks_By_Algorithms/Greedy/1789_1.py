from math import sqrt
def solution():
  return int((-1+sqrt(1+8*S))//2)
    
if __name__ =="__main__":
  S=0
  with open("input1789.txt","r") as file:
    S=int(file.readline())

  print(solution())