'''
Cual es la diferencia porcentual entre el curso actual y:
a.- el mas rapido de otros cursos
b.- el mas lento de otros cursos
c.- el promedio de los cursos
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

# diferencia porcentual entre el curso actual y el mas rapido de otros cursos
diferencia_con_min = 100 - (curso_actual/otros_cursos_min) * 100

# diferencia porcentual entre el curso actual y el mas lento de otros cursos
diferencia_con_max = 100 - (curso_actual/otros_cursos_max) * 100

# diferencia porcentual entre el curso actual y el promedio de otros cursos
diferencia_con_prom = 100 - (curso_actual/otros_cursos_promedio) * 100

print(f'El curso actual dura {diferencia_con_min}% menos que el mas rapido de otros cursos')
print(f'El curso actual dura {diferencia_con_max:.1f}% menos que el mas lento de otros cursos')
print(f'El curso actual dura {diferencia_con_prom}% menos que el promedio de otros cursos')

# operando los decimales directamente desde la operacion aritmetica
# resultado con un decimal
diferencia_con_max1 = 100 - curso_actual*1000//otros_cursos_max/10
print(f'El curso actual dura {diferencia_con_max1}% menos que el mas lento de otros cursos')

# resultado con dos decimales
diferencia_con_max2 = 100 - curso_actual*10000//otros_cursos_max/100
print(f'El curso actual dura {diferencia_con_max2}% menos que el mas lento de otros cursos')
