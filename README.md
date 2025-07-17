# GatePi_LoRaWAN_4CH/8CH_Software

<img src="https://github.com/sbcshop/GatePi_LoRaWAN_Software/blob/main/images/feature_banner.png" width="" height="">

GatePi Powered by RP2040 microcontroller and RAK3172 LPWAN module to support both LoRaWAN and P2P mode to build long range network. You can easily switch onboard module into LoRaWAN Mode for connecting with server platforms like The Things Network (TTN), Chirpstack, Actility, etc. or P2P Mode to implement your own customized long-range LoRa network quickly.

This GitHub provides getting started instructions for GatePi LoRaWAN 4CH/8CH.

### Features:
- Powered by RP2040 microcontroller equipped with RAK3172 LoRaWAN Node
- This module complies with Class A, B, & C of LoRaWAN 1.0.3 specifications. 
- It can easily connect to different LoRaWAN server platforms like TheThingsNetwork (TTN), Chirpstack, Helium, etc.
- It also supports LoRa Point-to-Point (P2P) communication mode which helps you in implementing your own customized long-range LoRa network quickly. 
- Sub-GHz frequency bands (EU868, US915, AS923, etc.)
- LoRaWAN activation by OTAA/ABP
- AT Command support (for quick configuration via UART)
- Onboard 4/8 Channel relay with NO, COM, NC breakout using screw terminal for easy connection
- Jumper selection to switch Type-C access between RP2040 and RAK3172
- Power and Relay status LED for visual indication of activity 
- Boot button for programming for RP2040
- Onboard Screw terminal for external power 5V
- SMA antenna connector for connecting Rod Antenna for increased range and stability


## Hardware Overview

### Pinout
<img src="https://github.com/sbcshop/GatePi_LoRaWAN_Software/blob/main/images/pinout.png"  width= "" height= "">

### Interfacing Details
Following GPIOs of RP2040 interfaced with onboard hardware components,

   | RP2040 | Hardware | Function |
   |---|---|---|
   | GP0/TXD0 | LoRaWAN Module_RX | UART Communication interface |
   | GP1/RXD0 | LoRaWAN Module_TX | UART Communication interface |
   | GP8      | Module Reset | RAK3172 module reset pin |
   | GP18     | Relay 1 | Relay interface |
   | GP19     | Relay 2 | Relay interface |
   | GP20     | Relay 3 | Relay interface |
   | GP21     | Relay 4 | Relay interface |
   | GP22     | Relay 5 | Relay interface |
   | GP23     | Relay 6 | Relay interface |
   | GP16     | Relay 7 | Relay interface |
   | GP17     | Relay 8 | Relay interface |
   

### Getting Started with GatePi LoRaWAN 4CH/8CH

### Step 1: Boot Firmware installation 
- Mostly hardware will have boot firmware preinstalled so you can skip and jump to next step.
- In case you want then Press and hold onboard BOOT button and plug dongle into the USB port of your PC/Laptop. Release the BOOT button once dongle is connected to system. Also, make sure jumper setting as shown below,

  <img src="https://github.com/sbcshop/GatePi_LoRaWAN_Software/blob/main/images/RP2040_USBaccess.jpg"  width="423" height="272">

- It will mount as a Mass Storage Device called RPI-RP2.

  <img src="https://github.com/sbcshop/LoRaWAN_RP2040_Dongle_Software/blob/main/images/mass_storage_rp.png"  width= "604" height= "371">

- Download this complete github which contains firmware and example codes,

  <img src="https://github.com/sbcshop/LoRaWAN_RP2040_Dongle_Software/blob/main/images/github_download.png" width="382" height="282">
  
- Drag and drop the [MicroPython UF2 file](https://github.com/sbcshop/GatePi_LoRaWAN_Software/blob/main/firmware.uf2) onto the RPI-RP2 volume. Your Pico RP2040 will reboot. You are now running MicroPython.

  <img src="https://github.com/sbcshop/Micro_RP2040/blob/main/Images/firmware_install.gif"  width= "720" height= "382">

### Step 2: Testing and Running Examples
-  Download and install [Thonny IDE](https://thonny.org/) from official site.
-  To try any demo examples or LoRaWAN/P2P operation codes having communication between RP2040 chip and RAK3172, make sure jumper setting as shown below:
  
   <img src="https://github.com/sbcshop/GatePi_LoRaWAN_Software/blob/main/images/RP2040_USBaccess.jpg" width= "352" height= "189">
  
-  Write simple code in Thonny IDE, select MicroPython board with suitable com port (maybe different in your case). Then click on run button
   
   <img src="https://github.com/sbcshop/Micro_RP2040/blob/main/Images/test_run_code.gif" width= "720" height= "382">
-  So, now device ready you can proceed to try demo examples provided [here](https://github.com/sbcshop/GatePi_LoRaWAN_Software/tree/main/examples) in github for **P2P/LoRaWAN** operations.

  
## RAK3172 Module Standalone
* You can access RAK3172 module directly. For this remove Pico from header and change jumper selection to USB-RAK side as shown below,
  
  <img src="https://github.com/sbcshop/GatePi_LoRaWAN_Software/blob/main/images/LoRaWAN_Module_USBaccess.jpg" width="447" height="254">

* Connect device to PC/laptop using Type C. Now you can follow steps mentioned [here](https://github.com/sbcshop/LoRaWAN_Breakout_Software) to use RAK3172 module standalone like breakout for changing configuration or [Firmware update](https://github.com/sbcshop/LoRaWAN_Breakout_Software/blob/main/documents/Firmware%20Update%20Procedure%20with%20WisToolBox.pdf).

  
## Resources
  * [Hardware Files](https://github.com/sbcshop/GatePi_LoRaWAN_Hardware) - Schematic, Step Files, 3D, etc.
  * [RAK3172 AT Command Reference](https://docs.rakwireless.com/product-categories/software-apis-and-libraries/rui3/at-command-manual/)
  * [CH340 Driver Installation Guide](https://github.com/sbcshop/NFC_Module/blob/main/documents/CH340%20Driver%20installation%20steps.pdf)
  * [MicroPython getting started for RPi Pico/Pico W](https://docs.micropython.org/en/latest/rp2/quickref.html)
  * [Pico W Getting Started](https://projects.raspberrypi.org/en/projects/get-started-pico-w)
  * [RP2040 Datasheet](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf)

## Related Products  

  * [LoRaWAN for Raspberry Pi Pico](https://shop.sb-components.co.uk/products/lorawan-for-raspberry-pi-pico)
  
  * [LoRaWAN RP2040 USB Dongle](https://shop.sb-components.co.uk/products/lorawan-rp2040-usb-dongle)

  * [LoRaWAN Breakout Board](https://shop.sb-components.co.uk/products/lorawan-breakout)
  
  * [LoRaWAN HAT for Raspberry Pi](https://shop.sb-components.co.uk/products/lorawan-hat-for-raspberry-pi)
  
  * [LoRaWAN Gateway HAT for Raspberry Pi](https://shop.sb-components.co.uk/products/lorawan-gateway-hat)
   

## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
