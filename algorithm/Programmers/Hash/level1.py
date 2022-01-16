from collections import Counter
def solution(participant,completion):
    return list((Counter(participant)-Counter(completion)).keys())[0]


if __name__=="__main__":
  participant=[]
  completion=[]
  with open("level1.txt","r") as file:
    participant=list(map(str,file.readline().split()))
    completion=list(map(str,file.readline().split()))
  
  print(solution(participant,completion))