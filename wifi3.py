import network
import time
from ujson import loads

class NetworkHandler():
    #class handling network connections

    def __init__(self, hostname, file: str = "network.config"):
        #initialize network handler
        self.file = file
        self.hostname = hostname
        self.config = {}
        
        with open(file, 'r') as f:
            config = f.read()
            
        self.config = loads(config)
        
    def connect_wifi(self):
        """Connect to WIFI - 
           Sleep time inserted to handled bug which causes as dump,
           when hostname is set """
        
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        
        #Wait some time to wlan.active to settle, before setting hostname
        time.sleep(2)
        wlan.config(dhcp_hostname=self.hostname)

        wlan.connect(self.config['SSID'], self.config['PSK'])

        while not wlan.isconnected():
            pass

if __name__ == '__main__':
    network_handler = NetworkHandler("brewtool","config.json")
    network_handler.connect_wifi()
    import uftpd
    
