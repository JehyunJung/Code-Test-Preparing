def two_pointer(array,i):
    start,end=0,n-2
    target_number=numbers[i]
    while start<end:
        result=array[start]+array[end]

        if result==target_number:
            return True
        
        elif result < target_number:
            start+=1

        elif result > target_number:
            end-=1
    
    return False

def solution():
    count=0
    numbers.sort()
    for i in range(n):
        if two_pointer(numbers[:i]+numbers[i+1:],i):
            count+=1
    return count

if __name__ == "__main__":
    with open("input1253.txt","r") as file:
        n=int(file.readline())
        numbers=list(map(int,file.readline().split()))
    print(solution())