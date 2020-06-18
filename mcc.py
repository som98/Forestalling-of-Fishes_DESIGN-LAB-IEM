from sensor import *
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
    manager = sensor_manager()
    num = int(input("Enter number of sensors: "))
    for i in range (1,num+1):
        water_level = int(open("waterlevel_"+str(i) , 'r').read())
        sens1 = water_sensor_1(str(i), water_level)
        signal1 = mcc_object.send_signal(sens1.get_address)
        if(signal1==1):
            print("Connection to sensor" + str(i) + " established")
        else:
            print("Connection to sensor" + str(i) + " not established")

    stat=open("status","r").read()
    print ("Status received as ",stat)
    value=mcc_object.receive_status(stat)
    ins=mcc_object.send_instruction(value)
    file= open("instruction",'w').write(ins)
    print("**** Instruction written to file ****")
