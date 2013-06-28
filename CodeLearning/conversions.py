__author__ = 'AISGIS01'


def metros (metros):
    result = float(metros/1852)
    print result
    print "%d meters are \n%d Nautical Miles " % (metros,result)

def feet (metros):
    print feet/3

metros(15000)