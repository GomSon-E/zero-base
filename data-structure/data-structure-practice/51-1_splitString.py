aboutPython = '파이썬은 1991년 프로그래머인 귀도 반 로섬이 발표한 고급 프로그래밍 언어이다.'

aboutPythonList = aboutPython.split(' ')
print(aboutPythonList)

aboutPythonDic = {}
for i in range(len(aboutPythonList)):
    aboutPythonDic[i] = aboutPythonList[i]
print(aboutPythonDic)
