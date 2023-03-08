def student_score(score):
    i = 0
    while i < len(score):
        BonusRules = 5-(score[i]%5)
        if BonusRules < 3 and score[i]+BonusRules >= 40:
            score[i] += BonusRules
        i += 1
    print('德瑞克 ' + str(score[0]))
    print('尚恩 ' + str(score[1]))
    print('傑夫 ' + str(score[2]))
    print('馬基 ' + str(score[3]))

'''依序輸入學生成績:德瑞克、尚恩、傑夫、馬基'''

AllScore = [33, 73, 63, 39]
student_score(AllScore)
