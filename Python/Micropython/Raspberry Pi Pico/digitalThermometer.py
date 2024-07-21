#code by Matheus Oliveira - 2014
#dallas and oneWire references from: https://randomnerdtutorials.com/raspberry-pi-pico-ds18b20-micropython/
#Uses RP Pico and two IC4511 for two 7seg displays

from machine import Pin
from time import sleep
import onewire, ds18x20

d0a = Pin(13, Pin.OUT)
d1a = Pin(15, Pin.OUT)
d2a = Pin(14, Pin.OUT)
d3a = Pin(12, Pin.OUT)

d0b = Pin(16, Pin.OUT)
d1b = Pin(11, Pin.OUT)
d2b = Pin(10, Pin.OUT)
d3b = Pin(17, Pin.OUT)

def show_display1(num):
    if num == 0:
        d0a.value(0)
        d1a.value(0)
        d2a.value(0)
        d3a.value(0)
        
    if num == 1:
        d0a.value(1)
        d1a.value(0)
        d2a.value(0)
        d3a.value(0)
        
    if num == 2:
        d0a.value(0)
        d1a.value(1)
        d2a.value(0)
        d3a.value(0)
    
    if num == 3:
        d0a.value(1)
        d1a.value(1)
        d2a.value(0)
        d3a.value(0)
        
    if num == 4:
        d0a.value(0)
        d1a.value(0)
        d2a.value(1)
        d3a.value(0)
        
    if num == 5:
        d0a.value(1)
        d1a.value(0)
        d2a.value(1)
        d3a.value(0)
        
    if num == 6:
        d0a.value(0)
        d1a.value(1)
        d2a.value(1)
        d3a.value(0)
        
    if num == 7:
        d0a.value(1)
        d1a.value(1)
        d2a.value(1)
        d3a.value(0)
    
    if num == 8:
        d0a.value(0)
        d1a.value(0)
        d2a.value(0)
        d3a.value(1)
        
    if num == 9:
        d0a.value(1)
        d1a.value(0)
        d2a.value(0)
        d3a.value(1)
        
def show_display2(num):
    if num == 0:
        d0b.value(0)
        d1b.value(0)
        d2b.value(0)
        d3b.value(0)
        
    if num == 1:
        d0b.value(1)
        d1b.value(0)
        d2b.value(0)
        d3b.value(0)
        
    if num == 2:
        d0b.value(0)
        d1b.value(1)
        d2b.value(0)
        d3b.value(0)
    
    if num == 3:
        d0b.value(1)
        d1b.value(1)
        d2b.value(0)
        d3b.value(0)
        
    if num == 4:
        d0b.value(0)
        d1b.value(0)
        d2b.value(1)
        d3b.value(0)
        
    if num == 5:
        d0b.value(1)
        d1b.value(0)
        d2b.value(1)
        d3b.value(0)
        
    if num == 6:
        d0b.value(0)
        d1b.value(1)
        d2b.value(1)
        d3b.value(0)
        
    if num == 7:
        d0b.value(1)
        d1b.value(1)
        d2b.value(1)
        d3b.value(0)
    
    if num == 8:
        d0b.value(0)
        d1b.value(0)
        d2b.value(0)
        d3b.value(1)
        
    if num == 9:
        d0b.value(1)
        d1b.value(0)
        d2b.value(0)
        d3b.value(1)
        
ds_pin = machine.Pin(18)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
print('Found DS devices: ', roms)

while True:
  ds_sensor.convert_temp()
  sleep(1)
  for rom in roms:
    print(rom)
    tempC = ds_sensor.read_temp(rom)
    tempC = str(tempC)
    print('temperature (ºC):'+ tempC)
    show_display1(int(tempC[0]))
    show_display2(int(tempC[1]))
    
time.sleep(5)


