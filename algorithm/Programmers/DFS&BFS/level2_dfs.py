def solution(numbers, target):
    if len(numbers)==0 and target==0:
        return 1
    elif len(numbers)==0:
        return 0
    else:
        return solution(numbers[1:],target-numbers[0])+solution(numbers[1:],target+numbers[0])

if __name__ == "__main__":
    numbers=[]
    target=0
    with open("level2.txt","r") as file:
        numbers=list(map(int,file.readline().split()))
        target=int(file.readline())
    print(solution(numbers,target))