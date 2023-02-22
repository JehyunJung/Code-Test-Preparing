def solution():
    time=0
    candidates=[]

    for vote in votes:
        #이미 존재하는 학생이면 추천수를 올린다.
        for index in range(len(candidates)):
            vote_count,register_time,student_index=candidates[index]
            if vote==student_index:
                candidates[index]=(vote_count+1,register_time,student_index)
                break
        #사진틀에 없는 학생인 경우
        else:
            #사진틀에 남는 자리가 없는 경우 추천수가 가장 적은 학생(동률이면 그 중에서 등록된지 가장 오래된 학생) 제거
            if len(candidates) == n:
                candidates.sort()
                del candidates[0]
            candidates.append((1,time,vote))   
            time+=1
    
    candidates.sort(key=lambda x:x[2])
    for candidate in candidates:
        print(candidate[2],end=" ")
if __name__ == "__main__":
    with open("input1713.txt","r") as file:
        n=int(file.readline())
        n_votes=int(file.readline())
        votes=list(map(int,file.readline().split()))
    solution()