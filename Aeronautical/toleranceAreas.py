__author__ = 'Antonio Locandro'

print "Tolerance Area Calculations for NDB"

from math import tan
from math import sin
from math import radians


def ndbToleranceArea (height):
    return 0.164*(height/1000)*tan(radians(40))

def ndbToleranceDist (height):
    return ndbToleranceArea(height)*sin(radians(15))

height = float(raw_input("Altitude at the Initial Approach Fix = "))

print "zN " + str(ndbToleranceArea (height)) + " NM"+'\n' + "qN " + str (ndbToleranceDist (height)) + " NM"

raw_input('Press ENTER to exit')

