'''
Code to Get/Set Device EUI, AppEUI (Join EUI), and AppKey
'''

from machine import UART, SPI, Pin
import time
from time import sleep

# Serial communication interface between RP2040 and RAK3172
uart = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))

# Global variables to hold parsed values
DEVEUI_ = ''
APPEUI_ = ''
APPKEY_ = ''

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
    uart.write(command + '\r\n')
    time.sleep(0.2)

def module_response_check():
    global DEVEUI_, APPEUI_, APPKEY_
    while uart.any():
        response = uart.readline()
        try:
            if isinstance(response, bytes):
                response = response.decode('utf-8', 'ignore').strip()
                print(f"Module Response : {response}")

                # Parse for known identifiers
                if response.startswith("AT+DEVEUI="):
                    DEVEUI_ = response.split('=')[1]
                elif response.startswith("AT+APPEUI="):
                    APPEUI_ = response.split('=')[1]
                elif response.startswith("AT+APPKEY="):
                    APPKEY_ = response.split('=')[1]

        except Exception as e:
            print("Parsing error:", e)

def get_IDkey():
    # Get DEVEUI, APPEUI, APPKEY
    send_command('AT+DEVEUI=?')
    module_response_check()

    send_command('AT+APPEUI=?')
    module_response_check()

    send_command('AT+APPKEY=?')
    module_response_check()

    # Final neatly formatted summary
    print("\n========== LoRaWAN Node Credentials ==========")
    print(f"DEVEUI  : {DEVEUI_}")
    print(f"APPEUI  : {APPEUI_}")
    print(f"APPKEY  : {APPKEY_}")
    print("==============================================")

def set_IDkey(deveui, appeui, appkey):
    
    send_command(f"AT+DEVEUI={deveui}")
    time.sleep(0.2)
    
    send_command(f"AT+APPEUI={appeui}")
    time.sleep(0.2)
    
    send_command(f"AT+APPKEY={appkey}")
    time.sleep(0.2)


# ----- Main -----
send_command('AT')
module_response_check()

# Put in LoRaWAN mode
send_command('AT+NWM=1')
module_response_check()

get_IDkey()  # to get stored credentials

# uncomment to update new credentials,
'''
DEVEUI_ = 'BC1F09FFFE1AF310'    				# replace with your Device EUI
APPEUI_ = 'BC1F09FFF9153170'					# replace with your APPEUI
APPKEY_ = 'BC1F09FFFE1AF318AC1F09FFF9153170'	# replace with your APPKEY
set_IDkey(DEVEUI_, APPEUI_, APPKEY_)

get_IDkey()  # verify again
'''