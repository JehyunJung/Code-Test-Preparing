def mergeSort(arr):
    length=len(arr)

    if length<=1:
        return arr
    
    mid=length//2

    left=mergeSort(arr[:mid])
    right=mergeSort(arr[mid:])
    return merge(left,right)

def merge(left,right):
    global answer
    i,j=0,0
    left_length,right_length=len(left),len(right)
    temp=[]

    while i < left_length and j < right_length:
        if left[i] <= right[j]:
            temp.append(left[i])
            i+=1
        else:
            answer+=(left_length-i)
            temp.append(right[j])
            j+=1
    
    temp+=left[i:]
    temp+=right[j:]
    return temp

if __name__ == "__main__":
    with open("input10090.txt","r") as file:
        n=int(file.readline())
        numbers=list(map(int,file.readline().split()))
    answer=0
    mergeSort(numbers)
    print(answer)