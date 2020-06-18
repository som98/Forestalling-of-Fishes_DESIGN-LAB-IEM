from sensor import *
import os
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
        status = open("status", "w")
        num = int(input("Enter no. of sensors: "))
        for i in range (1,num+1):
            alarm = open("raise_alarm_"+str(i),'r').read()
            if(alarm=='1'):
                sens_obj.update_status('high')
                break
            else:
                sens_obj.update_status('low')

        stat= open("status",'r').read()
        print("Status is updated as ",stat)
        try:
            instruct = open("instruction", 'r').read()
        except:
            print("Instruction yet not received for controlling net.")
            exit(0)
        sens_obj.control_net(instruct)
        os.remove("instruction")


