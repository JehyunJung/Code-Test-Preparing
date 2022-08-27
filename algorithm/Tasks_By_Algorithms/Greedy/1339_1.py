from itertools import permutations
from copy import deepcopy
def solution():
    conversion=dict()
    alpha_sets=[]

    for string in strings:
        alpha_sets.extend(string)
    
    alpha_sets=set(alpha_sets)
    max_result=0
    for permutation in permutations(alpha_sets):
        num=9
        for char in permutation:
            conversion[char]=num
            num-=1
        result=0
        for string in strings:
            length=len(string)
            temp=deepcopy(string)
            for index in range(length):
                temp[index]=str(conversion[temp[index]])
            result+=int("".join(temp))
        max_result=max(max_result,result)

    return max_result
            

       
if __name__ == "__main__":
    N=0
    strings=[]

    with open("input1339.txt","r") as file:
        N=int(file.readline())
        strings=[list(file.readline().strip()) for _ in range(N)]

    print(solution())