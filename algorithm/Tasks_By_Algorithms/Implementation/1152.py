def solution(strings):
  return len(strings)
if __name__ == "__main__":
  str_list=[]

  with open("input1152.txt","r") as file:
    str_list=list(map(str,file.readline().split()))
  
  print(solution(str_list))