''' Demo P2P Receive to control onbaord relay =>

  --------------- 4CH/8CH -------------------
   | GP18     | Relay 1 | Relay interface |
   | GP19     | Relay 2 | Relay interface |
   | GP20     | Relay 3 | Relay interface |
   | GP21     | Relay 4 | Relay interface |
  ---------------- 8CH ----------------------
   | GP22     | Relay 5 | Relay interface |
   | GP23     | Relay 6 | Relay interface |
   | GP16     | Relay 7 | Relay interface |
   | GP17     | Relay 8 | Relay interface |

'''
# Import required library modules
from machine import UART, SPI, Pin
import time
from time import sleep
import vga1_bold_16x32 as font

# UART communication between RP2040 and RAK3172
uart = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))

# Initialize relays, 
relay1 = Pin(18, Pin.OUT)
relay2 = Pin(19, Pin.OUT)
relay3 = Pin(20, Pin.OUT)
relay4 = Pin(21, Pin.OUT)

# Optional: ensure all relays are off at start
relay1.off()
relay2.off()
relay3.off()
relay4.off()


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
    sleep(1)
    response = uart.readline()
    sleep(0.1)
    return response

def p2p_setup():
    send_command('AT')  # Test command
    send_command('AT+NWM=0')  # Set to P2P mode
    send_command('AT+PRECV=0')  # Stop previous receive if running
    send_command('AT+P2P=903000000:7:0:0:14:5')  # Set P2P params
    print(send_command('AT+P2P=?'))  # Confirm settings

def activate_p2p_receive():
    send_command('AT+PRECV=65535')  # Start P2P RX mode

def parse_received_data(response):
    try:
        if isinstance(response, bytes):
            response = response.decode('utf-8', 'ignore')
            print(f"Module Response: {response}")

        if "+EVT:RXP2P" in response:
            parts = response.strip().split(":")
            if len(parts) >= 4:
                raw_data = parts[-1].strip()
                print("Received Data Payload:", raw_data)
                print("RSSI:", parts[2], "dBm")

                # Control relays based on payload
                if raw_data == "01":
                    relay1.on()
                    print("Relay 1 Activated")
                elif raw_data == "02":
                    relay2.on()
                    print("Relay 2 Activated")
                elif raw_data == "03":
                    relay3.on()
                    print("Relay 3 Activated")
                elif raw_data == "04":
                    relay4.on()
                    print("Relay 4 Activated")
                else:
                    print("Unknown command:", raw_data)

            global rx_mode
            rx_mode = 0
            sleep(1)

    except Exception as e:
        print("Parsing error:", e)

# Initial setup
p2p_setup()

rx_mode = 1
print("Waiting...")
sleep(1)
activate_p2p_receive()

# Main loop
while True:
    if uart.any():
        response = uart.readline()
        print(response)
        parse_received_data(response)

    if rx_mode == 0:
        activate_p2p_receive()
        rx_mode = 1
        print("Rx Mode Activated")
        print("Waiting!", end="")

    sleep(0.2)
    print(".", end="")
