def solution():
    di=[0] *(101)
    di[0]=0
    di[1]=1
    di[2]=1
    di[3]=1
    di[4]=2
    di[5]=2

    for i in range(6,num+1):
        di[i]=di[i-1]+di[i-5]

    return di[num]


if __name__ == "__main__":
    test_cases=0
    num=0
    with open("input9461.txt","r") as file:
        test_cases=int(file.readline())
        for _ in range(test_cases):
            num=int(file.readline())
            print(solution())
    