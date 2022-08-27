from collections import defaultdict
def solution():
    conversion=defaultdict(int)

    digits=[10**i for i in range(8)]
    
    for string in strings:
        length=len(string)
        for i in range(length):
            conversion[string[i]]+=digits[length-i-1]


    temp_list=[(value,index) for index,value in conversion.items()]
    temp_list.sort(key=lambda x: (-x[0]))
    print(temp_list)
    num=9
    for value,index in temp_list:
        conversion[index]=num
        num-=1
    
    result=0
    
    for string in strings:
        length=len(string)
        for i in range(length):
            string[i]=str(conversion[string[i]])
        result+=int("".join(string))

    return result 
if __name__ == "__main__":
    N=0
    strings=[]
    alpha_sets=[]
    with open("input1339.txt","r") as file:
        N=int(file.readline())
        for _ in range(N):
            string=list(file.readline().strip())
            strings.append(string)
            alpha_sets.extend(string)

    print(solution())