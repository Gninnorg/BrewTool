# This file contains hardware configurations. e.g. Pin assignments
from micropython import const


PIN_I2C_SDA = const(21)
PIN_I2C_SCL = const(22)

PIN_BAT_ADC = const(35)  # for measuring battery voltage
BAT_VOL_THD = 3.66       # threshold for battery health check

PIN_ONEWIRE = const(16)  # data line of DS18B20 temp sensor
PIN_DS18_PW = const(17)  # pin for controlling power to DS18B20 temp sensor
PIN_ENA_FTP = const(18)  # pin for controlling start of FTP server

PIN_MPU6_PW = const(23)  # pin for controlling power to MPU6005 gyro

PATH_CONFIG = 'config.json'  # configuration file with user settings
PATH_PARAMS = 'params.json'  # file with params used for calibration of device


