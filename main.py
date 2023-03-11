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

print("started!")
time.sleep(10)
f = open("/data/log.txt",  "w" )
f.write("\n" +  "Started")
f.close()

while True:
    print()
    try:
        temperature = round(temp.temp(temperature),1)
        z=(time.localtime())
        Zeit=str(z[0]) + "." + str(z[1])+ "." + str(z[2])+ "   " + str(z[3])+ ":" + str(z[4])+ ":" + str(z[5])
        f = open("/data/log.txt",  "a" )
        f.write("\n" +  str(Zeit) + ":   " + str(temperature) + "°C " + "\n")
        f.close()
        mail_attach.send_csv(Zeit, temperature)
        print(Zeit, temperature)
        print()
        time.sleep(3592)
                
    except:
        z=(time.localtime())
        Zeit=str(z[0]) + "." + str(z[1])+ "." + str(z[2])+ "   " + str(z[3])+ ":" + str(z[4])+ ":" + str(z[5])
        f = open("/data/log.txt",  "a" )
        f.write("\n" +  str(Zeit) + ":   " + str(temperature) + "°C " + "  :Try to connect!")
        f.close()
        Zeit = wlan.wifi_on(Zeit)
        print("Try to connect!", Zeit, temperature)
        time.sleep(3592)


