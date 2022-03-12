import heapq
def find_parent(parent,x):
    if x!=parent[x]:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union(parent,x,y):
    pre_x=find_parent(parent,x)
    pre_y=find_parent(parent,y)
    
    if pre_x < pre_y:
        parent[pre_x]=pre_y
    else:
        parent[pre_y]=pre_x

def solution(N,edges):
    parent=[i for i in range(N+1)]
    sum_Of_Weight=0
    while edges:
        weight,v1,v2=heapq.heappop(edges)
        if find_parent(parent,v1)==find_parent(parent,v2):
            continue
        else:
            union(parent,v1,v2)
            sum_Of_Weight+=weight
    return sum_Of_Weight

if __name__ == "__main__":
  
    V,E=0,0
    edges=[]
    with open("input1197.txt","r") as file:
      V,E=map(int,file.readline().split())
      
      for _ in range(E):
          v1,v2,weight=map(int,file.readline().split())
          heapq.heappush(edges,(weight,v1,v2))
        
    print(solution(V,edges))