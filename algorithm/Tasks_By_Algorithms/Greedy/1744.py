def solution():
    
if __name__ == "__main__":
    n=0
    number=[]

    with open("input1744.txt","r") as file:
        n=int(file.readline())
        for _ in range(n):
            number.append(int(file.readline()))
    
    print(solution())