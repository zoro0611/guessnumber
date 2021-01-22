import random
start = int(input("請決定隨機數字開始值:"))
end = int(input("請決定隨機數字結束值: "))

r = random.randint(start, end) # 使用【random】裡面的【隨機整數】，定義隨機整數範圍落在1~100裏頭
count = 0
while True:
    count += 1   # count = count + 1
    guess = int(input("請猜一個數字: "))
    if guess > r:
        print("你猜的太大了")
    elif guess < r:
        print("你猜得太小了")
    else:
        print("恭喜答對了，這是你猜中的第", count, "次")
        break
    print("這是你猜的第", count, "次")
