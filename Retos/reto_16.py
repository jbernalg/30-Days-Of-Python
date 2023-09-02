'''
Crea una función que calcule y retorne cuántos días hay entre dos cadenas
de texto que representen fechas.
- Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
- La función recibirá dos String y retornará un Int.
- La diferencia en días será absoluta (no importa el orden de las fechas).
- Si una de las dos cadenas de texto no representa una fecha correcta se
lanzará una excepción.
'''
fecha1 = '01/02/2018'
fecha2 = '01/10/2020'

# funcion que determine si un año es biciesto
def esBisiesto(year:int):
    
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


# lista con los dias del año
days_year = [31,28,31,30,31,30,31,31,30,31,30,31]

# funcion que calcula los dias del año menor
def days_year_min(days_min:int, month_min:int, year:int):

    days_year = [31,28,31,30,31,30,31,31,30,31,30,31]

    if esBisiesto(year):
        days_year[1] = 29

    sum_days_year = sum(days_year)
    sum_days_month = sum(days_year[:month_min-1])        
    sum_days_total = sum_days_year - sum_days_month - days_min 
    return sum_days_total
#print(days_year_min(32,1,2021))
        
# funcion que calcula los dias del año mayor
def days_year_maj(days_maj:int, month_maj:int, year:int):

    days_year = [31,28,31,30,31,30,31,31,30,31,30,31]

    if esBisiesto(year):
        days_year[1] = 29

    sum_days_month = sum(days_year[:month_maj-1])
    sum_days_total = sum_days_month + days_maj    

    return sum_days_total
#print(days_year_maj(27,2,2023))



# funcion que calcula los dias que hay entre la diferencia
# de los años mayor y menor

# funcion que calcula la diferencia en dias entre ambas fechas

