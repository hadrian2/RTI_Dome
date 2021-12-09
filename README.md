# **Hadrian Doromal Worklog**

## 9/5/2021: Officially Joined Team 11!
* Lightly researched Reflectance Transformation Imaging
* Exchanged information with groupmates

## 9/6/2021: Project Approved!
* Researched existing RTI apparatuses for ideas
  * [Scope D50](https://broncolor.swiss/products/scope-d50?gclid=EAIaIQobChMI7PHh9pSq8gIVht7ICh2UtwItEAMYASAAEgKtlvD_BwE)
  * [RTI-Dome](https://www.rti-dome.com/)
  * [Tim Zaman Dome](http://www.timzaman.nl/rti-dome)
 
## 9/8/2021: Discussed Design Ideas
* Nothing concrete yet, maybe some sort of retractable umbrella design?
* Basic ideas for block diagram modules

## 9/9/2021: Continued Design Discussion
* Sketched out rough umbrella design


  ![Image](https://github.com/hadrian2/RTI_Dome/blob/main/Umbrella_Sketch.jpg)
* Sketched out rough block diagram


  ![Image](https://github.com/hadrian2/RTI_Dome/blob/main/First_Block_Sketch.jpg)
  
## 9/16/2021: Proposal Write-up
* Met with group over Discord while they met in person
  * Outlined high level requirements, block requirements, etc.

## 9/21/2021: First TA Meeting
* Met with Evan to talk about our design
* Aiming to have a schematic by Friday

## 9/23/2021: Parts Discussion and Schematic Considerations
* Began looking into Microcontrollers, no decisions made yet
* Began Researching LED drivers and other circuit parts
  * [Shift Register](https://www.digikey.com/en/products/detail/texas-instruments/SN74HC165AN/12124771) 
  * [LED Driver Options](https://www.digikey.com/en/products/filter/pmic-led-drivers/745?s=N4IgTCBcDaIDYFMAmACJAnAlgNwekAugL5A)
  * [Transistor Options](https://www.digikey.com/en/products/filter/transistors-bipolar-bjt-single/276?s=N4IgTCBcDaIHYAc4AIAuAnAhnAzgSx1QHt0QBdAXyA)
  * [Camera Connector Jack](https://www.digikey.com/en/products/detail/cui-devices/SJ1-3533/738695)
* Still need to find a fuse and power connection along with other things
* Need to find out how to implement UART into our design

## 9/25/2021: Microcontroller Research
* Going with [ATmega48A](https://ww1.microchip.com/downloads/en/DeviceDoc/ATmega48A-PA-88A-PA-168A-PA-328-P-DS-DS40002061B.pdf) microcontroller for now.
* Alex began designing schematic

![Image](https://github.com/hadrian2/RTI_Dome/blob/main/First_Schematic.png)

## 9/26/2021: Continued Parts Research and Schematic Design
* Looked through multiple LED drivers and settled on [this](https://www.st.com/resource/en/datasheet/led5000.pdf) one for now
* [LED Bulbs](https://www.ledtronics.com/Clearance/?p=MR16-42-SIW-001M)
* [USB to UART](https://www.digikey.com/en/products/detail/digilent-inc/410-212/4090089)

## 9/27/2021: Continued Parts Research and Schematic Design
* Light research on led5000 driver datasheet to try to understand it
* Alex updated our schematic with new parts, Evan recommended [TLC5940 LED driver](https://www.ti.com/product/TLC5940) instead of led5000
* Jack working on Autocad designs for the dome

![Image](https://github.com/hadrian2/RTI_Dome/blob/main/Schematic_2.png)

* Decided on these [new LED bulbs](https://www.ledtronics.com/Clearance/?p=MR11-30-TPW-012AM) with lower current draw to make things easier for us
* Think we're ready to order parts!

## 9/28/2021: Prep for Design Doc Check + misfortune
* LEDs were out of stock, we decided to go with [these](https://www.superbrightleds.com/moreinfo/reflector-bulbs/mr11-led-landscape-light-bulb-20w-equivalent-240-lumens/2842/9418/) instead
* Jack put together slides for the DDC


## 9/29/2021: LED Sockets
* Found [sockets](https://www.superbrightleds.com/moreinfo/household-bulb-sockets-adapters/mr16-socket-mr11-bi-pin-socket-for-gu53g4gx53gy635gz4-base-bulbs/499/2027/?accessory_of=2842-all_accessories) for our LEDs

## 9/30/2021: Design Doc
* Flushing out our design doc
* Evan gave us the OK to submit design doc tomorrow evening since we just figured out all of our parts
* Jack continuing to work on CAD
* To do for Design Doc:
  * Add subsystem/part info to design section
  * RV table for subsystems
  * List parts and costs
  * Make headers look pretty

## 10/1/2021: More Parts, Board Design Updates, Design Doc stuff
* Looked into an [optoisolator](https://www.digikey.com/en/products/detail/vishay-semiconductor-opto-division/4N35/1738522) for our camera trigger
* Alex and I continued working on the PCB layout with all of our new parts 

![Image](https://github.com/hadrian2/RTI_Dome/blob/main/PCB_Layout_1.png)
* Completed the Design Doc

## 10/2/2021: Oops
* Forgot review signups

## 10/4/2021: Oops again
* Need to rework the schematic. Overlooked the fact that our usb-uart isn't a solderable part.
* BUT we found a [new Microcontroller](https://www.digikey.com/en/products/detail/ATMEGA32U4-AUR/ATMEGA32U4-AURCT-ND/3440960?utm_campaign=buynow&utm_medium=aggregator&curr=usd&utm_source=octopart) with UART capability built in
* Looked into the new Micro datasheet to see what she could do
* Schematic and Board updates

![Image](






