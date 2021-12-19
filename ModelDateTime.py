from datetime import datetime
from datetime import timedelta
filename = '/users/armankospanov/wrf/ModelDateTime'

def get_current_modeldatetime():
    f = open(filename,'r')
    yyyymmddhh = f.read()
    f.close()
    yyyy =  int(yyyymmddhh[0:4])
    mm =    int(yyyymmddhh[4:6])
    dd =    int(yyyymmddhh[6:8])
    hh =    int(yyyymmddhh[8:10])
    d = datetime(yyyy,mm,dd,hh)
    return d

def get_next_modeldatetime(d):
    delta = timedelta(hours=12)
    d = d + delta
    return d

def save_next_modeldatetime():
    d = get_next_modeldatetime(get_current_modeldatetime())
    yyyymmddhh = str(d.year)+"{0:0>2}".format(d.month)+"{0:0>2}".format(d.day)+"{0:0>2}".format(d.hour)
    f = open(filename,'w')
    f.write(yyyymmddhh)
    f.close()
    return d
