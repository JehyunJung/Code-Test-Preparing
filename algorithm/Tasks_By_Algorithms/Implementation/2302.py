def solution():
    di=[0] * 41
    di[0]=1

    for i in range(1,41):
        di[i]=di[i-1]+di[i-2]

    start=1
    result=1
    for vip in vips:
        result*=di[vip-start]
        start=vip+1

    result*=di[n_seats-start+1]

    return result

if __name__ == "__main__":
    n_seats=0
    n_vips=0
    vips=[]

    with open("input2302.txt","r") as file:
        n_seats=int(file.readline())
        n_vips=int(file.readline())
        for _ in range(n_vips):
            vips.append(int(file.readline().strip()))
    print(solution())