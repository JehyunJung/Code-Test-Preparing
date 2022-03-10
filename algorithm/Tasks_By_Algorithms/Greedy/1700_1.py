from collections import Counter
def solution(N,k,tasks):
  operators=[0]*(N)

  unplug_count=0
  
  while tasks:
    task=tasks.pop(0)
    print("task:",task)
    print("operators: ",operators)
    if task in operators:
        continue
    else:
      check=False
      for index in range(len(operators)):
        if operators[index]==0:
          operators[index]=task
          check=True
          break
      if not check:
        candidates=[]
        weight=[0]*(k+1)
        for index in range(N):
          future_key=operators[index]
          candidates.append(future_key)
          weight[future_key]=N-index
          
        if not set(operators).difference(candidates):
          min_index=0
          min_weight=k
          for index in range(len(operators)):
            if weight[index] < min_weight:
              min_index=index
          operators[min_index]=task
          unplug_count+=1
        else:
          for index in range(len(operators)):
            if operators[index] not in candidates:
              operators[index]=task
              unplug_count+=1
              break

  return unplug_count
  
if __name__ == "__main__":
  N,k=0,0
  tasks=[]

  with open("input1700.txt","r") as file:
    N,k=map(int,file.readline().split())
    tasks=list(map(int,file.readline().split()))

  print(solution(N,k,tasks))