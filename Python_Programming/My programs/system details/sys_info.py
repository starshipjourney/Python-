#!/usr/bin/env python3
import platform
import getpass
import psutil
import GPUtil
import cpuinfo
import socket

#----------OS LEVEL DETAILS----------------------------------
print("\n",f"OS : {platform.system()}")
print(f"Version : {platform.platform()}")
print(f"Current User : {getpass.getuser()}","\n")

#----------HARDWARE DETAILS----------------------------------
disk = psutil.disk_usage("/")
print(f"Total Storage: {round((disk.total / (1024**3)),2)}  GB","\t",f"Storage Used: {round((disk.used / (1024**3)),2)} GB","\t",f"Storage Free: {round((disk.free / (1024**3)),2)} GB")
print(f"Processor: {cpuinfo.get_cpu_info()['brand_raw']}")
print(f"Number of Phisical cores: {psutil.cpu_count(logical=False)}")
print(f"Ram : total {round((psutil.virtual_memory().total)/(1024**3), 2)}GB","\t",f"free {round((psutil.virtual_memory().free)/(1024**3), 2)}GB","\t",f"used {round((psutil.virtual_memory().used)/(1024**3), 2)} GB")
print(f"GPU : {GPUtil.getGPUs()}","\n") #.name .memoryTotal for name and memory details

#----------HARDWARE TEMPRATURE DETAILS------------------------
cpu_temp = psutil.sensors_temperatures(fahrenheit=False)
for i in cpu_temp['coretemp']:
    if "Package" in i[0]:
        continue 
    print(f"CPU core temprature: {i}")
print(f"GPU temprature : {GPUtil.getGPUs()}","\n") #.temprature


#----------NETWORK DETAILS------------------------------------
print(f"Host name : {socket.gethostname()}")
print(f"IP Address : {socket.gethostbyname(socket.gethostname())}","\n")

