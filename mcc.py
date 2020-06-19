from sensor_module import *
import numpy as np
import csv
class main_control_center():
    def _init_(self):
        self.id = None

    def configure_threshold(self):
        return 300

    def send_signal(self,mac_address):
        if(mac_address!="null" and  mac_address!=''):
            return (1)
        else:
            return (0)
    def updateTable(self,lookup_table,mac,waterlevel):
        lookup_table=np.append(lookup_table,np.array([[mac,waterlevel]]),axis=0)
        return lookup_table

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
    sens1 = sensor_manager()
    num = int(input("Enter number of sensors in your system: "))
    lookupTable = np.array([['mac','waterlevel']])
    try:

        for i in range (1,num+1):
            with open("sensor_"+str(i)+".csv" , 'r') as file:
                data=csv.DictReader(file)
                for row in data:
                    waterlevel=row['water_level']
                    mac = row['mac_address']
            lookupTable = mcc_object.updateTable(lookupTable,mac,waterlevel)
            signal1 = mcc_object.send_signal(mac)
            if(signal1==1):
                print("Connection to sensor" + str(i) + " established")
            else:
                print("Connection to sensor" + str(i) + " not established")
        print("Updated lookup table ::: ")
        print(lookupTable)
    except:
        print("You may have given higher number of sensors.")

    stat=open("status.txt","r").read()
    print ("Status received as ",stat)
    value=mcc_object.receive_status(stat)
    ins=mcc_object.send_instruction(value)
    file= open("instruction.txt",'w').write(ins)
    print("**** Instruction written to file ****")
