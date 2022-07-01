def ifPseudoPelindrom(string, start,end):
    while start <= end:
        if string[start]==string[end]:
            start+=1
            end-=1
        else:
            return False
    return True

def ifPelindrom(string):
    start=0
    end=len(string)-1
    while start<end:
        if string[start]==string[end]:
            start+=1
            end-=1
            continue
        
        else:
            check_left=ifPseudoPelindrom(string,start+1,end)
            check_right=ifPseudoPelindrom(string,start,end-1)

            if check_left or check_right:
                return 1
            else:
                return 2

    return 0
    

def solution():
    for string in strings:
        print(ifPelindrom(string))
        


if __name__ == "__main__":
    num=0
    strings=[]

    with open("input17609.txt","r") as file:
        num=int(file.readline())

        strings=[list(file.readline().strip()) for _ in range(num)]
    solution()