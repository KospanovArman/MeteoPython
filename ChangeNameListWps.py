from ModelDateTime import get_current_modeldatetime, get_next_modeldatetime

filename = '/users/armankospanov/wrf/WPS-4.0/namelist.wps'
CurrentModelDateTime = get_current_modeldatetime()
NextModelDateTime = get_next_modeldatetime(CurrentModelDateTime)


def format_date(d):
    s = "'"+str(d.year)+"-"+"{0:0>2}".format(d.month)+"-"+"{0:0>2}".format(d.day)+"_"+"{0:0>2}".format(d.hour)+":00:00'"
    return s

filetext = []


f = open(filename,'r')
for line in f:
    s = line
    if line.startswith(" start_date") :
        s = " start_date = " + format_date(CurrentModelDateTime) + "," + format_date(CurrentModelDateTime) + "," + format_date(CurrentModelDateTime)+"\n"
    elif line.startswith(" end_date") :
        s = " end_date   = " + format_date(NextModelDateTime) + "," + format_date(NextModelDateTime) + "," + format_date(NextModelDateTime)+"\n"
    filetext.append(s)
f.close()

f = open(filename,'w')
for sss in filetext:
    f.write(sss)
f.close()
