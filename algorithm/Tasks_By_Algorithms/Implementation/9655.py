def solution():
    if n % 4 ==1 or n % 4==3:
        print("SK")
    else:
        print("CY")
if __name__=="__main__":
    with open("input9655.txt","r") as file:
        n=int(file.readline())
    solution()