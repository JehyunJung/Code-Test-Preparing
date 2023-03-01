def solution(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return solution(n-1)+solution(n-2)

if __name__ == "__main__":
    with open("input2748.txt","r") as file:
        n=int(file.readline())
    print(solution(n))