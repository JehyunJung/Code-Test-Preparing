def solution():
    di=[0] * (31)
    di[0]=1
    di[2]=3

    if num % 2 ==1:
        return 0
    
    if num>=4:
        sub_sum=1
        for i in range(4,num+1):
            if i % 2== 1:
                continue
            di[i]=di[i-2]*3 + sub_sum*2
            sub_sum+=di[i-2]
    
    return di[num]

if __name__ == "__main__":
    num=0

    with open("input2133.txt","r") as file:
        num=int(file.readline())
    
    print(solution())