from mcc import *
class water_sensor_1:

    def __init__(self, id, waterlevel):
        self.id = id
        self.waterlevel=waterlevel

    def set_address(self, mac):
        self.mac=mac

    def get_address(self):
        return self.mac_address

    def raise_alarm(self, id, waterlevel, threshold):
        filename = "raise_alarm_"+id
        alarm1 = open(filename, "w")
        if (waterlevel > threshold):
            alarm1.write('1')
        elif (waterlevel < 0):
            alarm1.write("error")
        elif (waterlevel <= threshold):
            alarm1.write('0')

if __name__=='__main__':

    mcc_object = main_control_center()
    id = input("Enter sensor id :")

    water_level = input("Enter water level detected in sensor "+id+" : ")

    open("waterlevel_"+id ,'w').write(water_level)

    threshold=mcc_object.configure_threshold()
    mac=input("Enter MAC address : ")
    sens_obj = water_sensor_1(id, int(water_level))
    sens_obj.set_address(mac)
    sens_obj.raise_alarm(id, int(water_level),threshold)
    print("File written")


