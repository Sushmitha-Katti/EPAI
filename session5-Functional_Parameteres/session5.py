import time
from math import tan, pi
import math

def time_it(fn, *args, repetitons= 1, **kwargs):
    start = time.perf_counter()
    if (repetitons <= 0):
        raise ValueError("repetitions should be greater that 0")
    if (not(isinstance(repetitons,int))):
        raise ValueError("Repetions must be of type Integer")
    for _ in range(repetitons):
        fn(*args, **kwargs)
    stop = time.perf_counter()
    return ((stop - start)/repetitons)


def squared_power_list(num,start,end):
    square_list = []
    if(not (isinstance(start, int) and isinstance(end,int))):
        raise ValueError("Start and End must be intergers")
    if(start>end):
        raise ValueError("Stop must be greater than end")
    for i in range (start,end+1):
        square_list.append(math.pow(num,i))
    return square_list



def polygon_area( side_length, sides = 3):
    if(sides < 3 or sides > 6 ):
        raise ValueError("number of sides must be greater than 2 and less than 7")
    if(side_length < 0 ):
        raise ValueError("side length must be positive")

    return sides * (side_length ** 2) / (4 * tan(pi / sides))


def speed_converter(source_value = 100, dist='km', time='hr'):
    distance_conv = { 'km' : 1, 'm':  1000, 'ft':3280.84, 'yrd':1093.61 }
    time_conv = {'ms':3.6e+6,  's': 3600, 'm': 60  ,'hr' : 1, 'day': 0.0416666667 }

    if(dist not in ('km','m','ft','yrd')):
        raise ValueError("Distance should be any of type (km,m,ft,yrd)")

    if(time not in ('ms','s','m','hr','day')):
        raise ValueError("Time should be any of type ('ms','s','m','hr','day')")

    source_value *= (distance_conv[dist]/time_conv[time])
    return source_value



def temp_converter(base_temp, temp_given_in):
    if(temp_given_in  not in ('f', 'c')):
        raise ValueError("temperature should be given in either f or c (faraheineit or celsious) ")
    return ((base_temp - 32) * 5/9) if temp_given_in == 'f' else ((base_temp * 9/5) + 32)


