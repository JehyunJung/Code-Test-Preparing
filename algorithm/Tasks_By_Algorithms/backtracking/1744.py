from heapq import heappush, heappop

def solution():
    result=0

    plus_group=[]
    minus_group=[]
    zero_count=False

    for number in numbers:
        if number > 0 :
            heappush(plus_group,-number)
        elif number < 0:
            heappush(minus_group,number)
        else:
            zero_count=True
    
    #양수 처리
    while len(plus_group) >=2:
        op1=-(heappop(plus_group))
        op2=-(heappop(plus_group))
        #1은 곱하지 않는다
        if op1 ==1 or op2 ==1:
            result+=(op1+op2)
            break

        result+=op1*op2

     #남아 있는 양수 값은 더한다
    result-=sum(plus_group)

    #음수 처리
    while len(minus_group) >=2:

        op1=heappop(minus_group)
        op2=heappop(minus_group)
        
        result+=op1*op2
        
    #만약 0이 있게 되면 이는 음수와 곱해서 0으로 만드는것이 가장 큰 값을 만든다.
    if not zero_count:
        result+=sum(minus_group)
    
    return result


if __name__ == "__main__":
    N=0
    numbers=[]
    with open("input1744.txt","r") as file:
        N=int(file.readline())
        numbers=[int(file.readline()) for _ in range(N)]
    
    print(solution())