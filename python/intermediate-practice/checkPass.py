def check(s1, s2, s3, s4, s5):

    averageLimit = 60; scoreLimit = 40

    def getTotal():
        total = s1 + s2 + s3 + s4 + s5
        print(f'총점: {total}')
        return total

    def getAverage():
        average = getTotal() / 5
        print(f'평균: {average}')
        return average

    def checkScorePass():
        print(f'{s1}: {'Pass' if s1 >= scoreLimit else 'Fail'}')
        print(f'{s2}: {'Pass' if s2 >= scoreLimit else 'Fail'}')
        print(f'{s3}: {'Pass' if s3 >= scoreLimit else 'Fail'}')
        print(f'{s4}: {'Pass' if s4 >= scoreLimit else 'Fail'}')
        print(f'{s5}: {'Pass' if s5 >= scoreLimit else 'Fail'}')

    def checkAveragePass():
        if getAverage() >= averageLimit:
            if s1 >= scoreLimit and s2 >= scoreLimit and s3 >= scoreLimit and s4 >= scoreLimit and s5 >= scoreLimit:
                print('Final Pass!!')
            else:
                print('Final Fail!!')
        else:
            print('Final Fail!!')

    getAverage()
    checkScorePass()
    checkAveragePass()


