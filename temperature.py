# https://randomnerdtutorials.com/micropython-ds18b20-esp32-esp8266/

from config import PIN_DS18_PW, PIN_ONEWIRE
from machine import Pin
from onewire import OnWire
from ds18x20 import DS18X20
from time import sleep_ms

def get_wort_temperature():
  # Turn on power to DS18
  ds_pow = Pin(PIN_DS18_PW)
  ds_pow.value(1)
  
  # Open DS18
  ds_pin = Pin(PIN_ONEWIRE)
  ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
  roms = ds_sensor.scan()
  ds_sensor.convert_temp()
  sleep_ms(750)

  # Read temperature
  for rom in roms:
    temp = ds_sensor.read_temp(rom)
    print(rom)
    print(temp)

  return temp
