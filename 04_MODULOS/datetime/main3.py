# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')

from datetime import datetime

fmt = '%d/%m/%Y'

# data = datetime(2025, 4, 18, 14, 20, 52)

# 1º criar a data -> strptime
data = datetime.strptime('2025-04-18 14:20:52', '%Y-%m-%d %H:%M:%S')
print(data)
print()

# 2º formatar -> strftime
print(data.strftime(fmt))
print()
print(data.strftime('%d/%m/%Y %H:%M'))
print()

# Pegar valor real e não a string 
print(data.strftime('%Y'), data.year)
