''' P2P Transmit Demo code '''

# Import required library modules
from machine import UART, SPI, Pin
import time
from time import sleep
import vga1_bold_16x32 as font

# UART communication between RP2040 and RAK3172
uart = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))

def module_reset():
    lwanRST = Pin(8, Pin.OUT)
    lwanRST.on()
    sleep(0.1)
    lwanRST.off()
    sleep(0.1)
    lwanRST.on()
    print("Module Reset Done!")

module_reset()

def send_command(command):  
    uart.write(command+'\r\n')
    time.sleep(0.1)
    response = uart.readline()
    #print(response)
    return response

def p2p_setup():
    # command sequence require to put RAK3172 node module in P2P Receive
    res = send_command('AT')  # Simple Module response test command
    #print(res)
    
    # NWM = 0 - P2P mode, 1 - LoRaWAN Mode
    res = send_command('AT+NWM=0')
    #print(res)
    
    # Stop if any Previous receive command execute to avoid busy message
    res = send_command('AT+PRECV=0')
    #print(res)
    
    # To enable or disable P2P encryption, 0 - for disable and 1 - for enable
    res = send_command('AT+ENCRY=0')
    #print(res)
    
    #Set P2P Parameters settings, required only once
    res = send_command('AT+P2P=903000000:7:0:0:14:5')
    print(res)
    
    res = send_command('AT+P2P=?')  # to confirm if setting done
    print(res)
    

def module_response_check():
    while uart.any():
        response = uart.readline()
        try:
            # Convert bytes to string if needed
            if isinstance(response, bytes):
                response = response.decode('utf-8', 'ignore')
                print(f"Module Response : {response}")
                if "+EVT:TXP2P" in str(response):
                    print("Transmit Success")
                    sleep(1)
                    
        except Exception as e:
            print("Parsing error:", e)


    
p2p_setup()		# Command sequence to setup for P2P transmit mode

print("P2P Tx Demo")
last_time = time.ticks_ms()  # get current time in ms

while 1:
    send_command('AT+PSEND=1548')  # send payload data as byte (even count only allowed)
    module_response_check()
        
    time.sleep(0.5)
