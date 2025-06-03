# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# datetime.fromtimestamp(UNIX Timestamp)

# Timezones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime
# from pytz import timezone

# data_str_data = '2025/04/16 15:02:33'
# data_str_data = '16/04/2025'
# data_str_fmt = '%d/%m/%Y'

# data = datetime(2025, 4, 16, 15, 2, 33)
# data = datetime.strptime(data_str_data, data_str_fmt)

# data = datetime.now(timezone('America/Sao_Paulo'))

data = datetime.now()
print(data.timestamp())
print(datetime.fromtimestamp(1744828354.201516))
