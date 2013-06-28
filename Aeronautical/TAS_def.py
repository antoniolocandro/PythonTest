__author__ = 'Antonio Locandro'
__copyright__ = '(c) 2013'

# The following python script calculates the TAS for a given IAS, height and Temperature Variation (normally +15 degrees celsius

print "IAS to TAS Calculator "

def IAS_to_TAS_conversion (*args):
    #VARint = ISA+15 (it is assumed ISA+15 will be used, code can be changed to accept user input)
    IASint = int(IAS)
    VARint = 15
    Hint = int(H)
    kfactor = 171233*((((288+VARint)-0.00198*Hint)**(0.5))/((288-0.00198*Hint)**(2.628)))
    TASint = IASint*kfactor
    print  "TAS = "+ str(TASint) + " KT for " + H +" ft"

IAS = raw_input ("Input IAS in Knots? ")
H = raw_input("Height in feet? ")
IAS_to_TAS_conversion(IAS,H)

raw_input('Press Enter to exit')


