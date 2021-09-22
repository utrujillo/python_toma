nombre = 'manuel goichi yamamoto lopez'
nombre = nombre.upper()
print('Upper: ', nombre)

nombre = nombre.capitalize()
print('Capitalize: ', nombre)

nombre = nombre.lower()
print('Lower: ', nombre)

nombre = nombre.replace('m','mm')
print('Replace: ', nombre)

size = str(len(nombre))
print('Lenght: ', size)

print('====================================')
print('Slice: ', nombre[2:5])
print('Slice: ', nombre[:5])
print('Slice: ', nombre[::-1])