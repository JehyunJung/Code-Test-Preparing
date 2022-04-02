from math import inf
def solution(count,temp):
  global answer
  if temp==B:
    answer=min(count,answer)
  
  if temp *2 <= B:
    solution(count+1,temp*2)
  if int(str(temp)+'1') <=B:
    solution(count+1,int(str(temp)+'1'))
  
if __name__ == "__main__":
  A,B=0,0
  with open("input16953.txt","r") as file:
    A,B=map(int,file.readline().split())
  answer=inf
  solution(1,A)
  if answer==inf:
    answer=-1
  print(answer)