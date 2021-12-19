from ModelDateTime import get_current_modeldatetime, get_next_modeldatetime

filename = '/users/armankospanov/wrf/WRF/run/namelist.input'
CurrentModelDateTime = get_current_modeldatetime()
NextModelDateTime = get_next_modeldatetime(CurrentModelDateTime)

def convert_year(yyyy,d):
    res = "{:<37}".format(yyyy) + "= " + str(d.year) + ", "+str(d.year) + ","+str(d.year)+",\n"
    return res

def convert_month(mm, d):
    res = "{:<37}".format(mm) + "= " + "{0:0>2}".format(d.month)+ ",   " + "{0:0>2}".format(d.month) + ", " + "{0:0>2}".format(d.month) + ",\n"
    return res

def convert_day(dd, d):
    res = "{:<37}".format(dd) + "= " + "{0:0>2}".format(d.day)+ ",   " + "{0:0>2}".format(d.day) + "," + "{0:0>2}".format(d.day) + ",\n"
    return res

def convert_hour(hh, d):
    res = "{:<37}".format(hh) + "= " + "{0:0>2}".format(d.hour)+ ",   " + "{0:0>2}".format(d.hour) + "," + "{0:0>2}".format(d.hour) + ",\n"
    return res

def goNameListInput():
    filetext = []
    f = open(filename,'r')
    for line in f:
        s = line
        if line.startswith(" start_year"):    s = convert_year(" start_year", CurrentModelDateTime)
        elif line.startswith(" start_month"): s = convert_month(" start_month", CurrentModelDateTime)
        elif line.startswith(" start_day"):   s = convert_day(" start_day", CurrentModelDateTime)
        elif line.startswith(' start_hour'):  s = convert_hour(" start_hour", CurrentModelDateTime)
        elif line.startswith(" end_year"):    s = convert_year(" end_year", NextModelDateTime)
        elif line.startswith(" end_month"):   s = convert_month (" end_month", NextModelDateTime)
        elif line.startswith(" end_day"):     s = convert_day (" end_day", NextModelDateTime)
        elif line.startswith(' end_hour'):    s = convert_hour(" end_hour", NextModelDateTime)
        filetext.append(s)
    f.close()

    f = open(filename,'w')
    for sss in filetext:
        f.write(sss)
    f.close()
