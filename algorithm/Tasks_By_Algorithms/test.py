from collections import deque
from os.path import dirname,join

def ccw(point1,point2,point3):
    return (point1[0] * point2[1] - point2[0] * point1[1])+(point2[0] * point3[1] - point3[0] * point2[1])+(point3[0] * point1[1] - point1[0] *point3[1])
    
def solution():
    max_count=0
    for index in range(n):
        count=0
        if 0 < index:   
            left_highest_index=index-1
            count+=1
            for left_index in range(index-2,-1,-1):
                if ccw((index,buildings[index]),(left_highest_index,buildings[left_highest_index]),(left_index,buildings[left_index])) < 0:
                    left_highest_index=left_index
                    count+=1
                    
        if index < n-1:
            right_highest_index=index+1
            count+=1
            for right_index in range(index+2,n):
                if ccw((index,buildings[index]),(right_highest_index,buildings[right_highest_index]),(right_index,buildings[right_index])) > 0:
                    right_highest_index=right_index
                    count+=1
                
        max_count=max(max_count,count)
    
    print(max_count)

if __name__ == "__main__":
    scriptpath = dirname(__file__)
    filename = join(scriptpath, 'input.txt')

    with open(filename, "r") as file:
        n=int(file.readline())
        buildings=list(map(int, file.readline().split()))

    solution()

