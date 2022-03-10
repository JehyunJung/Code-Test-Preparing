def solution(N,k,tasks):
  operators=[]

  unplug_count=0
  
  while tasks:
    task=tasks.pop(0)
    if task in operators:
        continue
    elif len(operators) < N:
      operators.append(task)
    else:
      future_access=[0]*N
      
      for index, operator in enumerate(operators):
        if operator in tasks:
          future_access[index]=tasks.index(operator)
        else:
          future_access[index]=101
          
      index=future_access.index(max(future_access))
      del operators[index]
      operators.append(task)
      
      unplug_count+=1
        
      
  return unplug_count
  
if __name__ == "__main__":
  N,k=0,0
  tasks=[]

  with open("input1700.txt","r") as file:
    N,k=map(int,file.readline().split())
    tasks=list(map(int,file.readline().split()))

  print(solution(N,k,tasks))