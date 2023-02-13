hrs = int(input('Dame las horas: '))
mi = int(input('Dame los minutos: '))
dur = int(input('Dame la duracion: '))

mi += dur
hrs = hrs + (mi // 60) 
mi = mi % 60
while hrs > 24:
    hrs -= 24

print('Finaliza a las ', hrs,':',mi)
