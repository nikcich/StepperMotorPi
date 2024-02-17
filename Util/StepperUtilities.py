import math

def map_range(x, in_min, in_max, out_min, out_max):
    return round(out_min + (x - in_min) * (out_max - out_min) / (in_max - in_min), 5)