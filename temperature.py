# https://randomnerdtutorials.com/micropython-ds18b20-esp32-esp8266/

from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20
from time import sleep_ms

def get_wort_temperature(probe):
  
  # Open DS18
  ds_pin = Pin(probe)
  ds_sensor = DS18X20(OneWire(ds_pin))
  roms = ds_sensor.scan()
  ds_sensor.convert_temp()
  sleep_ms(750)

  # Read temperature
  temp = 0
  for rom in roms:
    temp = ds_sensor.read_temp(rom)
    temp = ds_sensor.read_temp(rom)

    print(rom)
    print(temp)

  ds_pin.value(0)

  return temp
