def make_table(S):
  length=len(S)
  table=[0] * length
  idx=0

  for i in range(1,length):
    while idx > 0 and S[i]!=S[idx]:
      idx=table[idx-1]

    if S[i]==S[idx]:
      idx+=1
      table[i]=idx

  return table

def solution(P,S):
  P_length=len(P)
  S_length=len(S)

  table=make_table(S)
  idx=0
  for i in range(P_length):
    while idx>0 and P[i] != S[idx]:
      idx=table[idx-1]

    if P[i] == S[idx]:
      if idx == S_length-1:
        return 1
      else:
        idx+=1
  return 0
      
if __name__ == "__main__":
    P=""
    S=""
    testcases=0
    with open("inputkmp.txt","r") as file:
      testcases=int(file.readline())
      for _ in range(testcases):
        P=file.readline().strip()
        S=file.readline().strip()
        
        print(solution(P,S))