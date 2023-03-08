import umail
import wlan
import temp
import network
import mail_attach
import utime as time
Zeit = []
Z = []
t = []
temperature = 0



try:
    Zeit = wlan.wifi_on(Zeit)
except:
    print("connection failed")
    mail_attach.send_csv(Zeit)
    z=(time.localtime())
    t=str(z[0]) + "." + str(z[1])+ "." + str(z[2])+ "   " + str(z[3])+ ":" + str(z[4])+ ":" + str(z[5])

    
    
f = open("/data/log.txt",  "w" )
f.write("\n" +  str(t) + "  :  Started")
f.close()

while True:
    print()
    try:
        temperature = round(temp.temp(temperature),1)
        z=(time.localtime())
        Zeit=str(z[0]) + "." + str(z[1])+ "." + str(z[2])+ "   " + str(z[3])+ ":" + str(z[4])+ ":" + str(z[5])
        mail_attach.send_csv(Zeit, temperature)
        f = open("/data/log.txt",  "a" )
        f.write("\n" +  str(Zeit) + ":   " + str(temperature) + "°C " + "  :  Email sent")
        f.close()
        print(Zeit, temperature," 3600s break")
        time.sleep(3600)
                
    except:
        z=(time.localtime())
        Zeit=str(z[0]) + "." + str(z[1])+ "." + str(z[2])+ "   " + str(z[3])+ ":" + str(z[4])+ ":" + str(z[5])
        f = open("/data/log.txt",  "a" )
        f.write("\n" +  str(Zeit) + ":   " + str(temperature) + "°C " + "  :  Email error")
        f.close()
        Zeit = wlan.wifi_on(Zeit)
        print("error", Zeit, temperature," 3600s break")
        time.sleep(3600)


