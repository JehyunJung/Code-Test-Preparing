def main():
  n=int(input("거스름으로 바꿔야할 돈을 입력해주세요: "))

  coin_types=[500,100,50,10]
  count=0
  for coin_type in coin_types:
    count+=n//coin_type
    n%=coin_type
  print(count)

if __name__ == "__main__":
  main()