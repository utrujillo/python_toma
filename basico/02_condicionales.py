# Preguntar primero por la nacionalidad
# - MX (mayoria de edad es de 18)
# - EU (mayoria de edad es de 20)
# Determinar si la persona es mayor o menor de edad

edad = int( input('Escribe tu edad: ') )
if edad > 18:
  print('Eres mayor de edad')
elif edad == 18:
  print('Estas en el rango de la mayoria de edad')
else:
  print('No eres mayor de edad')