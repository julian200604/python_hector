'''temperature = 20

if temperature > 35:
    print('Aviso por alta temperatura')

else : 
    print('Aviso por baja temperatura')'''



'''temperature = 50

if temperature < 20:
    if temperature < 10:
        print('Nivel azul')
    else:
        print('Nivel verde')
else:
    if temperature < 30:
        print('Nivel naranja')
    else:
        print('Nivel rojo')'''



'''temperature = 60

if temperature < 20:
    if temperature < 10:
        print('Nivel azul')
    else:
        print('Nivel verde')
elif temperature < 30:
    print('Nivel naranja')
else:
    print('Nivel rojo')'''

#declrando variables en condicionales de forma larga

'''temperature = 35

if temperature < 30:
    fire_risk = 'LOW'
else:
    fire_risk = 'HIGH'''


#declrando variables en condicionales de forma corta

'''temperature = 60

fire_risk = 'LOW' if temperature < 30 else 'HIGH'

fire_risk

print(fire_risk)'''


'''power = 10
signal_4g = 60

power > 25 and signal_4g > 10

print(power)'''

#sentencia match-case

'''color = '#00FF00'

match color:
    case '#FF0000':
        print('🔴')
    case '#00FF00':
        print('🟢')
    case '#0000FF':
        print('🔵')'''

#patrones avanzados


'''point = (2, 5, 7)

match point:
    case (x, y):
        print(f'({x},{y}) is in plane')
    case (x, y, z):
        print(f'({x},{y},{z}) is in space')'''

#Operador morsa

radius = 5
'''perimeter = 2 * 3.14 * radius
if perimeter < 100:
    print('Increase radius to reach minimum perimeter')
    print('Actual perimeter: ', perimeter)'''

#con operador morsa


if (perimeter := 2 * 3.14 * radius) < 100:
    print('Increase radius to reach minimum perimeter')
    print('Actual perimeter: ', perimeter)
