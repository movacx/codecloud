#Promedio de duraciòn
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#Diferencias de duraciòn

diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

print(f'El curso  dura un {diferencia_con_min}% menos que el màs rapido')
print(f'El curso  dura un {diferencia_con_max}% menos que el màs lento')
print(f'El curso  dura un {diferencia_con_promedio}% menos que el promedio')