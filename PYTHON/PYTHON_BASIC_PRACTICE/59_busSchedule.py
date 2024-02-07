for i in range(0, 17 * 60) :
    if i % 15 == 0 and i % 13 == 0:
        print('busA와 busB 동시 정차!! {}:{}'.format(i // 60 + 6, i % 60))
    if 20 <= i < 16 * 60 :
        if i % 15 == 0 and i % 8 == 0 :
            print('busA와 busC 동시 정차!! {}:{}'.format(i // 60 + 6, i % 60))
        elif i % 13 == 0 and i % 8 == 0 :
            print('busB와 busC 동시 정차!! {}:{}'.format(i // 60 + 6, i % 60))