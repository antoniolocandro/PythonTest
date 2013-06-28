__author__ = 'Antonio Locandro'

# This script provides the time to compensate on a VOR/NDB procedure based on timing
# Right now just caters for CAT H
# TODO list to be able to do all categories

def timeCompensation (distNavToRwyCline):
    return (distNavToRwyCline/TAS)*60

distNavToRwyCline = float(raw_input("distance from Navaid to runway intersection in NM? "))
TAS = float(raw_input("TAS in kt? "))

print str(timeCompensation (distNavToRwyCline)) + " minutes are needed to compensate"