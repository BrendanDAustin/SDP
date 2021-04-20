#from LED import gpio_runner
from datetime import datetime, timedelta
from threading import Thread
from time import sleep
#matrix = gpio_runner.matrix
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

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
vals = {-1:[0,0,0,0,0],
        0:[1,0,0,0,0],
        1:[1,0,0,0,1],
        2:[1,0,0,1,0],
        3:[1,0,0,1,1],
        4:[1,0,1,0,0],
        5:[1,0,1,0,1],
        6:[1,0,1,1,0],
        7:[1,0,1,1,1],
        8:[1,1,0,0,0],
        9:[1,1,0,0,1]}
pin_addr = {0:[4,17,3,2,27],
            1:[9,11,10,22,5],
            2:[19,26,13,6,21]}
#pin_addr = {0:[4,27,2,3,17],
#            1:[9,5,22,10,11],
#            2:[19,21,6,13,6]}
GPIO.setup(mux_pins,GPIO.OUT)
[GPIO.setup(i,GPIO.OUT) for i in pin_addr.values()]
all_addr = mux_pins+pin_addr[0]+pin_addr[1]+pin_addr[2]
def test_run(len_time: int):
    start_time=datetime.now()
    while True:
        for x in range(8):
            GPIO.output(all_addr,mux_vals[x]+vals[x]+vals[x]+vals[x])
            sleep(.025)
            if start_time+timedelta(seconds=len_time)<=datetime.now():
                GPIO.output(all_addr,mux_vals[-1]+vals[-1]+vals[-1]+vals[-1])
                return
def bcd_0():
    counter = 0
    for key in matrix.LED_VALUE_MATRIX_INDICES.keys():
        if 'top_' in key and '9' not in key and '10' not in key:
            matrix.set_inning_score(key,counter)
            counter+=1
    startTime = datetime.now()
    endTime = startTime + timedelta(seconds=10)
    runner = Thread(target=gpio_runner.run)
    runner.daemon=True
    runner.start()
    while True:
        if datetime.now()>=endTime:
            break
    counter = 8
    for key in matrix.LED_VALUE_MATRIX_INDICES.keys():
        if 'top_' in key and '9' not in key and '10' not in key:
            matrix.set_inning_score(key,counter)
            counter-=1
    startTime = datetime.now()
    endTime = startTime + timedelta(seconds=10)
    while True:
        if datetime.now()>=endTime:
            break
    matrix.all_off()

def bcd_1():
    counter = 0
    for key in matrix.LED_VALUE_MATRIX_INDICES.keys():
        if 'bottom_' in key and '9' not in key and '10' not in key:
            matrix.set_inning_score(key,counter)
            counter+=1
    startTime = datetime.now()
    endTime = startTime + timedelta(seconds=10)
    runner = Thread(target=gpio_runner.run)
    runner.daemon=True
    runner.start()
    while True:
        if datetime.now()>=endTime:
            break
    counter = 8
    for key in matrix.LED_VALUE_MATRIX_INDICES.keys():
        if 'bottom_' in key and '9' not in key and '10' not in key:
            matrix.set_inning_score(key,counter)
            counter-=1
    startTime = datetime.now()
    endTime = startTime + timedelta(seconds=10)
    while True:
        if datetime.now()>=endTime:
            break
    matrix.all_off()

def bcd_2():
    counter = 0
    for key in matrix.LED_VALUE_MATRIX_INDICES.keys():
        if '9' in key or '10' in key or 'runs' in key:
            matrix.set_inning_score(key,counter)
            counter+=1
    startTime = datetime.now()
    endTime = startTime + timedelta(seconds=10)
    runner = Thread(target=gpio_runner.run)
    runner.daemon=True
    runner.start()
    while True:
        if datetime.now()>=endTime:
            break
    counter = 8
    for key in matrix.LED_VALUE_MATRIX_INDICES.keys():
        if '9' in key or '10' in key or 'runs' in key:
            matrix.set_inning_score(key,counter)
            counter-=1
    startTime = datetime.now()
    endTime = startTime + timedelta(seconds=10)
    while True:
        if datetime.now()>=endTime:
            break
    matrix.all_off()

def main():
    matrix.toggle_mux(0,True,all=True)
    print('testing bcd0 (top innings 1-8)')
    bcd_0()
    print('testing bcd1 (bottom innings 1-8)')
    bcd_1()
    print("testing bcd2 (top/bottom innings 9-10, home runs, away runs)")
    bcd_2()
    print('done with bcd test')
def setup(bcd_num):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_addr[bcd_num],GPIO.OUT)
    return pin_addr[bcd_num]

def print_num(bcd_num: int, num: int):
    GPIO.output(pin_addr[bcd_num],vals[num])
    
def bcd_run(bcd_num: int):
    pins = setup(bcd_num)
    for x in range(10):
        print_num(bcd_num,x)
        sleep(.5)
    print_num(bcd_num,-1)
    
def bcd_mux_test(bcd_num: int):
    bcd_pins = pin_addr[bcd_num]
    tot_pins = mux_pins+bcd_pins
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(tot_pins,GPIO.OUT)
    for y in range(20):
        for x in range(8):
            GPIO.output(tot_pins,mux_vals[x]+vals[x])
            sleep(.5)
    GPIO.output(tot_pins,0)
    print('done!')

def set_mux(num: int):
    GPIO.output(mux_pins,mux_vals[num])
    
if __name__=="__main__":
    bcd_run(0)

    


