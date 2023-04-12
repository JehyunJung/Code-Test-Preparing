def line_function(slope,intercept,x):
    return slope*x+intercept

def check(left_index,right_index):
    left_height=buildings[left_index]
    right_height=buildings[right_index]

    slope=float(right_height-left_height)/(right_index-left_index)
    intercept=-slope*left_index+left_height

    for index in range(left_index+1,right_index):
        if line_function(slope,intercept,index)<=buildings[index]:
            return False
    
    return True

    
def solution():
    max_count=0
    for index in range(n):
        count=0
        for left_index in range(index-1,-1,-1):
            if check(left_index,index):
                count+=1
        for right_index in range(index+1,n):
            if check(index,right_index):
                count+=1
        max_count=max(max_count,count)
    
    print(max_count)

if __name__ == "__main__":
    with open("input1027.txt", "r") as file:
        n=int(file.readline())
        buildings=list(map(int, file.readline().split()))

    solution()
