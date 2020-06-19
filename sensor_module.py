import os
import csv
from mcc import *
import numpy as np
class sensor_manager:

    def __init__(self):
        self.id=None

    def createTable(self):
        self.lookupTable = []
        self.lookupTable.append('00:0a:95:9d:68:14')
        self.lookupTable.append('00:0a:95:9d:68:15')
        self.lookupTable.append('00:0a:95:9d:68:16')
        self.lookupTable.append('00:0a:95:9d:68:17')

    def raise_alarm(self, id, waterlevel, threshold):
        alarm =''
        if (waterlevel > threshold):
            alarm='1'
        elif (waterlevel < 0):
            alarm="error"
        elif (waterlevel <= threshold):
            alarm ='0'
        return alarm

    def update_status(self, status):
        try:
            stat=open("status.txt",'r').read()
            if stat=='high':
                return "Status written in file as "+status
            elif stat=='low':
                stat.write(status)
                return "Status written in file as " + status

        except:

            stat= open("status.txt",'w')
            stat.write(status)
            return "Status written in file as "+status

    def control_net(self, instruction):
        action=""
        if(instruction == 'raise net'):
            action="Net Raised"
        elif(instruction == 'lower net'):
            action="Net Lowered"
        print("Control Net : "+action)
        return action

if __name__=='__main__':
    sens_obj = sensor_manager()
    mcc_object = main_control_center()
    sens_obj.createTable()
    mac=sens_obj.lookupTable
    try:
        instruct = open("instruction.txt", 'r')
        sens_obj.control_net(instruct.read())
        instruct.close()
    except:
        num = input("Enter sensor id:")
        threshold = mcc_object.configure_threshold()
        waterlevel = int(input("Enter water level detected : "))
        with open("sensor_"+ num + ".csv",'w', newline='') as file:
            field=['mac_address','water_level']
            writer=csv.DictWriter(file,field)
            writer.writeheader()
            writer.writerow({'mac_address': mac[int(num)-1],'water_level': waterlevel})
        alarm = sens_obj.raise_alarm(num,waterlevel,threshold)

        if alarm == '1':
            sens_obj.update_status('high')
        elif alarm =='0' or alarm =='error':
            sens_obj.update_status('low')
        print("**** Status file updated ****")
