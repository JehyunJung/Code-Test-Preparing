from inspect import CO_NESTED
from math import inf
from pyexpat.errors import codes
def find_parents_collapsed(parents,x):
    if x!= parents[x]:
        parents[x]=find_parents_collapsed(parents,parents[x])
    return parents[x]

def union_parents(parents,x,y):
    pre_x=find_parents_collapsed(parents,x)
    pre_y=find_parents_collapsed(parents,y)

    if pre_x <pre_y:
        parents[pre_x]=pre_y
    else:
        parents[pre_y]=pre_x

def solution():
    parents=[i for i in range(num)]
    edges=[]
    edge_count=0
    result=0
    
    for i in range(num):
        for j in range(num):
            if i==j:
                continue

            min_value=min(abs(points[i][0]-points[j][0]),abs(points[i][1]-points[j][1]),abs(points[i][2]-points[j][2]))

            edges.append((min_value,i,j))
    
    edges.sort()

    while edge_count < num-1:
        cost,v1,v2=edges.pop(0)

        if find_parents_collapsed(parents,v1) != find_parents_collapsed(parents,v2):
            union_parents(parents,v1,v2)
            result+=cost
            edge_count+=1
    
    return result
if __name__ == "__main__":
    num=0
    points=[]

    with open("2887.txt","r") as file:
        num=int(file.readline())
        points=[list(map(int,file.readline().split())) for _ in range(num)]
    
    print(solution())