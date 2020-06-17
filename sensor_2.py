from mcc import *
from sensor_2 import *
class water_sensor_2:

    def __init__(self, waterlevel, mac_address):
        self.waterlevel=waterlevel
        self.mac_address = mac_address

    def get_address(self):
        return self.mac_address

    def raise_alarm(self,waterlevel, threshold):
        alarm1 = open("raise_alarm_2", "w")
        if (waterlevel > threshold):
            alarm1.write('1')
        elif (waterlevel < 0):
            alarm1.write("error")
        elif (waterlevel <= threshold):
            alarm1.write('0')

if __name__=='__main__':

    mcc_object = main_control_center()
    water_level_2 = input("Enter water level detected in sensor 2 : ")
    open("waterlevel_2",'w').write(water_level_2)
    threshold=mcc_object.configure_threshold()
    sen_obj = water_sensor_2(int(water_level_2),threshold)
    sen_obj.raise_alarm(int(water_level_2),threshold)
    print("File written")


