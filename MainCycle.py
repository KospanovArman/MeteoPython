import os
import time
from datetime import datetime
from ModelDateTime import get_current_modeldatetime, get_next_modeldatetime,save_next_modeldatetime
from ChangeNameListWps import changeDates, changePlSfc
from ChangeNameListInput import goNameListInput

CurrentModelDateTime = get_current_modeldatetime()
NextModelDateTime = get_next_modeldatetime(CurrentModelDateTime)
root = "/users/armankospanov/wrf"
both = True #лог в файл и на консоль. иначе только в файл

def str_time(d):
    return str(d.year) +"-" + "{0:0>2}".format(d.month) + "-" + "{0:0>2}".format(d.day) + "-" + "{0:0>2}".format(d.hour)+"-"+"{0:0>2}".format(d.minute)+"-"+"{0:0>2}".format(d.second)

def open_log():
    d=datetime.today()
    logname = "Modeling_log_"+ str_time(d)
    f = open(logname,'w')
    f.write('Log started \n')
    f.write('CurrentModelDateTime = ' + str(CurrentModelDateTime)+'\n')
    return f

def close_log(f):
    f.write('Log closed \n')
    f.close()

def print_log(msg,f):
    s = str_time(datetime.today())+' : '+msg+'\n'
    f.write(s)
    if both :
        print(s)
        f.write(s)
    else:
        f.write(s)

LogFileName = open_log()

while CurrentModelDateTime.year <=2021 and CurrentModelDateTime.month<=7 and CurrentModelDateTime.<=1:
    os.chdir(root)
    os.chdir(root+"/share_frcst")
    print_log("Removing emcf*",LogFileName )
    #---os.system("rm emcf*.*")
    print_log("emcf* removed",LogFileName )

    T2DMMDDHH = "T2D"+"{0:0>2}".format(CurrentModelDateTime.month)+"{0:0>2}".format(CurrentModelDateTime.day)+"{0:0>2}".format(CurrentModelDateTime.hour)
    print_log("Grib_filter started ",LogFileName )
    cmd = "grib_filter split.rule "+T2DMMDDHH+"*1"
    #---os.system(cmd)
    print_log("Grib_filter done ",LogFileName )

    os.chdir(root+"/WPS-4.0")
    print_log("Removing pl*,sfc*,met_em*",LogFileName )
    #---os.system("rm pl*.*")
    #---os.system("rm sfc*.*")
    #---os.system("rm met_em*.*")
    print_log("pl*,sfc*,met_em* removed",LogFileName )

    print_log("Setting dir and ld_library_path",LogFileName )
    os.environ["DIR"] = "/home/wrf/Build_WRF/LIBRARIES"
    os.environ["LD_LIBRARY_PATH"] = "$DIR/grib2/lib:$LD_LIBRARY_PATH"

    print_log("Changing namelist.wps dates",LogFileName )
    changeDates()
    PLorSFC = changePlSfc()

    #---os.system("geogrid.exe")
    YYYYMMDD = str(CurrentModelDateTime.year)+"{0:0>2}".format(CurrentModelDateTime.month)+"{0:0>2}".format(CurrentModelDateTime.day)
    if PLorSFC == "SFC":
        print_log("Changing pl to sfc", LogFileName)
    #---    os.system("link_grib.csh /home/wrf/share_frcst/ecmf_"+YYYYMMDD+"_fc_sfc_*1")
        os.system("ungrib.exe")
    else
        print_log("ошибка. должен был быть заменен блок pl на sfc", LogFileName)

    PLorSFC = changePlSfc()
    if PLorSFC == "PL":
        print_log("Changing sfc to pl", LogFileName)
    #---    os.system("link_grib.csh /home/wrf/share_frcst/ecmf_"+YYYYMMDD+"_fc_pl_*1")
    #---    os.system("ungrib.exe")
    else
        print_log("ошибка. должен был быть заменен блок sfc на pl", LogFileName)
    #---os.system("metgrid.exe")

    os.chdir(root+"/WRF/run")
    #---os.system("rm met_em*")
    #---os.system("ln -s /home/wrf/WPS-4.0/met_em*")
    goNameListInput()
    #---os.system("real.exe")
    #---os.system("screen -r")
    #---os.system("ulimit -s unlimited")
    #---os.system("mpirun -np 6 ./wrf.exe")
    time.sleep(7200)
    os.environ["LD_LIBRARY_PATH"] = "/lib/x86_64-linux-gnu/libz.so.1"

    save_next_modeldatetime()
    CurrentModelDateTime = get_current_modeldatetime()
    NextModelDateTime = get_next_modeldatetime(CurrentModelDateTime)

close_log(LogFileName )
