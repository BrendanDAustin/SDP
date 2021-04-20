#from RPi.GPIO import LOW, HIGH
import timeit
import pandas as pd
from numpy import array
LOW= False
HIGH = True
class gpio_map:
    def __init__(self):
        self.mux = {'en':7,
                    'C':20,
                    'B':16,
                    'A':12}
#         self.mux = {'C':20,
#                'B':16,
#                'A':12,
#                'en':7}
        self.bcd_0 = {'en':4,
                      'D':17,
                      'C':3,
                      'B':2,
                      'A':27}
#         self.bcd_0 = {'en':4,
#                  'A':27,
#                'B':2,
#                'C':3,
#                'D':17}
        self.bcd_1 = {'en':9,
                      'D':11,
                      'C':10,
                      'B':22,
                      'A':5}
#         self.bcd_1 = {'en':9,
#                'A':5,
#                'B':22,
#                'C':10,
#                'D':11}
        self.bcd_2 = {'en':19,
                      'D':26,
                      'C':13,
                      'B':6,
                      'A':21}
#         self.bcd_2 = {'en':19,
#                  'A':21,
#                  'B':6,
#                  'C':13,
#                  'D':26}
        self.bases_balls_strikes = 8
        self.outs = 25

        self.pin_set = self.create_tuples()

    def create_tuples(self):
        pin_set = []
        for i in [self.mux.values(),self.bcd_0.values(),self.bcd_1.values(),self.bcd_2.values()]:
            for j in i:
                pin_set.append(j)
        pin_set.insert(-1,self.bases_balls_strikes)
        pin_set.insert(-1,self.outs)
        return pin_set
    
if __name__=="__main__":
    mux = gpio_map()
    print(mux.create_tuples)