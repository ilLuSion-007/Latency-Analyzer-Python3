#*******************    For OS = Linux    ****************



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
cip = getip.get()
#----------------------location-------------------------



def locationfxn(self):

            header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0'}
            url = "http://api.ipstack.com/{0}?access_key=0f7428b8e19bb508ea42f672ca7b5203&output=json&legacy=1".format(self)
            txt = requests.get(url, headers=header).text
            d = json.loads(txt)

            city = d.get('city')
            longitude = d.get('longitude')
            latitude = d.get('latitude')
            country = d.get('country_name')
            country_code = d.get('country_code')
            return city, longitude, latitude, country, country_code
            print("fxn one")



#------------ To get ping data into file ---------------

def logos():
            logo = ''' ******************* PLEASE WAIT FOR A WHILE ****************
                       *********************************************************
                          ***************  IT MAY TAKE SOME TIME  ***********
                       ***********************************************************
                       ************* MAKE SURE THAT INTERNET IS WORKING*********** '''

            print(logo)
            print("")
            print("[+] SUCCESSFULLY CONNECTED TO LATENCY SERVER [+]")
            print("NOTE - DO NOT USE ANY VPN OR PROXY")
            print("[+] YOU WILL BE NOTIFIED WHEN COMPLETED [+]")
            print("IT WILL TAKE 5 MIN. OR MORE, PLEASE WAIT...")




def get_data(x,y):
      with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=UserWarning)
            c_data = locationfxn(cip)
            c_city = c_data[0]
            c_longitude = c_data[1]
            c_latitude = c_data[2]
            c_country = c_data[3]
            c_country_code = c_data[4]

                    #conn = pymysql.connect(host='localhost',user='root',password='',db='All_domains')
            #conn = pymysql.connect(host='localhost',user='root',password='',db='All_domains')
            data = []
            #a = conn.cursor()
            #j=0
            start = "(b'PING"
            end = 'bytes'
            start1='('
            end1=')'
            start2="min/avg/max/mdev = "
            end2 = " ms\\n', None)"
            #print("[+]CONNECTING TO DATABASE[+]")
            conn = pymysql.connect(host='101.99.74.61', port=3306, user='latency',password='latency@123',db='latency')
            a = conn.cursor()
            #print("[+]CONNECTED TO DATABASE[+] ")



            for i in range(x,y):
            #    j += 1
            #    print(r"PROCESS COMPLETED %{}...".format(j))
                #conn = pymysql.connect(host='185.11.146.151', port=3306, user='latency',password='latency@123',db='latency')

                # conn = pymysql.connect(host='localhost',user='root',password='',db='All_domains')
                # a = conn.cursor()
                domain_get = "SELECT Domain FROM domains WHERE Id="+str(i)+";"
                a.execute(domain_get)
                get=list(a.fetchall())

                get= list(get[0])
                get=str(get[0])
                data.append(get)

                p = subprocess.Popen("ping -c 4 {}".format(get), shell=True, stdout=subprocess.PIPE)
                c = str(p.communicate())
                if len(c) > 200:

                    d = c.split("\\r\\n")
                    ip=asn=lat=''

                    flag = 0
                    flag2 = 0

                    for k in d:

                        flag +=1
                        if (flag == 1 or flag == 10):
                            if(k.find("(b'PING")==0):
                                this = (k.split(start))[1].split(end)[0]

                                this = this.split(" ")
                                this = str(this[2])
                                this = (this.split(start1))[1].split(end1)[0]
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

                                    obj2 = IPWhois(cip)
                                    results = obj.lookup_rdap()
                                    p = results.get('asn')

                                    c_asn=str(p)
                                    data.append(c_asn)
                                if(k.find("100% packet loss") != 0):
                                    this2 = (k.split(start2))[1].split(end2)[0]
                                    this2 = this2.split("/")
                                    this2 = this2[1]
                                    lat = this2
                                    data.append(lat)
                                    #t = datetime.datetime.utcnow()
                                    #tt = str(t)
                                    #data.append(tt)
                                """
                                else:
                                    lat = '#'
                                    data.append(lat)
                                    #t = datetime.datetime.utcnow()
                                    #tt = str(t)
                                    #data.append(tt)
                                """


                            sql = "INSERT INTO `ipasnlat` (`domain`, `ip`, `ASN`, `Latency`,`d_latitude`, `d_longitude`, `d_city`, `d_country`, `d_country_code`, `c_asn`, `client_ip`, `c_country`, `c_country_code`, `c_city`, `c_longitude`, `c_latitude`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                            a.execute(sql, (data[0], data[1], data[2], data[4], d_latitude, d_longitude, d_city, d_country, d_country_code, data[3], cip, c_country, c_country_code, c_city, c_longitude,c_latitude))

                            data = []

                else:
                    data = []
                    continue

                conn.commit()
            conn.close()

                        #print(get,ip,asn,lat,datetime.datetime.utcnow())

if __name__ == "__main__":
               #pinger = ping.get_ping_data()

               while True:


                    try:

                        logos()

                        t1 = threading.Thread(target=get_data , args=(1,10))
                        t2 = threading.Thread(target=get_data , args=(10,20))
                        t3 = threading.Thread(target=get_data , args=(20,30))
                        t4 = threading.Thread(target=get_data , args=(30,40))
                        t5 = threading.Thread(target=get_data , args=(40,50))
                        t6 = threading.Thread(target=get_data , args=(50,60))
                        t7 = threading.Thread(target=get_data , args=(60,70))
                        t8 = threading.Thread(target=get_data , args=(70,80))
                        t9 = threading.Thread(target=get_data , args=(80,90))
                        t10 = threading.Thread(target=get_data , args=(90,101))

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
