''' Simple Data Send on TTN Server

To Register Setup and Register Gateway on TTN Server :
https://github.com/sbcshop/LoRaWAN_Gateway_HAT_Software

To create application & register endnode on TTN Server checkout instructions:
https://github.com/sbcshop/LoRaWAN_Breakout_Software/tree/main/lorawan_application_TTN

To get/set LoRaWAN Endnode credentials using code => 
https://github.com/sbcshop/GatePi_LoRaWAN_Software/blob/main/examples/lorawan_endnode_config.py

'''


from machine import Pin,UART
from time import sleep
import utime, time

uart = UART(0,baudrate = 115200,tx = Pin(0),rx = Pin(1))

def module_reset():
    lwanRST = Pin(8, Pin.OUT)  # RAK3172 Reset pin
    lwanRST.on()
    sleep(0.2)
    lwanRST.off()
    sleep(0.2)
    lwanRST.on()
    print("Module Reset Done!")
    sleep(1)

#module_reset() #required only once if module not responding or join issue
    
def send_command(command): #Simple AT command
    uart.write(command+'\r\n')
    response = uart.read()
    #print(response)
    global counter
    counter = 0
    if counter:
        print(response)
    else :
        counter = 1
    sleep(1)             

def check_join_status(timeout=5000):
    prvmills = utime.ticks_ms()
    send_command('AT+NJS=?')
    while (utime.ticks_ms() - prvmills) < timeout:
        #send_command('AT+NJS=?')
        if uart.any():
            response = uart.readline()
            if 'AT+NJS=1' in response:
                #print(response)
                print("Already Connected to Network")
                return True
        else :
            print(".",end=' ')
        sleep(0.2)
        
    return False


def join_network():
    attemptCnt = 0

    while status != True:
        if uart.any():
            response = uart.read()
            print(response)
            if '+EVT:JOINED' in response or 'AT+NJS=1' in response:   # join status check commands
                print("Connected to Network")
                flag = 1
                print(response)
                break
        else:
            flag = 0
            print(".",end=' ')
            attemptCnt = attemptCnt + 1
            if attemptCnt > 20:
                break
        sleep(1)

    if attemptCnt > 20 :
        print("Join Failed! Restart Node")
        sleep(5)
        while True:
            pass
        
def send_data(port, data):
    portVal = str(port) #convert into string
    dataVal = str(data)
        
    print("To send Data: ", dataVal)
    
    if (len(dataVal) % 2 == 0): # payload byte needs to be even
        # Concatenate the components to form the command string, sample #AT+SEND='port:data' e.g. 'AT+SEND=2:3456'
        cmd = f'AT+SEND={portVal}:{dataVal}'
    else :
        cmd = f'AT+SEND={portVal}:{0}{dataVal}'
    
    #print("Sending cmd:", cmd)
    if status:
        send_command(cmd)
        print("Data Sent!")
    else :
        print("LNS connection Lost! Restart Node")
        
    
def upload_interval(interval):
    for i in range(interval):
        pass
        sleep(60)

print("Checking LNS Connection")

flag = 0
status = check_join_status()
#print("Join Status: ", status)

if status != True:
    print("\nNOT JOINED! Try Connecting...")
    sleep(1)
    flag = 0
    
    # NWM = 0 - P2P mode, 1 - LoRaWAN Mode
    res = send_command('AT+NWM=1')
    
    send_command('AT+JOIN=1:0:10:8')
    join_network()

while True:
    print("\nUploading Data...!")
    send_data(1, "34") 	# pass => (port, data)
    sleep(20) # time in sec
    #upload_interval(1) # pass time in min

 


