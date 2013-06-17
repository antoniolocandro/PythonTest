__author__ = 'Antonio Locandro'

# The following python script calculates the TAS for a given IAS, height and Temperature Variation (normally +15 degrees celsius



print "IAS to TAS Calculator "

IAS = raw_input ("Input IAS in Knots? ")
VAR = raw_input("VAR? normally 15 degrees Celsius " )
H = raw_input("Height in feet? ")

IASint = int(IAS)
VARint = int(VAR)
Hint = int(H)

kfactor = 171233*((((288+VARint)-0.00198*Hint)**(0.5))/((288-0.00198*Hint)**(2.628)))
TASint = IASint*kfactor

print "Conversion Factor k= " + str(kfactor)
print "TAS= "+ str(TASint) + " KT for " + H +" ft"
raw_input('Press Enter to exit')


