'''
a.- Cual es la diferencia porcentual entre el curso actual y:
- el mas rapido de otros cursos
- el mas lento de otros cursos
- el promedio de los cursos

b.-Porcentaje de material inservible que se reduce en
- El promedio de los cursos
- El curso actual

c.- Ver 10 horas del curso actual equivale a cuantas horas de otros cursos?
y al reves?

Datos:
Tiempo curso actual = 1.5h
Tiempo minimo otros cursos = 2.5h
Tiempo promedio otros cursos = 4h
Tiempo maximo otros cursos = 7h
Tiempo promedio crudo otros cursos = 5h
Tiempo promedio crudo curso actual 3.5h
'''

# promedios de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
curso_actual = 1.5

#----------------------- SOLUCION A --------------------------------------
print('-----------------------------------------------')
# diferencia porcentual entre el curso actual y el mas rapido de otros cursos
diferencia_con_min = 100 - (curso_actual/otros_cursos_min) * 100

# diferencia porcentual entre el curso actual y el mas lento de otros cursos
diferencia_con_max = 100 - (curso_actual/otros_cursos_max) * 100

# diferencia porcentual entre el curso actual y el promedio de otros cursos
diferencia_con_prom = 100 - (curso_actual/otros_cursos_promedio) * 100

print(f'El curso actual dura {diferencia_con_min}% menos que el mas rapido de otros cursos')
print(f'El curso actual dura {diferencia_con_max:.1f}% menos que el mas lento de otros cursos')
print(f'El curso actual dura {diferencia_con_prom}% menos que el promedio de otros cursos')


'''
# operando los decimales directamente desde la operacion aritmetica
# resultado con un decimal
diferencia_con_max1 = 100 - curso_actual*1000//otros_cursos_max/10
print(f'El curso actual dura {diferencia_con_max1}% menos que el mas lento de otros cursos')

# resultado con dos decimales
diferencia_con_max2 = 100 - curso_actual*10000//otros_cursos_max/100
print(f'El curso actual dura {diferencia_con_max2}% menos que el mas lento de otros cursos')
'''

#------------------------- SOLUCION B ------------------------------
print('-----------------------------------------------')
# duracion de crudos
crudo_promedio = 5
crudo_curso_actual = 3.5

# porcentaje de tiempo vacio eliminado por otros cursos
tiempo_vacio_prom = 100 - otros_cursos_promedio * 1000//crudo_promedio/10

# porcentaje de tiempo vacio eliminado por el curso actual
tiempo_vacio_actual = 100 - curso_actual * 1000//crudo_curso_actual/10

print(f'Un curso promedio elimina un {tiempo_vacio_prom}% de tiempo vacio')
print(f'El curso actual elimina hasta un {tiempo_vacio_actual}% de tiempo vacio')

#-------------------------- SOLUCION C -------------------------------
print('-----------------------------------------------')
# mostrar diferencias si el curso actual durara 10 horas
print(f'Ver 10 horas del curso actual equivale a {otros_cursos_promedio/curso_actual * 10:.1f} horas de otros cursos')

# mostrar diferencias si los otros cursos duraran 10 horas
print(f'Ver 10 horas de otros cursos equivale a {curso_actual/otros_cursos_promedio * 10:.1f} horas del curso actual')