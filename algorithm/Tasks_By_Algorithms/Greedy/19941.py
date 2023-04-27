import sys
def solution():
    eat_count=0

    visited=[False]*n

    for i in range(n):
        if datas[i] != "P":
            continue
        for dx in range(-k,k+1):
            adj_index=i+dx

            if adj_index < 0 or adj_index >= n:
                continue

            if datas[adj_index] == "H" and not visited[adj_index]:
                eat_count+=1
                visited[adj_index]=True
                break
        
    print(eat_count)

if __name__ == "__main__":
    sys.stdin=open("input19941.txt","r")
    n,k=map(int,input().split())
    datas=list(input())
    solution()
        

