# Connect wifi and start ftp server for development purposes
print("------------------------------------")
print("Connect to wifi and setup ftp server")
from wlan import NetworkHandler
wireless = NetworkHandler("brewtool")
wireless.connect_wifi()
import uftpd
print("------------------------------------")
print("")
# Code starts here

import machine, onewire, ds18x20, time

ds_pin = machine.Pin(16)
ds_pow = machine.Pin(17, machine.Pin.OUT)
ds_pow.value(1)

ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
print('Found DS devices: ', roms)

while True:
  ds_sensor.convert_temp()
  time.sleep_ms(750)
  print(ds_sensor.read_temp(roms[0]))
  time.sleep(5)