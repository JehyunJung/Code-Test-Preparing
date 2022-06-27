from audioop import add
from ntpath import join
import os

def solution():
    global nutrition_level,graph
    dy=[-1,-1,-1,0,1,1,1,0]
    dx=[-1,0,1,1,1,0,-1,-1]
    for _ in range(K):
        dead_map=[[0]*N for _ in range(N)]
        # 봄
        for i in range(N):
            for j in range(N):
                if graph[i][j]!=0:
                    trees=graph[i][j]
                    trees.sort()
                    temp=[]
                    dead_trees=0
                    while trees:
                        tree=trees.pop(0)
                        if tree <= nutrition_level[i][j]:
                            temp.append(tree+1)
                            nutrition_level[i][j]-=tree
                        else:
                            dead_trees+=tree       
                    graph[i][j]=temp
                    dead_map[i][j]=dead_trees
                        
        #여름
        for i in range(N):
            for j in range(N):
                if dead_map[i][j] !=0:
                    nutrition_level[i][j]+=dead_map[i][j]//2
        
        #가을
        new_growings=[]
        for i in range(N):
            for j in range(N):
                if graph[i][j]!=0:
                    trees=graph[i][j]
                    for tree in trees:
                        if tree % 5 !=0:
                            continue
                        for dir in range(8):
                            new_row=i+dy[dir]
                            new_col=j+dx[dir]

                            if new_row < 0 or new_row >=N or new_col < 0 or new_col >=N:
                                continue
                            new_growings.append((new_row,new_col))
        for row,col in new_growings:
            if graph[row][col]==0:
                graph[row][col]=[]
            graph[row][col].append(1)

        #겨울
        for i in range(N):
            for j in range(N):
                nutrition_level[i][j]+=adding_nutrition_level[i][j]

    count=0
    for i in range(N):
        for j in range(N):
            if graph[i][j]!=0:
                count+=len(graph[i][j])
    return count                    


if __name__ == "__main__":
    N,M,K=0,0,0

    adding_nutrition_level=[]
    nutrition_level=[]
    trees=[]
    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, "input16235.txt")
    with open(filename,"r") as file:
        N,M,K=map(int,file.readline().split())
        adding_nutrition_level=[list(map(int,file.readline().split())) for _ in range(N)]
        nutrition_level=[[5]*N for _ in range(N)]
        graph=[[0] * N for _ in range(N)]

        for _ in range(M):
            row,col,age=map(int,file.readline().split())
            if graph[row-1][col-1]==0:
                graph[row-1][col-1]=[]
            graph[row-1][col-1].append(age)
    print(solution())
