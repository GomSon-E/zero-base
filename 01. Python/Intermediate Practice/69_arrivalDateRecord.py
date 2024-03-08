from datetime import datetime, timedelta

firstDay = datetime(2021, 1, 1)
lastDay = datetime(2021, 12, 31)

period = (lastDay - firstDay).days

for i in range(period + 1):
    if i % 3 == 0 and i % 4 == 0 and i % 5 == 0:
        with open('files/arrivalDateRecord.txt', 'a', encoding='utf-8') as f:
            day = firstDay + timedelta(days=i)
            f.write(f'{day.strftime('%Y-%m-%d')} 10:00:00\n')