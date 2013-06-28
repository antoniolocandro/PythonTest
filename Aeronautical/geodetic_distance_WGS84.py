__author__ = 'ANTONIO LOCANDRO (c) 2013'
# This module needs geopy installed
# Uses Vincenty's distance formula


from geopy import distance
e = distance.distance((24,5),(35,67)).m
print e


