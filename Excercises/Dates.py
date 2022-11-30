from datetime import datetime as dt

#strftime -> string format time
my_time = dt.utcnow()
latam = my_time.strftime('%d/%m/%Y')
random = my_time.strftime(f'We are in year %Y')
print(f'Formato LATAM: {latam}')
print(random)
print(my_time.strftime('%I:%M %p'))