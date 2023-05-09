import sys
def solution():
    for _ in range(m):
        for party in parties:
            if trues & party:
                trues.union(party)


    count=0
    for party in parties:
        if trues & party:
            continue
        count+=1

    print(count) 

if __name__ == '__main__':
    sys.stdin=open("input1043.txt","r")
    n,m=map(int,input().split())
    trues=set(map(int,input().split()[1:]))
    parties=[set(map(int,input().split()[1:])) for _ in range(m)]

    solution()