def solution(P,S):
  if S in P:
    return 1
  else:
    return 0
if __name__ == "__main__":
  P,S="",""
  with open("input16916.txt","r") as file:
    P=file.readline()
    S=file.readline()

  print(solution(P,S))