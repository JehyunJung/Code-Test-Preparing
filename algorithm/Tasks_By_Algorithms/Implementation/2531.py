from collections import defaultdict
def solution():
    sushie_counter=defaultdict(int)

    for i in range(k):
        sushie_counter[sushies[i]]+=1
    
    #쿠폰으로 들어간 초밥 추가
    sushie_counter[c]+=1

    count=len(sushie_counter)
    max_count=count

    for index in range(k,n+k):
        #start위치의 초밥 제거
        start=sushies[index-k]
        sushie_counter[start]-=1    
        #초밥의 갯수가 0이라는 것은 k개 연속으로 먹은 초밥 중에 없다는 것 --> 종류 1감소
        if sushie_counter[start]==0:
            del sushie_counter[start]
            count-=1

        #end 위치의 초밥 추가
        sushie_counter[sushies[index%n]]+=1
        #처음 추가되는 초밥이면 종류 1 증가
        if sushie_counter[sushies[index%n]]==1:
            count+=1
        max_count=max(max_count,count)

    return max_count
if __name__ == "__main__":
    with open("input2531.txt","r") as file:
        n,d,k,c=map(int,file.readline().split())
        sushies=[int(file.readline()) for _ in range(n)]

    print(solution())