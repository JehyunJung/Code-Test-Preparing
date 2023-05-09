import sys
from collections import deque

def bfs(start_vertex):
    global true_bit
    queue=deque([(start_vertex)])

    while queue:
        vertex=queue.popleft()

        for adj_vertex in graph[vertex]:
            adj_vertex_bit=1 << adj_vertex
            if true_bit & adj_vertex_bit == adj_vertex_bit:
                continue
            true_bit |= adj_vertex_bit
            queue.append(adj_vertex)
                


def solution():
    global true_bit
    for true_person in trues:
        true_person_bit=1 << true_person
        if true_bit & true_person_bit == true_person_bit:
            continue
        true_bit |= true_person_bit
        bfs(true_person)

    count=0
    for party_bit in parties:
        if party_bit & true_bit == party_bit:
            continue
        count+=1

    print(count)

if __name__ == '__main__':
    sys.stdin=open("input1043.txt","r")
    n,m=map(int,input().split())
    trues=list(map(int,input().split()[1:]))
    true_bit=0
    parties=[]
    graph=[set() for _ in range(n+1)]

    for _ in range(m):
        party=list(map(int,input().split()))
        length=party[0]
        src=party[1]
        party_bit = 1 << src
        for i in range(2,length+1):
            dest=party[i]
            party_bit |= 1 << dest
            graph[src].add(dest)
            graph[dest].add(src)
        parties.append(party_bit)

    solution()