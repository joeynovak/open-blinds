import Stepper
import Blinds
import WebServer

from machine import Pin
'''
IN1 -->  16
IN2 -->  17
IN3 -->  5
IN4 -->  18
'''

stepper = Stepper.create(Pin(5,Pin.OUT),Pin(4,Pin.OUT),Pin(0,Pin.OUT),Pin(2,Pin.OUT), delay=1)

blinds = Blinds.Blinds(stepper, 5)

print('Opening Blinds A Bit')
blinds.openABit()

print('Closing Blinds A Bit')
blinds.closeABit()

print('Initing Webserver')
webServer = WebServer.WebServer()

print('Serving Webpage')
webServer.serve(blinds)

