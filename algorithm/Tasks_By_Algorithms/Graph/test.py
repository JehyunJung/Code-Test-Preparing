import heapq

def find_parents_compressed(parents,x):
    if x!= parents[x]:
        parents[x]=find_parents_compressed(parents,parents[x])
    return parents[x]

def union_parents(parents,x,y):
    pre_x=find_parents_compressed(parents,x)
    pre_y=find_parents_compressed(parents,y)

    if pre_x < pre_y:
        parents[pre_x]=pre_y
    else:
        parents[pre_y]=pre_x

def solution():
    #간선 집합 정렬
    edges.sort(key=lambda x:x[2])
    parents=[0] * (v+1)
    for i in range(1,v+1):
        parents[i]=i

    result=0
    edge_count=0
    max_cost=0
    
    for v1,v2,cost in edges:
        #cycle 여부를 확인하기 위해 disjoint_set을 이용한다.
        if find_parents_compressed(parents,v1) != find_parents_compressed(parents,v2):
            union_parents(parents,v1,v2)
            result+=cost
            max_cost=max(max_cost,cost)
            edge_count+=1
            if edge_count==v-1:
                break
            else:
                continue
    return result-max_cost

if __name__ == "__main__":
    with open("test.txt","r") as file:    
        v,e=map(int,file.readline().split())
        edges=[list(map(int,file.readline().split())) for _ in range(e)]

    print(solution())