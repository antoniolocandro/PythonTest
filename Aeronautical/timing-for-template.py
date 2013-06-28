__author__ = 'Antonio Locandro'

# PANS OPS Timing done for CAT H aircraft only
# The code is not to be used for operational use, just to do preliminary work as I am learning to code

def intersectionTime ():
    return (height-airportElevation)/(inboundMaxRate+outboundMaxRate)

def intersectionAltitude ():
    return -outboundMaxRate*intersectionTime()+height

height = float(raw_input("Altitude at the Initial Approach Fix in feet = "))/3.2808 #conversion to meters
airportElevation = float(raw_input("Aerodrome Altitude in meters = "))+15 # The aerodrome altitude should be read from file
outboundMaxRate = 365.0 # m/min
inboundMaxRate = 230.0 # m/min

print "Exact Time is "+str (intersectionTime ())+" min"+'\n'+"Turn base altitude should be " +'\n'+str(intersectionAltitude())+" meters /" +'\n'+ str(intersectionAltitude()*3.2808)+" feet"

raw_input('Press Enter to exit')