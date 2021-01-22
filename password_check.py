password = 'a123456'
left_chance = 3 #剩餘機會
#讓使用者最多輸入3次密碼
# 不對的話 印出"密碼錯誤! 還有_次機會"
# 對的話， 就印出 "登入成功!"

while left_chance > 0: #迴圈開始
    user_type = input("請輸入密碼: ")
    if user_type == password:
        print("登入成功!")
        break #逃出迴圈
    else:
        left_chance = left_chance - 1
        print("密碼錯誤! 還有", left_chance ,"次機會")

#這邊停止迴圈

