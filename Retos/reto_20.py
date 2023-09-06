'''
Crea una función que reciba días, horas, minutos y segundos (como enteros) y retorne 
su resultado en milisegundos.
- Recordemos que 1 segundo contiene 1000 milisegundos
'''

def convert_miliseconds(days:int, hours:int, minutes:int, seconds:int):

    # validar entrada
    if days >= 0 and hours >= 0 and minutes >= 0 and seconds >= 0:

        # de minutos a segundos
        seg_min = minutes * 60

        # de horas a segundos
        seg_hour = hours * 60 * 60

        # dias a segundos
        seg_days = days * 24 * 60 * 60

        # total en segundos
        total_seg = seconds + seg_min + seg_hour + seg_days

        # total en minisegundos
        total_miliseg = total_seg * 1000

        return total_miliseg
    
    else:
        return None
    
print(convert_miliseconds(0,0,1,1)) # --> 61000
print(convert_miliseconds(5,10,2,10)) # --> 468130000
print(convert_miliseconds(20, 50, 90, 500)) # --> 1913900000
print(convert_miliseconds(1, -2, 1, 10)) # --> None  