import serial.tools.list_ports
serialInst = serial.Serial()

portsList = []
ports = serial.tools.list_ports.comports()
print('all ports: ')

for onePort in ports: 
    portsList.append(onePort)
    # print(str(onePort))
    print((onePort.device))
    # print(type(onePort))

# import sys
# sys.exit()

# val = input('Select Port: COM')
# serialInst.baudrate = 9600
serialInst.baudrate = 115200
# serialInst.port = "COM8" 
# serialInst.port = "COM" + str(val)
serialInst.port = portsList[0].device


try: 
    serialInst.open()
except Exception as e:
    print(e) 
    print('COM not setup correctly')
