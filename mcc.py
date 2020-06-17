from sensor_1 import *
from sensor_2 import *
from sensor_manager import *
class main_control_center():
    def _init_(self):
        self.id = None

    def get_water_sensor_data(self, water_level, mac_address):
        self.water_sensor_address= mac_address
        self.water_sensor_data = water_level

    def configure_threshold(self):
        return 300

    def send_signal(self,mac_address):
        if(mac_address!="null"):
            return (1)
        else:
            return (0)

    def send_instruction(self, value):
        if (value == 1):
            return('raise net')
        elif (value == 0):
            return('lower net')

    def receive_status(self, status):
        if(status=='high'):
            return (1)
        elif(status=='low'):
            return (0)
if __name__=='__main__':
    mcc_object = main_control_center()
    water_level_1 = int(open("waterlevel_1", 'r').read())
    water_level_2 = int(open("waterlevel_2", 'r').read())
    manager = sensor_manager()

    sens1 = water_sensor_1(water_level_1, "192.0.0.1")
    sens2 = water_sensor_2(water_level_2, "192.0.0.2")

    signal1= mcc_object.send_signal(sens1.mac_address)
    signal2= mcc_object.send_signal(sens2.mac_address)
    if(signal1==1):
        print("Connection to sensor 1 established")
    else:
        print("Connection to sensor 1 not established")
    if (signal2 == 1):
        print("Connection to sensor 2 established")
    else:
        print("Connection to sensor 2 not established")

    stat=open("status","r").read()
    print ("Status received as ",stat)
    value=mcc_object.receive_status(stat)
    ins=mcc_object.send_instruction(value)
    file= open("instruction",'w').write(ins)
    print("**** Instruction written to file ****")
