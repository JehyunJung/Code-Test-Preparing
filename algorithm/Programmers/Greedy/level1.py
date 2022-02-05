def solution(n, lost, reserve):
    answer = 0
    reserve_set=set(reserve)
    lost_set=set(lost)
    
    reserve=reserve_set-lost_set
    lost=lost_set-reserve_set
    
    reserve=set(reserve)
    lost=set(lost)
    
    for r in reserve:
        f=r-1
        b=r+1
        
        if f in lost:
            lost.remove(f)
        elif b in lost:
            lost.remove(b)
            
    answer=n-len(lost)
    return answer

if __name__ == "__main__":
  n,lost,reserve=0,[],[]

  with open("input1.txt","r") as file:
    n=int(file.readline())
    lost=list(map(int,file.readline().split()))
    reserve=list(map(int,file.readline().split()))

  print(solution(n,lost,reserve))