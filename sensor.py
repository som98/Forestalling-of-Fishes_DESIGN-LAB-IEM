from mcc import *
class water_sensor_1:

    def __init__(self):
        self.id=None

    def set_address(self, mac):
        self.mac=mac

    def get_address(self):
        return self.mac

    def raise_alarm(self, id, waterlevel, threshold):
        filename = "raise_alarm_"+id
        alarm1 = open(filename, "w")
        alarm =''
        if (waterlevel > threshold):
            alarm='1'
        elif (waterlevel < 0):
            alarm="error"
        elif (waterlevel <= threshold):
            alarm ='0'
        alarm1.write(alarm)
        return alarm

if __name__=='__main__':
    mcc_object = main_control_center()
    num = int(input("Enter no. of sensors :"))
    threshold = mcc_object.configure_threshold()
    sens_obj = water_sensor_1()
    for i in range (1,num+1):
        water_level = input("Enter water level detected in sensor " + str(i) + " : ")
        open("waterlevel_"+str(i) ,'w').write(water_level)
        mac=input("Enter MAC address : ")
        sens_obj.set_address(mac)
        sens_obj.raise_alarm(str(i), int(water_level),threshold)
        print("File written")



