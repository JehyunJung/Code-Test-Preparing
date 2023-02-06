def solution():
    if n==0:
        print(1)
        return
    else:
        if n==p and scores[-1]>=new_score:
            print(-1)
        else:
            rank=1
            for score in scores:
                if new_score>=score:
                    print(rank)
                    break
                rank+=1
    
if __name__ == "__main__":
    with open("input1205.txt","r") as file:
        n,new_score,p=map(int,file.readline().split())
        scores=list(map(int,file.readline().split()))
    solution()