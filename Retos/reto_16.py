'''
Crea una función que calcule y retorne cuántos días hay entre dos cadenas
de texto que representen fechas.
- Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
- La función recibirá dos String y retornará un Int.
- La diferencia en días será absoluta (no importa el orden de las fechas).
- Si una de las dos cadenas de texto no representa una fecha correcta se
lanzará una excepción.
'''

# funcion que determine si un año es biciesto
def esBisiesto(year:int):
    
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0 or year % 100 == 0:
        return True
    else:
        return False
#print(esBisiesto(1993))

# funcion que calcula los dias del año menor
def days_year_min(days_min:int, month_min:int, year:int):

    days_year = [31,28,31,30,31,30,31,31,30,31,30,31]

    if esBisiesto(year):
        days_year[1] = 29

    sum_days_year = sum(days_year)
    sum_days_month = sum(days_year[:month_min-1])        
    sum_days_total = sum_days_year - sum_days_month - days_min 
    return sum_days_total
#print(days_year_min(1,1,1900))
        
# funcion que calcula los dias del año mayor
def days_year_maj(days_maj:int, month_maj:int, year:int):

    days_year = [31,28,31,30,31,30,31,31,30,31,30,31]

    if esBisiesto(year):
        days_year[1] = 29

    sum_days_month = sum(days_year[:month_maj-1])
    sum_days_total = sum_days_month + days_maj    

    return sum_days_total
#print(days_year_maj(18,4,2022))

# validacion de fechas
def validate_num_date(int_day, int_month, int_year):

    days_year = [31,28,31,30,31,30,31,31,30,31,30,31]

    # validar año
    if int_year < 0:
        return False
    # validar moth
    elif int_month > len(days_year):
        return False
    # validar days
    elif int_day > days_year[int_month-1]:
        return False
    else:
        return int_day, int_month, int_year
#print(validate_date(3,12,-1))

# funcion que determina la fecha menor y mayor
def date_min_maj(day1, month1,year1,day2,month2,year2):
    
    if year1 > year2:
        band = year1
        year1 = year2
        year2 = band

        band = month2
        month1 = month2
        month2 = band

        band = day1
        day1 = day2
        day2 = band

    return day1, month1, year1, day2, month2, year2
#print(date_min_maj(2,2,2022,1,1,2020))

# funcion que valida el formato y valor de fecha
def validate_date(fecha):
    
    list_fecha = fecha.split('/')  

    if len(list_fecha) == 3: 
        int_month = int(list_fecha[1])
        int_day = int(list_fecha[0])
        int_year = int(list_fecha[2])

        if validate_num_date(int_day, int_month, int_year) == False:
            return False
        else:
            val_day, val_month, val_year = validate_num_date(int_day, int_month, int_year)
            return val_day, val_month, val_year
    else:
        return False
#fecha = '01/02/2023'
#print(f'Validacion hecha: {validate_date(fecha)}')

# funcion que cuenta los dias que hay entre la diferencia de años
def days_year_difference(year1:int, year2:int):

    year_min = year1
    year_max = year2

    if year_max - year_min == 0 or year_max - year_min == 1:
        return 0
    else:
        sum_days = 0
        for i in range(year_min + 1,year_max):
            
            if esBisiesto(i):
                days_year = 366
                sum_days += days_year
            else:
                days_year = 365
                sum_days += days_year

    return sum_days
#print(days_year_difference(2019, 2021))           

# funcion que suma todos los dias
def sum_days_total(sum_year_maj, sum_year_min, sum_dif_years):
    return sum_year_maj + sum_dif_years + sum_year_min

############################################################

fecha1 = '1/1/1'
fecha2 = '18/04/2022'

if validate_date(fecha1) == False:
    print('Primera fecha erronea. Corrija y vuelva a introducir')
else:
    day1, month1, year1 = validate_date(fecha1)

if validate_date(fecha2) == False:
    print('Segunda fecha erronea. Corrija y vuelva a introducir')
else:
    day2, month2, year2 = validate_date(fecha2)

day1, month1, year1, day2, month2, year2 = date_min_maj(day1,month1,year1,day2,month2,year2)

if year2 - year1 != 0:
    sum_days_year_min = days_year_min(day1,month1,year1)
    sum_days_year_max = days_year_maj(day2,month2,year2)
    sum_days_year = days_year_difference(year1,year2)
    total_days = sum_days_total(sum_days_year_min, sum_days_year_max, sum_days_year)
else:
    sum_days_year1 = days_year_maj(day1,month1,year1)
    sum_days_year2 = days_year_maj(day2,month2,year2)
    total_days = abs(sum_days_year2 - sum_days_year1)
    
print(total_days)