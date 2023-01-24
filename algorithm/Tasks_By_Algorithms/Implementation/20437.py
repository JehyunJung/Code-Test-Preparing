from collections import defaultdict
from math import inf
def solution():
    for index in range(T):
        string=strings[index]
        k=ks[index]

        string_counter=defaultdict(list)
        #입력된 문자열에 대해 특정 문자에 대해 k개 이상을 만족하는 문자의 인덱스 정보를 파악한다.
        for i,char in enumerate(string):
            if string.count(char)>=k:
                string_counter[char].append(i)


        #만족하는 문자열이 없는 경우 -1 반환
        if len(string_counter) ==0:
            print(-1)
            continue

        min_length=inf
        max_length=0

        for char in string_counter:
            char_indexes=string_counter[char]
            index_length=len(char_indexes)
            for i in range(index_length-k+1):
                min_length=min(min_length,char_indexes[i+k-1]-char_indexes[i]+1)
                max_length=max(max_length,char_indexes[i+k-1]-char_indexes[i]+1)
        print(min_length,max_length)
if __name__ == "__main__":
    with open("input20437.txt","r") as file:
        T=int(file.readline())
        strings=[]
        ks=[]

        for _ in range(T):
            strings.append(file.readline().strip())
            ks.append(int(file.readline().strip()))
    
    solution()
