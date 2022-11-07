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