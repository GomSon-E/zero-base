gearA = int(input('Gear A 톱니 수 입력 : '))
gearB = int(input('Gear B 톱니 수 입력 : '))

newGearA = gearA
newGearB = gearB

endGearA = 0
endGearB = 0

while True :
    if endGearA > 0 and endGearB > 0 :
        print('최초 만나는 톱니수(최소공백수): {}톱니'.format(endGearA))
        print('gearA 회전 수: {}회전'.format(endGearA // gearA))
        print('gearB 회전 수: {}회전'.format(endGearB // gearB))
        break
    else :
        print('gearA: {}, gearB: {}'.format(newGearA, newGearB))

        if endGearA == 0:
            newGearA += gearA
            if newGearA % gearB == 0:
                endGearA = newGearA

        if endGearB == 0:
            newGearB += gearB
            if newGearB % gearA == 0:
                endGearB = newGearB



