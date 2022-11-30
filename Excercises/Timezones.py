from datetime import datetime as dt
import pytz

# List of timezone https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
bogota_timezone = pytz.timezone("America/Bogota")
print(bogota_timezone)
bogota_date = dt.now(bogota_timezone)
print(bogota_date)