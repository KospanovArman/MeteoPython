""" 
мне нужны файлы типа gfs.t00z.pgrb2.op25.00nn
где nn номер часа

проблема еще в том что я не всегда начинаю с 0
сейчас например я качаю 9-81

чтобы прогноз был от полудня

все файлы вида gfs.tXXzzpgrb2.op25.00YY
где XX - пофигу, а YY - кратны 3 (00,03,06,09,12,15,18,21)
"""

import requests

fileext = ".idx"
ext = ""
destfolder = '/Users/armankospanov/Desktop/'#'/mnt/f/fcst/DATA/'  #папка для записи файла

hours = {h for h in range(0,243,3)}          #множество часов с шагом 3 для моделирования

def get_and_write(filename):
    f=open(destfolder+filename,"wb")        #открываем файл для записи, в режиме wb в заданную папку
    print("Downloading file :"+filename )
    ufr = requests.get(meteourl+filename)   #делаем запрос
    f.write(ufr.content)                    #записываем содержимое в файл; как видите - content запроса
    f.close()


print('Hello!')
meteodate = input('Введите дату в формате YYYYMMDD : ')
startHour = input('Введите начальный час в формате HH : ')
meteourl1 = "https://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/prod/gfs."

meteourl2 = "/"+startHour+"/atmos/"
filemask = "gfs.t"+startHour+"z.pgrb2.0p25.f"
meteourl = meteourl1+meteodate+meteourl2

print('Запрашиваю данные по адресу : '+ meteourl)
print('Маска файлов : '+ filemask)

urlpage=requests.get(meteourl) #делаем запрос к странице
pagetext = urlpage.text
pagelen = len(pagetext)
substr = '<a href="'

#количество файлов в каталоге. определяем по ссылке <a href=" 
filescount = pagetext.count(substr)
print('Найдено ссылок на файлы : '+str(filescount))
filenames=[] #масcив имен файлов
#выбираем имена файлов 
for i in range(pagelen):
    if pagetext.startswith(substr,i):
        j=0
        filename=''
        while pagetext[9+i+j]!='"':
            filename=filename+pagetext[9+i+j]
            j+=1
        filenames.append(filename)

filename=''
for filename in filenames:
    if filename.startswith(filemask):
        if not filename.endswith(fileext):
            l = len(filename)
            hour = int(filename[l-3])*100 + int(filename[l-2])*10 + int(filename[l-1])
            if hour in hours:
                get_and_write(filename)