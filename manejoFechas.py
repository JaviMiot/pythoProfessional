from datetime import datetime

dateNow = datetime.now() #* Trae fecha y tiempo en ese momento
my_day = datetime.today() #*  Te trae la fecha de hoy
#*  te trae la fecha en URC
print(dateNow)
print(my_day)

print(f'day {my_day.day}')
print(f'month {my_day.month}')
print(f'year {my_day.year}')

print(f'hora y fecha utc {datetime.utcnow()}')

#! DAR UN FORMATO A LAS FECHAS mm/dd/yyyy dd/mm/yyyy

print(f'formato LATAM {dateNow.strftime("%d/%m/%Y")}')
print(f'formato USA {dateNow.strftime("%d/%m/%Y")}')
print(f'formato RANDOM {dateNow.strftime("%Estamos en el año %Y")}')


