# Usando calendar para calendários e datas
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar você pode saber coisas como:
#   Qual o último dia do mês (ex.: monthrange)
#   Qual o nome e número do dias de determinada data (ex.: weekday)
#   Criar um calendário em si (ex.: monthcalendar)
#   Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão, dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo

import calendar

print(calendar.calendar(2025))
print()

print(calendar.month(2077, 1))
print()

print(calendar.monthrange(2025, 11)) # ultimo dia do mês
print()

print(list(enumerate(calendar.day_name)))
print()


numero_primeiro_dia, ultimo_dia = calendar.monthrange(2025, 11)
print(calendar.day_name[numero_primeiro_dia])
print()

print(calendar.weekday(2025, 11, ultimo_dia))
print()

print(calendar.monthcalendar(2025, 8))
print()

# for week in calendar.monthcalendar(2025, 8):
#     print(list(enumerate(week)))

for week in calendar.monthcalendar(2025, 8):
    for day in week:
        if day == 0:
            continue
        print(day)
