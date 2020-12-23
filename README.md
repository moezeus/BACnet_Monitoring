# BACnet_Monitoring
SCADA Final Assignment Repository - Commercial AC BACnet Protocol Simulation (IoT Gateway for Monitoring and Control)

By : Husnul Amri & Rizal Fariz

Welcome!

## Preface

This repository is aimed to get sensor data from local BACnet networks and also control the BACnet devices, then send it to Google IoT Core services using MQTT bridge. It's hard, but in order to make it (more) simply, we are try to use node-red as the gateway to the IoT Core, and also as the dashboard display. 
There are some advantages of using node-red for this project : (1) Good Community Support; (2) More understandable and drag & drop node; (3) Included with customable GUI ; (4) It could support some programming language inside the function nodes, also execute them; (4) Free and Lightweight (at least for this project); and maybe many more. 
We are using BACnet protocol simulator from [ScadaEngine](http://www.scadaengine.com/software6.html) (of course, we are using trial version, but install it to virtual machine, so, when it expired, we flash the virtual machine and reinstall) to get the BACnet data. The simulator was awesome, and has customable device/device data/device properties, very good start to learn about BACnet networks. When we add some devices and its objects, it will lied under UDP/IP (the simulator itself) and MS/TP (BACnet Objects), so we are using [Python BAC0](https://bac0.readthedocs.io/en/latest/getstarted.html) to read the data, and then send it to node-red using local MQTT [Mosquitto](https://mosquitto.org/). At last, of course this repository is maybe full of bugs, and need many code optimization, but actually, for some limited use, "it just works!". Enjoy !

## IoT Architecture
In general, IoT Architecture consist of a Device (send or receive some data/command), Gateways (Connector between the cloud and devices, or with the edge devices) and then the Cloud itself (receive the data/command from the enterprises). 

![IoT General Architecture](/BACnet_Pictures/IoT_General.png)

For this project, we are defined the Bacnet Simulator from the [ScadaEngine](http://www.scadaengine.com/software6.html) as the devices, and then Python and node-red as the edge devices and finally [Google IoT Core](https://cloud.google.com/iot/docs/quickstart) as the Cloud Services.

![BACnet Monitoring Architecture](/BACnet_Pictures/BACnet_Architecture.PNG)

## Requirements
In order to use the code in this Repository, you need to install: 
* Install [node-red](https://nodered.org/docs/getting-started/local) locally
* Install Python 3.7 environment. Here, we are using [Anaconda Environment](https://docs.anaconda.com/anaconda/install/)
* Install [Mosquitto MQTT](https://mosquitto.org/) to send data locally
* Install BACnet simulator from  [ScadaEngine](http://www.scadaengine.com/software6.html), you can install it on the other computer (Windows OS) which connected on same local network with your main device. OR, you can use [Oracle Virtual Machine](https://www.oracle.com/virtualization/technologies/vm/downloads/virtualbox-downloads.html) so you can configure it on the same devices (although, this would rapidly slow down your system), choose one that match your condition. 
* (OPTIONAL) Install [Cygwin](https://cygwin.com/install.html) if you want to have some connection to the Google IoT Core, it is used to generate open SSL Certificate easier. 

## Use the code Locally
if all of the requirements have been fulfilled, the next step for local access is: 
* clone this repository using `git clone` or download this repository code, place it on your project directory (if youre about to use jupyter lab in default, place it under (C:Users/$User/Your Project Folder)).
```
git clone https://github.com/moezeus/BACnet_Monitoring.git
```
* Open your Jupyter Lab, using anaconda prompt, and then type `jupyter lab`, it will automatically opened in your default browser. open your project directory. 
* Install some important lib : 
```
pip install configparser
pip install BAC0
pip install paho-mqtt
```
  If it ask for admin user, you can open anaconda prompt in administrator and then run those command
* Run the python by using the jupyter lab terminal, type `python Tubes_BACNET.py`. if you severe some error because of library/module dependencies, install it based on the missing modules. if you got error/something referred to `google-cloud-iotcore device node`, check the `Google Iot Core Integration sections` or simply disable the node.  
* Open your command prompt, and then type `node-red`, to open the node-red, and then it would opened automatically in your default browser.  
* import the JSON file on the node-red folder, to get BACnet monitoring edge and gateway services. and then press the `Deploy` button. After the deploy process, you would get some errors because of missing node modules. notes the missing modules, and then find it on `manage palletes` menu, then install it. 
* After the modules are installed (no errors on deploy), you can then open the UI dashboard on `localhost:1880/ui/`. the UI is set for `1366*768` resolution, if your resolution differs, the UI may not shown in a good orders.
* Turn on your BACnet simulator (either on other computers in same networks or on the virtual machine), and add your device objects with this criteria: (in order to meet the Python code)
```
Analog Input --> Instance 0
Analog Value --> Instance 1
Binary Input --> Instance 2
Binary Output -> Instance 3
Binary Value --> Instance 4
```
  Actually, you are free to choose the objects instance, but make sure to adjust it on the Python Code. this criteria is used if you are about to use our code purely. 
* On the Node-red Home UI, press the `WHO IS?` button, and it will reveal your bacnet ID and devices objects. stop the who is command, and then notes the devices object adresses (something with `20:0x20........` or MS/TP adresses). open the command.ini using notepad, and then fills the device object addresses and instance, based on example that exists on the file. finally, save it. (notes: adjust the file based on the how much device found on the networks, if only one, remove/delete the other devices)

![Home GUI](/BACnet_Pictures/GUI_main.png)

* after that, press the `CONNECT` button, if the process succesfully running, you will look at the device objects printed onto the table, otherwise, check the jupyter lab terminal to look at the error message.
* if the Connect process passed, you can proceed to the display page, by pressing the `NEXT` button.

![Display Page](/BACnet_Pictures/GUI_display.png)

* when everythings is ready, press the `START` button to start your data display. if you want to send command (currently available for BO,BV and AV), you can type example: `AV 0 124` <-- AV is the analog value, 0 is instance and 124 is the value to send. You can check it on the BACnet simulator to know whether it has changed or not. 

## Google IoT Core Integration
To connect the data from the node-red to the IoT Core, you need to: 
Best procedure documented on google IoT Core [documentation](https://cloud.google.com/iot/docs/quickstart), but we`ll try to highlight the general procedures.
* Create project on your cloud console, make sure to enable the Google IoT Core API/Services
* On the IoT Core (under the Big Data section), choose IoT Core and create your registry, or follow the instructions on this [tutorial](https://www.opc-router.com/google-gcp-iot-core-mqtt-connection/), you can skip the OPC Router step. 
* After creating registry and your own pub/sub topics, you can create your own devices. upon creating the devices, on the security/certificate, you need to read about how to [creating public-private RSA256 keys](https://cloud.google.com/iot/docs/how-tos/credentials/keys), and to make it simply, you can use the Cygwin that has been installed before, and use the command on that link. after the credential has been created, upload the public keys to the device you`ve been created. 
* After device has been created, take a look at the node-red, and enable the iot-core node (only if it previously disabled), and then edit the broker data based on your IoT Core configuration. you can see if the node is labelled connected if the configuration is match. 
* then, you can test to send send some data from the IoT Core. open the device under the IoT core registry, then click send command (you can choose text or base64 command) then click `send`. check on the node-red debug message, normally, it would print the command you`ve been send on the msg node, or you can check it on the command prompt message also. 
* to send the data, you need to create some subscription point to make sure whether the data that send to the IoT Core from node red has been received or not. to do so, just follow this [tutorial](https://www.opc-router.com/google-gcp-iot-core-mqtt-connection/) on the very last step, adjust it based on your projects. Finally, try to send data using inject node (you can edit the injected string/other value), then check it on your IoT Core. Of course, we can change the data source to the BACnet output or the others easily, and catch the input to control something else.
* Also, this can be integrated to SQL and to Google Data Studio or the others, but for now, our works covered till this step, and maybe the completion will be done next over time. 

Thanks!!

## Special Thanks : 
This works is supported by Lab-ME Teknik Fisika, Fakultas Teknologi Industri, Institut Teknologi Bandung. 
 


