import os.path

def check_route(way):
    visited=[False]*n
    for i in range(n-1):
        if way[i]  < way[i+1]:
            if abs(way[i] - way[i+1]) >1:

                return 0
            height=way[i]
            for k in range(L):
                if i -k <0 or visited[i-k] or way[i-k]!=height:

                    return 0
                visited[i-k]=True 
        if way[i]  > way[i+1]:
            if abs(way[i] - way[i+1]) >1:

                return 0
            height=way[i+1]
            for k in range(L):
                if i+k+1 >=n or visited[i+k+1] or way[i+k+1]!=height:

                    return 0
                visited[i+k+1]=True 

    return 1

def solution():
    count=0

    #row
    for i in range(n):
        count+=check_route(graph[i])
    #col
    for i in range(n):
        count+=check_route([graph[j][i] for j in range(n)])
    return count
if __name__ == "__main__":


    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, "input14890.txt")
    n,L=0,0
    graph=[]

    with open(filename,"r") as file:
        n,L=map(int,file.readline().split())
        graph=[list(map(int,file.readline().split())) for _ in range(n)]
    print(solution())
