#*******************    For OS = WINDOWS    ****************



#   ------------------------------------
#   Data to DB
#   ------------------------------------

from ipwhois import IPWhois
#import pprint
import subprocess
import warnings
import pymysql
import datetime
import time
import requests
import json
import getip
import threading
import sys
cip = getip.get()
#----------------------location-------------------------

def locationfxn(ipp):

    header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0'}
    url = "http://api.ipstack.com/{0}?access_key=0f7428b8e19bb508ea42f672ca7b5203&output=json&legacy=1".format(ipp)
    txt = requests.get(url, headers=header).text
    d = json.loads(txt)

    city = d.get('city')
    longitude = d.get('longitude')
    latitude = d.get('latitude')
    country = d.get('country_name')
    country_code = d.get('country_code')
    return city, longitude, latitude, country, country_code


def all_data(x,y):

    with warnings.catch_warnings():

                            warnings.filterwarnings("ignore", category=UserWarning)
                            c_data = locationfxn(cip)
                            c_city = c_data[0]
                            c_longitude = c_data[1]
                            c_latitude = c_data[2]
                            c_country = c_data[3]
                            c_country_code = c_data[4]

                            #conn = pymysql.connect(host='localhost',user='root',password='',db='All_domains')

                            #a = conn.cursor()
                            #j = 0
                            start = '['
                            end = ']'
                            #domain_id=1
                            #print("[+]CONNECTING TO DATABASE[+]")
                            conn = pymysql.connect(host='185.22.154.187', port= 3306, user='latency',password='latency@123',db='latency')
                            a = conn.cursor()
                            #print("[+]CONNECTED TO DATABASE[+] ")
                            for i in range(x,y):
                                #j+=1
                                #print(r"PROCESS COMPLETED %{}...".format(j))
                                # conn = pymysql.connect(host='localhost',user='root',password='',db='All_domains')
                                # a = conn.cursor()
                                data = []
                                #data.append(str(domain_id))
                                domain_get = "SELECT Domain FROM domains WHERE Id="+str(i)+";"
                                a.execute(domain_get)
                                get=list(a.fetchall())

                                get= list(get[0])
                                get=str(get[0])
                                data.append(get)
                               
                                #a.execute("INSERT INTO ipasnlat(domain_id,Domain) VALUES(%s,%s);" %(i,get))
                                p = subprocess.Popen("ping {}".format(get), shell=True, stdout=subprocess.PIPE)
                                c = str(p.communicate())

                                d = c.split("\\r\\n")
                                ip=''
                                asn=''
                                lat=''
                                flag = 0
                                flag2 = 0
                                c_asn = ''
                                for k in d:

                                    if(flag2==2):
                                        flag=0
                                    flag += 1
                                    if (flag == 11 or flag == 2 or flag == 10):
                                        if (flag == 10):
                                             if (k.find('Approximate') == -1):
                                                 flag2 += 1
                                                 lat=" ## "
                                                 data.append(lat)
                                                 #t = datetime.datetime.utcnow()
                                                 #tt = str(t)
                                                 #data.append(tt)

                                             if(flag2==2):
                                                 
                                            
                                                 #domain_id += 1
                                                 #insert = ("INSERT INTO ipasnlat" + "VALUES(%s,%s,%s,%s)")
                                                 sql = "INSERT INTO `ipasnlat` (`domain`, `ip`, `ASN`, `Latency`,`d_latitude`, `d_longitude`, `d_city`, `d_country`, `d_country_code`, `c_asn`, `client_ip`, `c_country`, `c_country_code`, `c_city`, `c_longitude`, `c_latitude`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                                 a.execute(sql, (data[0], "#", "#", "#","#", "#", "#", "#", "#", "#", cip, c_country, c_country_code, c_city, c_longitude,c_latitude))


                                        if (flag == 11 or flag == 2):
                                            flag2 += 1
                                            if(k.find('Pinging')==0):
                                                this = (k.split(start))[1].split(end)[0]
                                                data.append(this)
                                                d_data = locationfxn(this)
                                                d_city =  d_data[0]
                                                d_longitude =  d_data[1]
                                                d_latitude =  d_data[2]
                                                d_country =  d_data[3]
                                                d_country_code =  d_data[4]
                                    

                                                with warnings.catch_warnings():

                                                    warnings.filterwarnings("ignore", category=UserWarning)

                                                    obj = IPWhois(this)
                                                    results = obj.lookup_rdap()
                                                    g = results.get('asn')

                                                    asn=str(g)
                                                    data.append(asn)
                                                with warnings.catch_warnings():
                                                    warnings.filterwarnings("ignore", category=UserWarning)

                                                    obj2 = IPWhois(cip)
                                                    results = obj.lookup_rdap()
                                                    p = results.get('asn')

                                                    c_asn=str(p)
                                                    data.append(c_asn)

                                                    


                                            elif (k.find('=') != -1):
                                                get = k.split('=')

                                                lat=get[3].lstrip()
                                                lat = lat.strip('ms')
                                                data.append(lat)
                                                #t = datetime.datetime.utcnow()
                                                #tt = str(t)
                                                #data.append(tt)







                                            if(flag2==2):
                                                
                                                data[4] = str(data[4])
                                                #domain_id += 1
                                               # insert = ("INSERT INTO ipasnlat" + "VALUES(%s,%s,%s,%s)")
                                               # sql = "INSERT INTO `ipasnlat` (`domain`, `ip`, `ASN`, `Latency`, `client_ip`, `country`, `country_code`, `city`, `longitude`, `latitude`, `date_time`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                                #a.execute(sql, (data[0], data[1], data[2], data[3], ipp, country, country_code, city, longitude,latitude, data[4]))
                                                sql = "INSERT INTO `ipasnlat` (`domain`, `ip`, `ASN`, `Latency`,`d_latitude`, `d_longitude`, `d_city`, `d_country`, `d_country_code`, `c_asn`, `client_ip`, `c_country`, `c_country_code`, `c_city`, `c_longitude`, `c_latitude`) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                                a.execute(sql, (data[0], data[1], data[2], data[4], d_latitude, d_longitude, d_city, d_country, d_country_code, data[3], cip, c_country, c_country_code, c_city, c_longitude,c_latitude))
                         
                              
                                                #print(get,ip,asn,lat,datetime.datetime.utcnow())

                                conn.commit()
                            conn.close()


#------------ To get ping data into file ---------------

def get_ping_data():
    logo = ''' ******************* PLEASE WAIT FOR A WHILE ****************
               *********************************************************
                  ***************  IT MAY TAKE SOME TIME  ***********
               ***********************************************************
               ************* MAKE SURE THAT INTERNET IS WORKING***********'''

    print(logo)
    print("")
    print("[+] SUCCESSFULLY CONNECTED TO LATENCY SERVER [+]")
    print("NOTE - DO NOT USE ANY VPN OR PROXY")
    print("[+] YOU WILL BE NOTIFIED WHEN COMPLETED [+]")
    print("IT WILL TAKE 5 MIN. OR MORE, PLEASE WAIT...")
 


while True:


    try:
        get_ping_data()       
        t1 = threading.Thread(target= all_data, args= (1,10))
        t2 = threading.Thread(target= all_data, args= (10,20))
        t3 = threading.Thread(target= all_data, args= (20,30))
        t4 = threading.Thread(target= all_data, args= (30,40))
        t5 = threading.Thread(target= all_data, args= (40,50))
        t6 = threading.Thread(target= all_data, args= (50,60))
        t7 = threading.Thread(target= all_data, args= (60,70))
        t8 = threading.Thread(target= all_data, args= (70,80))
        t9 = threading.Thread(target= all_data, args= (80,90))
        t10 = threading.Thread(target= all_data, args= (90,101))
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t9.start()
        t10.start()
        t1.join()
        print("10% PROCESS COMPLETED...")
        t2.join()
        print("20% PROCESS COMPLETED...")
        t3.join()
        print("30% PROCESS COMPLETED...")
        t4.join()
        print("40% PROCESS COMPLETED...")
        t5.join()
        print("50% PROCESS COMPLETED...")
        t6.join()
        print("60% PROCESS COMPLETED...")
        t7.join()
        print("70% PROCESS COMPLETED...")
        t8.join()
        print("80% PROCESS COMPLETED...")
        t9.join()
        print("90% PROCESS COMPLETED...")
        t10.join()
        print("100% PROCESS COMPLETED...")

        print("[+]FINISHED, THANKS FOR YOUR TIME[+]")
        time.sleep(20)
	   
	   
        break

    except Exception as e:
        print(e)
       
	  
        
