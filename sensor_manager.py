from sensor_1 import *
from sensor_2 import *
from mcc import *
class sensor_manager:
    def __init__(self):
        self.id=None

    def update_status(self, status):
        stat= open("status",'w')
        stat.write(status)

    def control_net(self, instruction):
        if(instruction == 'raise net'):
            print("Control Net : Net Raised")
        elif(instruction == 'lower net'):
            print("Control Net : Net Lowered")

if __name__=='__main__':

        sens_obj= sensor_manager()
        mcc_object=main_control_center()
        alarm1= open("raise_alarm_1",'r').read()
        alarm2 = open("raise_alarm_2",'r').read()
        status = open("status", "w")
        if(alarm1 =='0' and alarm2 =='0'):
            sens_obj.update_status('low')
        elif(alarm1=='1' or alarm2=='1'):
            sens_obj.update_status('high')

        stat= open("status",'r').read()
        print("Status is updated as ",stat)
        try:
            instruct = open("instruction", 'r').read()
        except:
            print("Instruction yet not received for controlling net.")
            exit(0)
        sens_obj.control_net(instruct)
