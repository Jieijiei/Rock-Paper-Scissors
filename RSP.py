import random
print("じゃんけんをしましょう！！0：グー、1：チョキ、2：パー")
userVictory = 0
userLose = 0
Even = 0
for i in range(10):
    com = random.randint(0,2)
    print("いきますよ、じゃーん...けーん...")
    User = input('数字を入力してください：')
    user = int(User)
    judge = (com + 3 - user) % 3
    if judge == 0:
        print("あいこ。")
        Even + 1
    if judge == 1:
        print("あなたの負け！")
        userLose + 1
    if judge == 2:
        print("あなたの勝ち！！")
        userVictory + 1
print(userLose)
print(userVictory)
print(Even)