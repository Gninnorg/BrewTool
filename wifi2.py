def load_configuration(config_file):
    import ujson
    with open(config_file, 'r') as f:
        json = f.read()
    print('File ' + config_file +' has been loaded!')
    return ujson.loads(json)

def wifi():
    import network
        
    # Network settings
    settings = load_configuration('wifi.json')

    # Create a station object to store our connection
    wlan = network.WLAN(network.STA_IF)
    
    print("wait wlan")
    while not wlan.active(True):
        pass
    
    print("Connecting: " + settings['wifi']['ssid'])
    wlan.connect(settings['wifi']['ssid'], settings['wifi']['pass'])

    # Continually try to connect to WiFi access point
    while not wlan.isconnected():
        pass        
 
    print("Connected!")
    print("My IP Address:", wlan.ifconfig()[0])

wifi()
import uftpd

