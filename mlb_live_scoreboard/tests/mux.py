#from LED import gpio_runner
import RPi.GPIO as GPIO
from time import sleep

mux_pins = [7,20,16,12]
mux_vals = {-1:[0,0,0,0],
            0:[1,0,0,0],
            1:[1,0,0,1],
            2:[1,0,1,0],
            3:[1,0,1,1],
            4:[1,1,0,0],
            5:[1,1,0,1],
            6:[1,1,1,0],
            7:[1,1,1,1]}

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(mux_pins,GPIO.OUT)
def mux_run():
    for x in range(8):
        print(f'{x}:{mux_vals[x]}')
        GPIO.output(mux_pins,mux_vals[x])
        sleep(3)
    GPIO.output(mux_pins,mux_vals[-1])
    
def mux_set(number: int):
    GPIO.output(mux_pins,mux_vals[number])
    
if __name__=="__main__":
    setup()
    mux_run()