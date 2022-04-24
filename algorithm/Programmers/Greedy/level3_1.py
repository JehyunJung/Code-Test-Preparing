def find_parent(parents,x):
    if x!=parents[x]:
        parents[x]=find_parent(parents,parents[x])
    return parents[x]

def union_parents(parents,x,y):
    pre_x=find_parent(parents,x)
    pre_y=find_parent(parents,y)
    
    if pre_x < pre_y:
        parents[pre_y]=pre_x
    else:
        parents[pre_x]=pre_y

def kruskal_algorithm(n,edges):
    parents=[i for i in range(n)]
    num_edges=0
    sum_cost=0

    while num_edges <n-1:
        v1,v2,cost=edges.pop(0)
        if find_parent(parents,v1) != find_parent(parents,v2):
            union_parents(parents,v1,v2)
            num_edges+=1
            sum_cost+=cost
            
    return sum_cost
    
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    answer=kruskal_algorithm(n,costs)
    return answer
  
if __name__ =="__main__":
    v,e=0,0
    costs=[]
    with open("input3_1.txt","r") as file:
        v,e=map(int,file.readline().split())
        costs=[list(map(int,file.readline().split())) for _ in range(e)]
    solution(v,costs)