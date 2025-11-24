import os

shutdown = input('Quieres apagar el equipo? (s/n): ')

if shutdown.lower() == 's':
    os.system('shutdown /s /t 1')   
    print('El equipo se apagará en breve.')
else:
    print('Operación cancelada.')       
    exit()