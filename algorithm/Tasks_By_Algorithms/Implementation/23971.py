from math import ceil
def solution():
    print(ceil(h/(n+1)) * ceil(w/(m+1)))
if __name__ == '__main__':
    with open("input23971.txt", "r") as file:
        h,w,n,m=map(int,file.readline().split())
    
    solution()