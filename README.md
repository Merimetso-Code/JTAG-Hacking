# JTAG Hacking

The Joint Test Action Group (JTAG) name is associated with the IEEE 1149.1 standard 
entitled Standard Test Access Port and Boundary-Scan Archi- tecture. The goal fo this 
standard is to allow for testing of the integrated circuit to ensure that the core 
logic and boundary connections are woking correctly. Prior to the creation and 
adoption of the JTAG standard and bed of nails we used to test the boundary connections. 
But as boundary connections got smaller and smaller so a new approach was needed and 
hence the creation of the JTAG standard. 

The JTAG interface connects to an on-chip Test Access Port (TAP) that implements a 
stateful protocol to access a set of registers. The registers allow for the testing 
of the internal core logic of an integrated circuit as well and the boundary pins 
that connect the integrated circuit to the outside world. The JTAG standard defines 
the following pins for testing.
  - TDI - Test Data In.
  
  - TDO - Test Data Out.
  
  - TCK - Test Clock.
  
  - TMS - Test Mode Select.
  
  - TRST - Test Reset (Optional).

The JTAG standard makes use of of various registers.
  - Instruction Registers - This defines the mode in which the Boundary- Scan Data Registers will operate. The instruction register holds the current instruction. Its content is used by the TAP controller to decide what to do with signals that are received. Most commonly, the content of the instruction register will define to which of the data registers signals should be passed. In fact all Boundary-Scan instructions set operational models that place a selected register between the TDI and TDO.
  
  - ByPass Register - This is a single-bit register that passes information from TDI to TDO. It allows other devices in a circuit to be tested with minimal overhead.
  
  - Device Identification Register (IDCODE) - This register contains the ID code and revision number for the device. This information allows the device to be linked to its Boundary Scan Description Language (BSDL) file. The file contains details of the Boundary Scan configuration for the de- vice. The Device Identification Register is composed of three elements as follows. We can use this information and identify the Manufacturer of the device and the device device itself.
  
  - Boundary Register - This is the main testing data register. It is used to move data to and from the I/O pins of a device.
## JTAG Hacking Tools in Python
The following are the tools that we can use when hacking a UART connection on a embedded system.
  - jlookup.py

## jlookup
This is Device Identification Register lookup and decode utility. That given the valie of the
Device Identification Register can identify the Manufacturer, Part and version number of the JTAG enabled device.
The program has been developed by Merimetso. This utility has a built in manual page.
```sh
$ python jlookup.py -h
Program: jlookup.py - Version: 1.0 - Author: ab@merimetso.net - Date: 2020/10/21

USAGE: jlookup.py [-h] [-t bin|dec|hex] IDCODE

 Optional Arguments:
    -h    Show this help message and exit.
    -t    The type of the JTAG IDCode. The type as are follows.
             bin - The IDCODE is expressed as a binary number.
             dec - The IDCODE is expressed as a decimal number.
             hex - The IDCODE is expressed as a hexidecimal number.
         If the -t option is NOT specified it id assumed that the IDCODE is
         expressed as a hexidecimal number.

EXAMPLE:
        $ python jlookup.py -t hex 0x4caf0477

$ 
```
The program/utility can be involved at the command line and allows us to specify/decode 
the value of the Device Identification Register (IDCODE)  in Hexadecimal, Decimal 
and Binary formats.
```sh
$ python jlookup.py -t hex 0x4caf0477 
Program: jlookup.py - Version: 1.0 - Author: ab@merimetso.net - Date: 2020/10/21

The IDCODE is := 01001100101011110000010001110111 / 0x4caf0477
 -> The Manufacturer ID is : 01000111011 / 0x23b ( ARM Ltd. )
 -> The Part ID is         : 1100101011110000 / 0xcaf0
 -> The Version Number is  : 0100 / 0x4

$
```
## License
  - MIT

