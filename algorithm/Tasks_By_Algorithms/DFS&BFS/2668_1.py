import sys
def dfs(start_vertex,current_vertex,visited):
    global answer
    next_vertex=numbers[current_vertex]

    if next_vertex in visited:
        if next_vertex == start_vertex:
            answer.update(visited)
        return
    
    visited.add(next_vertex)
    
    dfs(start_vertex,next_vertex,visited)

def solution():
    for number in numbers:
        visited=set([number])
        dfs(number,numbers[number],visited)

    print(len(answer))
    print("\n".join(map(lambda x: str(x+1),sorted(answer))))
if __name__ == "__main__":
    sys.stdin=open("input2668.txt","r")
    n=int(input())
    numbers=[int(input())-1 for _ in range(n)]
    answer=set()

    solution()