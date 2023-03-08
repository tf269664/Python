def ball_height(height, time):
    i = 1
    total = height
    while i <= time:
        height = height/2
        if i != time:
            total += height*2
        i += 1
    print('總共:' + str(total))
    print('第' + str(time) + '次:' + str(height))

'''輸入初始高度和落地次數'''

BallHeight = 100
DropTime = 10

ball_height(BallHeight, DropTime)
