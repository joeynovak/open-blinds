# Complete project details at https://RandomNerdTutorials.com
try:
    import usocket as socket
except:
    import socket
    
import ujson

from machine import Pin
import network
import esp
import WebServerRouter
import WebServerRequest
        
class WebServer:
    
    
    def __init__(self):
        
        esp.osdebug(None)            

        with open('wifi.json', 'r') as fp:
            wifiSettings = ujson.load(fp)

        station = network.WLAN(network.STA_IF)

        station.active(True)
        
        print("Connecting to network...")
        station.connect(wifiSettings['ssid'], wifiSettings['password'])


        while station.isconnected() == False:
          pass

        print('Connection successful')
        print(station.ifconfig())

        self.router = WebServerRouter.WebServerRouter()
        
    def serve(self, blinds):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', 80))
        s.listen(5)

        while True:
            conn, addr = s.accept()
            print('Got a connection from %s' % str(addr))
            webRequest = WebServerRequest.WebServerRequest()        
            request = conn.recv(2048)
            while(request):                        
                webRequest.appendRequestData(request)
                if webRequest.endReached():
                    break
            
            #Let's clear the memory used by the request...
            request = ''
            print('Content = %s' % request)
            blinds_open = request.find('/?blinds=open')
            blinds_closed = request.find('/?blinds=closed')

            response = self.router.getResponse(webRequest)
            
            conn.send('HTTP/1.1 ' + str(response.responseCode) + ' OK\n')
            conn.send('Content-Type: ' + response.responseType + '\n')
            conn.send('Connection: close\n\n')
            conn.sendall(response.responseBody)
            conn.close()
            
            if blinds_open == 6:
                print('Blinds Opening')
                blinds.open()
            if blinds_closed == 6:
                print('Blinds Closing')
                blinds.close()
                