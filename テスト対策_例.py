import random

result = 0#最終的な得点
allPoint = 100#最高得点

#ここに問題を入れる
questions = [
    "データを情報にするために介在し、情報の一般化・抽象化によってまとめることができるもの",
    "加工したデータ",
    "集めたままのデータ",
    "データや 情報を概念化したもの",
    "事実がありのままに記録されているもの",
]

#ここに答えをいれる
#入れる順番に注意
answers = [
    "知識", 
    "2次データ", 
    "1次データ", 
    "知識", 
    "データ"]

#問題のランダムピックアップ
p = list(zip(questions, answers))
random.shuffle(p)
questions, answers = zip(*p)

point_add_less = allPoint/len(questions)
point_add_normal = 5

count = 0

for i in range(len(questions)):
    print("【問{}】".format(i+1))
    print("")
    print(questions[i])
    print("")
    string = input("答え：")
    print("あなたの答え：{}".format(string))
    if string == answers[i]:
        print("正解！やったね！！！！")
        if len(questions) > 20:
            result += point_add_normal
            print("+{}点加算されるよ".format(point_add_normal))
        else:
            result += point_add_less
            print("+{}点加算されるよ".format(point_add_less))
    else:
        print("残念、不正解！　答えは{}だよーん".format(answers[i]))
    print("--------------------------------------------")
    count += 1
    if count == 19:
        break

print("")
print("【結果発表】")
print("きみの最終的な得点は、、、、、{}でした".format(result))
if result < 60:
    print("ドンマイ不合格　ここから始めましょう。1から、いいえ0から")
else:
    print("合格だね　他の科目にも注力を注ごう")