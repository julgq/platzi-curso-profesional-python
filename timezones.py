from datetime import datetime
import pytz

mexico_timezone = pytz.timezone("America/Mexico_City")
mexico_date =  datetime.now(mexico_timezone)
print("México: ", mexico_date.strftime("%d/%m/%y, %H:%M:%S"))
