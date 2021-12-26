from collections import deque

def topological_sort():
  queue=deque()

  for i in range(1,v+1):
    if indegree[i]==0:
      queue.append(i)

  for i in range(v):
    global cycle,confuse
    if len(queue) ==0 :
      cycle=True
      return

    if len(queue)>1:
      confuse=True
      return

    vertex=queue.popleft()
    result.append(vertex)

    for i in range(1,v+1):
      if graph[vertex][i]:
        indegree[i]-=1

        if indegree[i]==0:
          queue.append(i)


test_cases=0
v,m=0,0
graph=[]
rank_data=[]
indegree=[]
with open("input45.txt") as file:
  test_cases=int(file.readline())
  for _ in range(test_cases):
    v=int(file.readline())
    rank_data=list(map(int,file.readline().split()))
    graph=[[False]*(v+1) for _ in range(v+1)]
    indegree=[0]*(v+1)
    for i in range(v):
      for j in range(i+1,v):
        graph[rank_data[i]][rank_data[j]]=True
        indegree[rank_data[j]]+=1

    m=int(file.readline())

    for _ in range(m):
      v1,v2=map(int,file.readline().split())
      if graph[v1][v2]:
        graph[v1][v2]=False
        graph[v2][v1]=True
        indegree[v2]-=1
        indegree[v1]+=1
      else:
        graph[v1][v2]=True
        graph[v2][v1]=False
        indegree[v1]-=1
        indegree[v2]+=1

    result=[]
    cycle=False
    confuse=False
    topological_sort()


    if cycle:
      print("IMPOSSIBLE")
    elif confuse:
      print("?")
    else:
      for i in range(v):
        print(result[i],end=" ")
      print()