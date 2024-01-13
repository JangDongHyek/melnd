import pyMeow as pm
from random import randint

import globals

for (i,m) in enumerate(globals.map):
    low_y = m["low_y"] - 2
    high_y = m["high_y"] + 2
    print(m)
    print(i)
