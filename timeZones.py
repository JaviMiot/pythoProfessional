from datetime import datetime
import pytz
#! Trabajando con zonas horarias paar eso se instala el modulo pytz.

newYork_timezone = pytz.timezone('America/New_York')
newYork_date = datetime.now(newYork_timezone)
print(newYork_date.strftime('%d/%m/%Y %H:%M:%S'))

