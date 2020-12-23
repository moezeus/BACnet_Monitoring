import BAC0
import paho.mqtt.client as mqtt 
from random import randrange
import time
import configparser

config = configparser.ConfigParser()
config.read('command.ini')

# inisialisasi variabel
device0 = 0
device0address = 0
device1 = 0
device2 = 0
device3 = 0
device4 = 0
device5 = 0
state = 2

def connect_get_points():
    config.read('command.ini')
    readparam = dict(config['Device'])
    global x
    global device0,device1,device2,device3,device4,device5
    global device0address,device1address,device2address,device3address,device4address,device5address
    x = len(readparam)
    for i in range(x):
        if i==0 :
            device0 = config['Device']['Device'+str(i)]
            device0 = device0.split(',')
            device0address = device0[0]
            device0ID = device0[1]
            mycontroller0 = BAC0.device(device0address,int(device0ID),bacnet)
            client.publish("BACNET/points",str(mycontroller0.points))
            time.sleep(1)
        if i==1 :
            device1 = config['Device']['Device'+str(i)]
            device1 = device1.split(',')
            device1address = device1[0]
            device1ID = device1[1]
            mycontroller1 = BAC0.device(device1address,int(device1ID),bacnet)
            client.publish("BACNET/points",str(mycontroller1.points))
            time.sleep(1)
        if i==2 :
            device2 = config['Device']['Device'+str(i)]
            device2 = device2.split(',')
            device2address = device2[0]
            device2ID = device2[1]
            mycontroller2 = BAC0.device(device2address,int(device2ID),bacnet)
            client.publish("BACNET/points",str(mycontroller2.points))
            time.sleep(1)
        if i==3 :
            device3 = config['Device']['Device'+str(i)]
            device3 = device3.split(',')
            device3address = device3[0]
            device3ID = device3[1]
            mycontroller3 = BAC0.device(device3address,int(device3ID),bacnet)
            client.publish("BACNET/points",str(mycontroller3.points))
            time.sleep(1)
        if i==4 :
            device4 = config['Device']['Device'+str(i)]
            device4 = device4.split(',')
            device4address = device4[0]
            device4ID = device4[1]
            mycontroller4 = BAC0.device(device4address,int(device4ID),bacnet)
            client.publish("BACNET/points",str(mycontroller4.points))
            time.sleep(1)
        if i==5 :
            device5 = config['Device']['Device'+str(i)]
            device5 = device5.split(',')
            device5address = device5[0]
            device5ID = device5[1]
            mycontroller5 = BAC0.device(device5address,int(device5ID),bacnet)
            client.publish("BACNET/points",str(mycontroller5.points))
            time.sleep(1)  

def start_send_data():
    for i in range(x):
        if i==0 :
            AIdev0 = device0address + " " + "analogInput" + " " + "0" + " " + "85"
            AVdev0 = device0address + " " + "analogValue" + " " + "1" + " " + "85"
            BIdev0 = device0address + " " + "binaryInput" + " " + "2" + " " + "85"
            BOdev0 = device0address + " " + "binaryOutput" + " " + "3" + " " + "85"
            BVdev0 = device0address + " " + "binaryValue" + " " + "4" + " " + "85"
            AI0 = bacnet.read(AIdev0)
            AI0 = "dev0"+":"+str(AI0)
            client.publish("BACNET/analogInput",AI0)
            AV0 = bacnet.read(AVdev0)
            AV0 = "dev0"+":"+ str(AV0)
            client.publish("BACNET/analogValue",AV0)
            BI0 = bacnet.read(BIdev0)
            BI0 = "dev0"+":"+ str(BI0)
            client.publish("BACNET/binaryInput",BI0)
            BO0 = bacnet.read(BOdev0)
            BO0 = "dev0"+":"+ str(BO0)
            client.publish("BACNET/binaryOutput",BO0)
            BV0 = bacnet.read(BVdev0)
            BV0 = "dev0"+":"+ str(BV0)
            client.publish("BACNET/binaryValue",BV0)
#             time.sleep(1)
        if i==1 :
            AIdev1 = device1address + " " + "analogInput" + " " + "0" + " " + "85"
            AVdev1 = device1address + " " + "analogValue" + " " + "1" + " " + "85"
            BIdev1 = device1address + " " + "binaryInput" + " " + "2" + " " + "85"
            BOdev1 = device1address + " " + "binaryOutput" + " " + "3" + " " + "85"
            BVdev1 = device1address + " " + "binaryValue" + " " + "4" + " " + "85"
            AI1 = bacnet.read(AIdev1)
            AI1 = "dev1"+":"+str(AI1)
            client.publish("BACNET/analogInput",AI1)
            AV1 = bacnet.read(AVdev1)
            AV1 = "dev1"+":"+str(AV1)
            client.publish("BACNET/analogValue",AV1)
            BI1 = bacnet.read(BIdev1)
            BI1 = "dev1"+":"+ str(BI1)
            client.publish("BACNET/binaryInput",BI1)
            BO1 = bacnet.read(BOdev1)
            BO1 = "dev1"+":"+ str(BO1)
            client.publish("BACNET/binaryOutput",BO1)
            BV1 = bacnet.read(BVdev1)
            BV1 = "dev1"+":"+ str(BV1)
            client.publish("BACNET/binaryValue",BV1)
#             time.sleep(1)
        if i==2 :
            AIdev2 = device2address + " " + "analogInput" + " " + "0" + " " + "85"
            AVdev2 = device2address + " " + "analogValue" + " " + "1" + " " + "85"
            BIdev2 = device2address + " " + "binaryInput" + " " + "2" + " " + "85"
            BOdev2 = device2address + " " + "binaryOutput" + " " + "3" + " " + "85"
            BVdev2 = device2address + " " + "binaryValue" + " " + "4" + " " + "85"
            AI2 = bacnet.read(AIdev2)
            AI2 = "dev2"+":"+str(AI2)
            client.publish("BACNET/analogInput",AI2)
            AV2 = bacnet.read(AVdev2)
            AV2 = "dev2"+":"+str(AV2)
            client.publish("BACNET/analogValue",AV2)
            BI2 = bacnet.read(BIdev2)
            BI2 = "dev2"+":"+ str(BI2)
            client.publish("BACNET/binaryInput",BI2)
            BO2 = bacnet.read(BOdev2)
            BO2 = "dev2"+":"+ str(BO2)
            client.publish("BACNET/binaryOutput",BO2)
            BV2 = bacnet.read(BVdev2)
            BV2 = "dev2"+":"+ str(BV2)
            client.publish("BACNET/binaryValue",BV2)
#             time.sleep(1)
        if i==3 :
            AIdev3 = device3address + " " + "analogInput" + " " + "0" + " " + "85"
            AVdev3 = device3address + " " + "analogValue" + " " + "1" + " " + "85"
            BIdev3 = device3address + " " + "binaryInput" + " " + "2" + " " + "85"
            BOdev3 = device3address + " " + "binaryOutput" + " " + "3" + " " + "85"
            BVdev3 = device3address + " " + "binaryValue" + " " + "4" + " " + "85"
            AI3 = bacnet.read(AIdev3)
            AI3 = "dev3"+":"+str(AI3)
            client.publish("BACNET/analogInput",AI3)
            AV3 = bacnet.read(AVdev3)
            AV3 = "dev3"+":"+str(AV3)
            client.publish("BACNET/analogValue",AV3)
            BI3 = bacnet.read(BIdev3)
            BI3 = "dev3"+":"+ str(BI3)
            client.publish("BACNET/binaryInput",BI3)
            BO3 = bacnet.read(BOdev3)
            BO3 = "dev3"+":"+ str(BO3)
            client.publish("BACNET/binaryOutput",BO3)
            BV3 = bacnet.read(BVdev3)
            BV3 = "dev3"+":"+ str(BV3)
            client.publish("BACNET/binaryValue",BV3)
#             time.sleep(1)
        if i==4 :
            AIdev4 = device4address + " " + "analogInput" + " " + "0" + " " + "85"
            AVdev4 = device4address + " " + "analogValue" + " " + "1" + " " + "85"
            BIdev4 = device4address + " " + "binaryInput" + " " + "2" + " " + "85"
            BOdev4 = device4address + " " + "binaryOutput" + " " + "3" + " " + "85"
            BVdev4 = device4address + " " + "binaryValue" + " " + "4" + " " + "85"
            AI4 = bacnet.read(AIdev4)
            AI4 = "dev4"+":"+str(AI4)
            client.publish("BACNET/analogInput",AI4)
            AV4 = bacnet.read(AVdev4)
            AV4 = "dev4"+":"+str(AV4)
            client.publish("BACNET/analogValue",AV4)
            BI4 = bacnet.read(BIdev4)
            BI4 = "dev4"+":"+ str(BI4)
            client.publish("BACNET/binaryInput",BI4)
            BO4 = bacnet.read(BOdev4)
            BO4 = "dev4"+":"+ str(BO4)
            client.publish("BACNET/binaryOutput",BO4)
            BV4 = bacnet.read(BVdev4)
            BV4 = "dev4"+":"+ str(BV4)
            client.publish("BACNET/binaryValue",BV4)
#             time.sleep(1)
        if i==5 :
            AIdev5 = device1address + " " + "analogInput" + " " + "0" + " " + "85"
            AVdev5 = device1address + " " + "analogValue" + " " + "1" + " " + "85"
            BIdev5 = device1address + " " + "binaryInput" + " " + "2" + " " + "85"
            BOdev5 = device1address + " " + "binaryOutput" + " " + "3" + " " + "85"
            BVdev5 = device1address + " " + "binaryValue" + " " + "4" + " " + "85"
            AI5 = bacnet.read(AIdev5)
            AI5 = "dev5"+":"+str(AI5)
            client.publish("BACNET/analogInput",AI5)
            AV5 = bacnet.read(AVdev5)
            AV5 = "dev5"+":"+str(AV5)
            client.publish("BACNET/analogValue",AV5)
            BI5 = bacnet.read(BIdev5)
            BI5 = "dev5"+":"+ str(BI5)
            client.publish("BACNET/binaryInput",BI5)
            BO5 = bacnet.read(BOdev5)
            BO5 = "dev5"+":"+ str(BO5)
            client.publish("BACNET/binaryOutput",BO5)
            BV5 = bacnet.read(BVdev5)
            BV5 = "dev5"+":"+ str(BV5)
            client.publish("BACNET/binaryValue",BV5)
#             time.sleep(1)

#Inisialisasi MQTT
# mqttBroker ="34.121.186.105"  #localhost 
mqttBroker ="127.0.0.1"  #localhost
command = "nothing"
control = 0
writemsg = 0
size = 0
def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))
    global received,command,control
    received = str(message.payload.decode("utf-8"))
    received = received.split(",")
    command = received[0]
    control = received[1]
#     control = control.split()

def signal_control():
    global size
    control = received[1]
    control = control.split(" ")
    size = len(control)
    if size>2:
        print("entering")
        global writemsg
        if str(control[1])=="0":
#             print("im here")
            if str(control[0])=="AV":
                writemsg = str(device0address) + " analogValue" + " 1" + " presentValue " + str(control[2]) + " - 8"
                bacnet.write(writemsg)
            if control[0]=="BO":
                writemsg = str(device0address) + " binaryOutput" + " 3" + " presentValue " + control[2] + " - 8"
                bacnet.write(writemsg)
            if control[0]=="BV":
                writemsg = str(device0address) + " binaryValue" + " 4" + " presentValue " + control[2] + " - 8"
                bacnet.write(writemsg)
        elif str(control[1])=="1":
            if str(control[0])=="AV":
                writemsg = str(device1address) + " analogValue" + " 1" + " presentValue " + str(control[2]) + " - 8"
                bacnet.write(writemsg)
            if control[0]=="BO":
                writemsg = str(device1address) + " binaryOutput" + " 3" + " presentValue " + control[2] + " - 8"
                bacnet.write(writemsg)
            if control[0]=="BV":
                writemsg = str(device1address) + " binaryValue" + " 4" + " presentValue " + control[2] + " - 8"
                bacnet.write(writemsg)
        elif str(control[1])=="2":
            if str(control[0])=="AV":
                writemsg = str(device2address) + " analogValue" + " 1" + " presentValue " + str(control[2]) + " - 8"
                bacnet.write(writemsg)
            if control[0]=="BO":
                writemsg = str(device2address) + " binaryOutput" + " 3" + " presentValue " + control[2] + " - 8"
                bacnet.write(writemsg)
            if control[0]=="BV":
                writemsg = str(device2address) + " binaryValue" + " 4" + " presentValue " + control[2] + " - 8"
                bacnet.write(writemsg)
        elif str(control[1])=="3":
            if str(control[0])=="AV":
                writemsg = str(device3address) + " analogValue" + " 1" + " presentValue " + str(control[2]) + " - 8"
                bacnet.write(writemsg)
            if control[0]=="BO":
                writemsg = str(device3address) + " binaryOutput" + " 3" + " presentValue " + control[2] + " - 8"
                bacnet.write(writemsg)
            if control[0]=="BV":
                writemsg = str(device3address) + " binaryValue" + " 4" + " presentValue " + control[2] + " - 8"
                bacnet.write(writemsg)
        elif str(control[1])=="4":
            if str(control[0])=="AV":
                writemsg = str(device4address) + " analogValue" + " 1" + " presentValue " + str(control[2]) + " - 8"
                bacnet.write(writemsg)
            if control[0]=="BO":
                writemsg = str(device4address) + " binaryOutput" + " 3" + " presentValue " + control[2] + " - 8"
                bacnet.write(writemsg)
            if control[0]=="BV":
                writemsg = str(device4address) + " binaryValue" + " 4" + " presentValue " + control[2] + " - 8"
                bacnet.write(writemsg)
        elif str(control[1])=="5":
            if str(control[0])=="AV":
                writemsg = str(device5address) + " analogValue" + " 1" + " presentValue " + str(control[2]) + " - 8"
                bacnet.write(writemsg)
            if control[0]=="BO":
                writemsg = str(device5address) + " binaryOutput" + " 3" + " presentValue " + control[2] + " - 8"
                bacnet.write(writemsg)
            if control[0]=="BV":
                writemsg = str(device5address) + " binaryValue" + " 4" + " presentValue " + control[2] + " - 8"
                bacnet.write(writemsg)       

client = mqtt.Client("whatt")
client.connect(mqttBroker) 

#Inisialisasi BACNET
bacnet = BAC0.connect()

#Subscribe Data
client.loop_start()
# client.subscribe("topic/state")
# client.on_message=on_message 
# client.subscribe("topic/settingTemp")
# client.on_message=on_message 
client.subscribe([("BACNET/check",0)])
client.on_message=on_message
time.sleep(5)

while True:
    #print(control)
    #print(command)
    #print(size)
    if command=="check":
        mstp = bacnet.whois()
        client.publish("BACNET/status",str(mstp))
    if command=="connect":
        connect_get_points()
        command="nothing"  
    if command=="start":
        start_send_data()
        signal_control()
    time.sleep(1)