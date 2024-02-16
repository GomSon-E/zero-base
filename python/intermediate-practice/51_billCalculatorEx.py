import billCalculator as b

income = int(input('수입 입력: '))
waterBill = int(input('수도요금 입력: '))
electronicBill = int(input('전기요금 입력: '))
gasBill = int(input('가스요금 입력: '))

b.setIncome(income)
b.setWaterBill(waterBill)
b.setElectronicBill(electronicBill)
b.setGasBill(gasBill)

print(f'공과금: {format(b.getTotalBill(), ',')}원')
print(f'공과금 비율: {b.getBillRate()}%')