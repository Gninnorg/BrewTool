import machine

from config import *


def __create_flag(flag):
    with open(flag, 'w'):
        pass


def __remove_flag(flag):
    import uos

    if flag in uos.listdir():
        uos.remove(flag)


def load_configuration():
    import ujson

    with open(PATH_CONFIG, 'r') as f:
        json = f.read()
    print('File "user_settings.json" has been loaded!')
    return ujson.loads(json)


def load_calibration_params():
    import ujson

    with open(PATH_PARAMS, 'r') as f:
        json = f.read()
    reg = ujson.loads(json)
    return reg.get('a'), reg.get('b'), reg.get('c'), reg.get('unit')


def init_vpp():
    print('The VPP pin has been initialized')
    return machine.Pin(PIN_VPP, machine.Pin.OUT, value=0)


def init_mode_switch():
    print('The mode switch has been initialized')
    return machine.Pin(PIN_MODE, machine.Pin.IN, machine.Pin.PULL_UP)


def init_gy521():
    from gy521 import GY521
    # Initialize the GY521 module
    print('Initializing GY521 module')
    try:
        gy521_sensor = GY521(PIN_I2C_SDA, PIN_I2C_SCL)
    except Exception as e:
        print(e)
        gy521_sensor = None
    return gy521_sensor


def init_ds18b20():
    from tempsensor import Ds18Sensors, SingleTempSensor
    print('Initializing DS18B20 sensor')
    try:
        ow = Ds18Sensors(PIN_ONEWIRE)
        romcode_string = ow.get_device_list()[0].get('value')
        ds18_sensor = SingleTempSensor(ow, romcode_string)
    except Exception as e:
        print(e)
        ds18_sensor = None
    return ds18_sensor


def init_lipo_adc():
    from battery import Battery
    # Initialize the battery power management
    print('Initializing power management')
    lipo = Battery(PIN_BAT_ADC)
    return lipo


def init_wifi():
    from wifi import WiFi
    # Initialize Wifi
    print('Initializing WiFi')
    wlan = WiFi()
    return wlan

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('<ssid>', '<key>')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

def __init_led(pin_led, is_low_active):
    led = machine.Signal(
        machine.Pin(pin_led, machine.Pin.OUT, value=is_low_active),
        invert=True if is_low_active else False
    )
    return led


def init_led_mode():
    return __init_led(PIN_LED_MODE, PIN_LED_MODE_LOW_ACTIVE)


def init_led_grn():
    return __init_led(PIN_LED_GRN, PIN_LED_GRN_LOW_ACTIVE)


def init_led_red():
    return __init_led(PIN_LED_RED, PIN_LED_RED_LOW_ACTIVE)


def pull_hold_pins():
    """
    Set output pins to input with pull hold to save power consumption
    """
    pins_to_hold = [
        PIN_I2C_SDA,
        PIN_I2C_SCL,
        PIN_VPP,
        PIN_LED_MODE,
        PIN_LED_RED,
        PIN_LED_GRN,
    ]
    for pin in pins_to_hold:
        machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_HOLD)


def unhold_pins():
    """
    Unhold the pins after wake up from deep sleep
    """
    pins_to_unhold = [
        PIN_I2C_SDA,
        PIN_I2C_SCL,
        PIN_VPP,
        # PIN_LED_MODE,
        # PIN_LED_RED,
        # PIN_LED_GRN,
    ]
    for pin in pins_to_unhold:
        machine.Pin(pin, machine.Pin.OUT, None)


def __is_in_mode(mode_flag):
    import uos
    return mode_flag in uos.listdir()


def in_firstsleep_mode():
    return __is_in_mode(FLAG_FIRSTSLEEP)


def in_deepsleep_mode():
    return __is_in_mode(FLAG_DEEPSLEEP)


def in_ftp_mode():
    return __is_in_mode(FLAG_FTP)


def get_machine_id():
    return int.from_bytes(machine.unique_id(), 'big')
