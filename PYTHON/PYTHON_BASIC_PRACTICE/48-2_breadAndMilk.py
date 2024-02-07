bread = 197
milk = 152
student = 17

print('학생 한 명이 갖게 되는 빵 개수 : {}개'.format(bread // student))
print('학생 한 명이 갖게 되는 우유 개수 : {}개'.format(milk // student))

print('남는 빵 개수 : {}개'.format(bread % student))
print('남는 우유 개수 : {}개'.format(milk % student))