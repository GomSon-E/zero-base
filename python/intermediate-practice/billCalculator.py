income = 0 ; waterBill = 0 ; electronicBill = 0 ; gasBill = 0

def setIncome(i):
    global income
    income = i

def getIncome():
    return income
def setWaterBill(wb):
    global waterBill
    waterBill = wb

def getWaterBill():
    return waterBill

def setElectronicBill(eb):
    global electronicBill
    electronicBill = eb

def getElectronicBill():
    return electronicBill

def setGasBill(gb):
    global gasBill
    gasBill = gb

def getGasBill():
    return gasBill

def getTotalBill():
    return getWaterBill() + getElectronicBill() + getGasBill()

def getBillRate():
    return round(getTotalBill() / getIncome() * 100, 2)
