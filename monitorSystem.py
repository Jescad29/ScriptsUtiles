import psutil
import time

def monitor_system(thresholds):
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    
    if cpu > thresholds['cpu']:
        print(f"Alerta: Uso de CPU alto - {cpu}%")
    if memory > thresholds['memory']:
        print(f"Alerta: Uso de Memoria alto - {memory}%")
    if disk > thresholds['disk']:
        print(f"Alerta: Uso de Disco alto - {disk}%")
    
    time.sleep(5)
    
sytemData = {
    'cpu': 80,
    'memory': 80,
    'disk': 90
    }

monitor_system(sytemData)