def solution():
    previous_high=towers[0]
    max_high=towers[0]
    previous_high_index=0
    previous_indexes=[-1] * n

    results=[0]
    for i in range(1,n):
        #이전 탑보다 큰 경우
        if towers[i] > towers[i-1]:
            #기존의 최대 높이보다 큰 경우, 최대높이와 이전 최대 높이를 갱신한다.
            if towers[i]>=max_high:
                max_high=towers[i]
                previous_indexes[i]=-1
                results.append(0)
            else:
                index=previous_high_index
                while True:
                    #이전 최대 높이가 높은 경우, 그 이전의 최대 높이를 찾을때까지 반복문을 수행해서 해당 인덱스를 previous_index으로 설정
                    if towers[i] > towers[index]:
                        index=previous_indexes[index]
                    else:
                        break
                previous_indexes[i]=index
                results.append(index+1)
            previous_high_index,previous_high=i,towers[i]
        #이전 탑보다 작은 경우에는, 이전 최대 크기를 이전 탑의 크기로 설정하고, 그 이전의 최고 크기와 연결해준다.
        else:
            previous_indexes[i]=previous_high_index
            previous_high_index,previous_high=i-1,towers[i-1]
            results.append(i) 

    print(*results)





if __name__ == "__main__":
    with open("input2493.txt","r") as file:
        n=int(file.readline())
        towers=list(map(int,file.readline().split()))

    solution()