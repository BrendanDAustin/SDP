import RPi.GPIO as GPIO
from numpy import array
from LED.pin_map import gpio_map
from LED.values_matrix import Matrix
from time import sleep
matrix = Matrix()
gpio_addresses = gpio_map()
GPIO.setmode(GPIO.BCM)
pin_addresses = gpio_addresses.pin_set
print(f'Pin addresses: {pin_addresses}')
#GPIO.setup(pin_addresses,GPIO.OUT)
for pin in pin_addresses:
    print(pin)
    GPIO.setup(pin,GPIO.OUT)
def run_dummy(time_sleep):
    while True:
        for i in matrix.values:
            matrix.lock.acquire()
            print(i)
            matrix.lock.release()
            sleep(time_sleep)

def run():
    while True:
        for i in matrix.values:
            matrix.lock.acquire()
            addr = list(pin_addresses)
            vals = tuple([int(j) for j in i])
            #print(list(pin_addresses),tuple(i))
            GPIO.output(addr,vals)
            sleep(0.25)
            matrix.lock.release()


