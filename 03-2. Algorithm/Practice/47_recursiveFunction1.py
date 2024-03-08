def recursiveFuction(data):

    if len(data) < 2:
        return data

    print(f'sales: {data}')

    change = (data.pop(0) - data[0]) * -1

    if change > 0:
        print(f'매출증감액: +{change}')
    else:
        print(f'매출증감액: {change}')

    recursiveFuction(data)


sales = [12000, 13000, 12500, 11000, 10500, 98000, 91000, 91500, 10500, 11500, 12000, 12500]
recursiveFuction(sales)