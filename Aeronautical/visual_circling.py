__author__ = 'Antonio Locandro'

<<<<<<< HEAD
# Visual Circling Calculations

IASvisualapproach = {'CAT A':100,'CAT B':135,'CAT C':180,'CAT D':205, 'CAT E':240}
=======
from math import *
from numpy import *
print sqrt(25)
>>>>>>> a few changes in aeronautical scripts

def IAS_to_TAS_conversion (*args):
    #VARint = ISA+15 (it is assumed ISA+15 will be used, code can be changed to accept user input)
    #IASint = int(IAS)
    VARint = 15
    Hint = int(H)
    kfactor = 171233*((((288+VARint)-0.00198*Hint)**(0.5))/((288-0.00198*Hint)**(2.628)))
    TASint = IASint*kfactor
    #print  "TAS = "+ str(TASint) + " KT for " + H +" ft"

H = raw_input("Height in feet? ")
IAS_to_TAS_conversion(IASvisualapproach['CAT A'],H)



raw_input('Press Enter to exit')
