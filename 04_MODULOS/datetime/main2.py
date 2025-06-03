#datetime.timedelta e dateutil.relativetimedelta (calculando datas)

# pip install python-dateutil types-python-dateutil

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('18/01/1994 02:10:00', fmt)
data_fim = datetime.strptime('17/04/2025 15:30:20', fmt)

print(data_fim > data_inicio)
print(data_fim < data_inicio)
print(data_fim == data_inicio)
print()

print(data_fim - data_inicio)
print()


delta = data_fim - data_inicio
print(delta.days, delta.seconds)
print(delta.total_seconds())


# delta2 = timedelta(days=10, hours=2)
# print(data_fim + delta2)

delta2 = relativedelta(data_fim, data_inicio)
print(delta2)
print(delta2.years, delta2.days)

print(data_fim + relativedelta(seconds=59, minutes=15))
