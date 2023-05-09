import sys

def solution(vertex):
    global dp

    childs=[]
    #자식이 있으면 계속 내려간다.
    if tree[vertex] != []:
        for adj_vertex in tree[vertex]:
            solution(adj_vertex)
            #자식 노드가 처리가 되면 자식 노드가 처리 되기 위한 시간 값을 저장
            childs.append(dp[adj_vertex])
    #더 이상 자식이 없는 경우
    else:
        return 0
    #시간이 많이 걸리는 자식을 먼저 처리할 수 있도록 한다.
    childs.sort(reverse=True)

    #가장 오래 걸리는 시간 값을 저장한다.
    dp[vertex]=max([childs[i] + i+1 for i in range(len(childs))])
    return dp[vertex]

if __name__ == '__main__':
    sys.stdin=open("input1135.txt","r")
    n=int(input())
    child_infos=list(map(int,input().split()))
    tree=[[] for _ in range(n)]

    for child in range(1,n):
        parent=child_infos[child]
        tree[parent].append(child)
    
    dp=[0] * n
    solution(0)
    print(dp[0])
