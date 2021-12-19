from ModelDateTime import get_current_modeldatetime, get_next_modeldatetime

filename = '/users/armankospanov/wrf/WPS-4.0/namelist.wps'
CurrentModelDateTime = get_current_modeldatetime()
NextModelDateTime = get_next_modeldatetime(CurrentModelDateTime)


def format_date(d):
    s = "'"+str(d.year)+"-"+"{0:0>2}".format(d.month)+"-"+"{0:0>2}".format(d.day)+"_"+"{0:0>2}".format(d.hour)+":00:00'"
    return s

def changePlSfc():
    filetext = []
    f = open(filename,'r')
    for line in f:
        s = line
        if line.startswith(" prefix = '") :
            l = len(" prefix = '")
            if line[l:l+2] == "PL":
                s = " prefix = '"+"SFC',\n"
                res = "SFC"
            else:
                s = " prefix = '"+"PL',\n"
                res = "PL"
        filetext.append(s)
    f.close()
    f = open(filename,'w')
    for sss in filetext:
        f.write(sss)
    f.close()
    return res

def changeDates():
    filetext = []
    f = open(filename,'r')
    for line in f:
        s = line
        if line.startswith(" start_date") :
            s = " start_date = " + format_date(CurrentModelDateTime) + "," + format_date(CurrentModelDateTime) + "," + format_date(CurrentModelDateTime)+"\n"
        elif line.startswith(" end_date") :
            s = " end_date   = " + format_date(NextModelDateTime) + "," + format_date(NextModelDateTime) + "," + format_date(NextModelDateTime)+"\n"
        elif line.startswith(" prefix = '") :
            l = len(" prefix = '")
            if line[l:l+2] == "PL":
                s = " prefix = '"+"SFC',\n"
            else:
                s = " prefix = '"+"PL',\n"
        filetext.append(s)
    f.close()
    f = open(filename,'w')
    for sss in filetext:
        f.write(sss)
    f.close()


# uncomment for singleuse. not in MainCycle
#changeDates()
#changePlSfc()
