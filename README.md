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


  ![Image](https://github.com/hadrian2/RTI_Dome/blob/main/Design_Images_and_Code_Sippets/Umbrella_Sketch.jpg)
* Sketched out rough block diagram


  ![Image](https://github.com/hadrian2/RTI_Dome/blob/main/Design_Images_and_Code_Sippets/First_Block_Sketch.jpg)
  
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

![Image](https://github.com/hadrian2/RTI_Dome/blob/main/Design_Images_and_Code_Sippets/First_Schematic.png)

## 9/26/2021: Continued Parts Research and Schematic Design
* Looked through multiple LED drivers and settled on [this](https://www.st.com/resource/en/datasheet/led5000.pdf) one for now
* [LED Bulbs](https://www.ledtronics.com/Clearance/?p=MR16-42-SIW-001M)
* [USB to UART](https://www.digikey.com/en/products/detail/digilent-inc/410-212/4090089)

## 9/27/2021: Continued Parts Research and Schematic Design
* Light research on led5000 driver datasheet to try to understand it
* Alex updated our schematic with new parts, Evan recommended [TLC5940 LED driver](https://www.ti.com/product/TLC5940) instead of led5000
* Jack working on Autocad designs for the dome

![Image](https://github.com/hadrian2/RTI_Dome/blob/main/Design_Images_and_Code_Sippets/Schematic_2.png)

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

![Image](https://github.com/hadrian2/RTI_Dome/blob/main/Design_Images_and_Code_Sippets/PCB_Layout_1.png)
* Completed the Design Doc

## 10/2/2021: Oops
* Forgot review signups

## 10/4/2021: Oops again
* Need to rework the schematic. Overlooked the fact that our usb-uart isn't a solderable part.
* BUT we found a [new Microcontroller](https://www.digikey.com/en/products/detail/ATMEGA32U4-AUR/ATMEGA32U4-AURCT-ND/3440960?utm_campaign=buynow&utm_medium=aggregator&curr=usd&utm_source=octopart) with UART capability built in
* Looked into the new Micro datasheet to see what she could do
* Schematic and Board updates

![Image](https://github.com/hadrian2/RTI_Dome/blob/main/Design_Images_and_Code_Sippets/Schematic_Rework.png)

![Image](https://github.com/hadrian2/RTI_Dome/blob/main/Design_Images_and_Code_Sippets/PCB_Layout_2.png)

## 10/5/2021: Design Review
* Updated R/V Table

## 10/6/2021: Final PCB Revisions
* Dotted i's and crossed t's on tha schematic and PCB layout. Ready to order (hopefully)

![Image](https://github.com/hadrian2/RTI_Dome/blob/main/Design_Images_and_Code_Sippets/Schematic_3.png)

![Image](https://github.com/hadrian2/RTI_Dome/blob/main/Design_Images_and_Code_Sippets/PCB_Layout_3.png)

## 10/7/2021: Submitted our PCB Design!

## 10/8/2021: General Group Meeting
* Talked about next steps
* Set a tentative to do list
* I plan to have a software flowchart and GUI sketch by next week

## 10/12/2021: Parts came in!
* Jack finalized a physical dome design

![Image](https://github.com/hadrian2/RTI_Dome/blob/main/Design_Images_and_Code_Sippets/Dome_Design.png)

## 10/13/2021: Looked into possible GUI frameworks
* Intend to use Python. Currently considering:
  * Kivy
  * Tkinter
  * PyQt maybe?
* Created tentative software flowchart

[Flowchart](https://github.com/hadrian2/RTI_Dome/blob/main/Design_Images_and_Code_Sippets/RTI_Dome_Flowchart.pdf)

## 10/16/2021: Working on GUI
* Rough Sketch of GUI

![Image](https://github.com/hadrian2/RTI_Dome/blob/main/Design_Images_and_Code_Sippets/GUI_Rough_Sketch.JPG)

* Tried getting started with Kivy, but wouldn't install on my virtual environment
* Ended up having to install Spyder IDE which worked 
* Began playing around in Kivy to learn how to make a nice GUI. Was able to get a basic layout of the Home page.

![Image](https://github.com/hadrian2/RTI_Dome/blob/main/Design_Images_and_Code_Sippets/Kivy_GUI_Homepage.png)

## 10/18/2021: Dome Construction has begun!

## 10/19/2021: PCB arrived + GUI considerations
* Evan suggested using WebUSB to create a webapp instead of a desktop application
* I like this idea more than Kivy because if I had so much trouble installing the library, it could surely happen to our sponsor too
* Began researching [WebUSB](https://wicg.github.io/webusb/)

## 10/22/2021: More WebUSB Research
* Important functions:
  * navigator.usb.requestDevice()
    * Prompts user to select a connected USB device
    * Use this to select our PCB and allow us to send data back and forth
  * navigator.usb.getDevices()
    * Gets a list of all connected USB devices
    * Could be an alternative to select our PCB, searching through the list using specific vendor ID
    * Makes things easier for the user (they don't have to select the device themselves)
* Sample code (Connecting to an Arduino):

navigator.usb.requestDevice({ filters: [{ vendorId: 0x2341 }] })
.then(device => {
  console.log(device.productName);      // "Arduino Micro"
  console.log(device.manufacturerName); // "Arduino LLC"
})
.catch(error => { console.error(error); });

* After that, seems to be just simple serial communication
* Gotta learn JavaScript and HTML unfortunately. Started looking into the basics of both

## 10/26/2021: Board Assembly and testing
* We soldered on essential parts (Drivers, Power, Micro) onto our board
* Supplied power to the board, but nothing's happening
  * LED turns on sometimes, but it's not supposed to, as the micro isn't programmed
    * Current guess is this is because the values of the micro are currently floating, so they could be high or low.
    * Maybe board is shorted?

## 10/29/2021: Board Assembly and testing (cont.)
* Board seems to be shorted somewhere. The LEDs are drawing current from the drivers when they shouldn't be. The drivers' registers haven't been set, so they shouldn't be allowing any current draw under normal functioning conditions.
* Arduino IDE can't find the micro. We think the board is shorted within the LED driver section of the PCB.
* Scratched off 5V trace on our board, separating the LED drivers to isolate our micro to see if we could program it that way. No dice.

## 11/2/2021: More GUI Considerations
* Evan suggested we ditch WebUSB and stick with Python, using the built in framework TKinter.
* I like this suggestion because I don't have to worry about dealing with JavaScript and HTML.

## 11/4/2021: Board Assembly and testing (cont.)
* Decided to resolder a new micro and a couple of LED drivers onto a new board. Now the LED is consistently on when given power. Now we are assuming this is due to incorrect PCB layout. 
* While this board issue is being resolved, I plan to use an Arduino to unit test an LED driver to see if I can figure out how to get it functioning properly.

## 11/4/2021: Dome Construction Finished!

## 11/6/2021: Fun with Tkinter
* I found a [great resource](https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/) on how to create a GUI with multiple pages in Tkinter
* I took this sample code and adapted it to work with our project, and was able to create a skeleton of the GUI

![Image](https://github.com/hadrian2/RTI_Dome/blob/main/Design_Images_and_Code_Sippets/GUI_Home_Skeleton.png)

![Image](https://github.com/hadrian2/RTI_Dome/blob/main/Design_Images_and_Code_Sippets/GUI_Auto_Skeleton.png)

![Image](https://github.com/hadrian2/RTI_Dome/blob/main/Design_Images_and_Code_Sippets/GUI_Manual_Skeleton.png)


## 11/9/2021: LED Driver testing
* Evan provided us with a breakout board for our LED driver so I could test with an Arduino on a breadboard. God bless you Evan.
* Jack working on wiring the dome
* Found an Arduino library for controlling our specific driver. Trying to get an LED to light up using this driver using [this](https://playground.arduino.cc/Learning/TLC5940/) reference.
* Tried using given library functions to turn on and off LEDs to no avail. Referring back to the [TLC5940 Datasheet](https://www.ti.com/product/TLC5940?utm_source=google&utm_medium=cpc&utm_campaign=app-led-null-prodfolderdynamic-cpc-pf-google-wwe&utm_content=prodfolddynamic&ds_k=DYNAMIC+SEARCH+ADS&DCM=yes&gclid=CjwKCAiA78aNBhAlEiwA7B76p3s54ISAGRmD_Q9z8pcWMUK1mUTM8qzrQvB5o3cjqEsktUIdCyhSQRoC2y8QAvD_BwE&gclsrc=aw.ds) to see if I can get the driver working using my own code. 
* Necessary signals (i think):
  * TLC5940 clocks in 192 bits of lighting data from SIN using SClk.
  * BLANK, when high, closes outputs, preventing all LEDs from turning on.
  * XLAT is what actually sets the data after it's clocked in
* Still can't get the driver working with my own code.
  * Initialize signals (All are digital):
  
  ![Image](https://github.com/hadrian2/RTI_Dome/blob/main/Design_Images_and_Code_Sippets/LED_Test_init.png)
  
  * Function to clock in bits from SIN:

  ![Image](https://github.com/hadrian2/RTI_Dome/blob/main/Design_Images_and_Code_Sippets/LED_Test_clock.png)

  * Function to set bits after being clocked in:

  ![Image](https://github.com/hadrian2/RTI_Dome/blob/main/Design_Images_and_Code_Sippets/LED_Test_set.png)

* Guessing that I busted the chip at some point because after 4 hours I genuinely don't know what else could be wrong. Calling it a night.

## 11/11/2021: LED Driver testing (cont.)
* Trying to test on a new driver using the TLC5940 library.
* IT WORKS
* Now trying to get it working using my own code, so we can further customize how exactly we want to control our LEDs
* Not working on code from Tuesday 9th. Looking into the datasheet some more.
* After looking at the timing chart more closely I learned some things:
  
  ![Image](https://github.com/hadrian2/RTI_Dome/blob/main/Design_Images_and_Code_Sippets/TLC5940_Timing.png)
  
  * Seems like XLAT should be triggered inside of a high BLANK signal.
  * GSClk looks like I can just have it running at all times.

* With this in considerations, I modified the set() function and changed GSClk to an analog signal with 50% PWM duty cycle.
  
  ![Image](https://github.com/hadrian2/RTI_Dome/blob/main/Design_Images_and_Code_Sippets/LED_Test_set2.png)
  
* LED now lights up with my code!
* Started implementation of Automatic Imaging and Manual Imaging functions for a single driver
* Continued messing with the LED driver, and I think I broke it...
* To add insult to injury, when trying to solder on a new driver to the breakout board, I ripped one of the traces of the board...
* Still happy with today's results though.

## 11/12/2021: PCB Redesign
* Now that we actually know what signals we need to control the drivers, we updated our PCB and Schematic to include BLANK and XLAT signals from the micro to the drivers, and hope to get a new set of boards ASAP. Should be here on the 23rd :/

![Image](https://github.com/hadrian2/RTI_Dome/blob/main/Design_Images_and_Code_Sippets/Schematic_4.png)

![Image](https://github.com/hadrian2/RTI_Dome/blob/main/Design_Images_and_Code_Sippets/PCB_Layout_4.png)

* Still need to figure out uploading code our micro through USB. Keep getting the error: “selected serial port does not exist or your board is not connected”
* Started implementation of Automatic Imaging and Manual Imaging functions

## 11/19/2021: New PCB Arrived!
## 11/19/2021: Microcontroller troubleshooting
* Still can't get the micro programmed through USB.
* After searching all over the internet for a solution, we found a random [reddit user's post](https://www.reddit.com/r/arduino/comments/drkoom/solved_atmega32u4_forcing_reset_using_1200bps/) that was having the same problem as us, who found this solution of installing the Arduino Micro bootloader instead of the Leonardo bootloader we had been using. It worked lol.

## 11/22/2021 - 11/27/2021: Thanksgiving Break
* Adapted Arduino code to match pin assingments for ATmega
* Updated Automatic Imaging and Manual Imaging functions to accommodate all 4 drivers

![Image](https://github.com/hadrian2/RTI_Dome/blob/main/Design_Images_and_Code_Sippets/Auto_Imaging.png)

![Image](https://github.com/hadrian2/RTI_Dome/blob/main/Design_Images_and_Code_Sippets/Manual_Imaging.png)

* Worked on the actual functionality of the GUI. Using Pyserial to establish a serial connection and searching through the COM ports for chip's vendor ID. Firmware will look for serial input of "A" to run automatic imaging, and "Mx" for manual, where x is an integer 0-31.
  * Pyserial search:
    * import serial.tools.list_ports as st
      plist = list(st.comports())
      port = None
      for i in plist:
        if i.vid == 9025:
          port = i.device
          device = "Connected!"

      if port == None:
      device = "Not Found :("

      cereal = ser.Serial(port, 9600, timeout=1)

  * Firmware main loop:


![Image](https://github.com/hadrian2/RTI_Dome/blob/main/Design_Images_and_Code_Sippets/ATmega_loop.png)

  * Issues sending the correct number for manual imaging serial command. Since each button in the manual imaging grid is being created in the same nested for loop, whenever we update the number variable, it changes the sent number for all buttons. All buttons send "M31".
  * Created a helper function "makeButton" which makes a button using the desired number as an input, so a unique button with a unique command is created every iteration of the for loop

## 11/28/2021: More PCB Problems...
* Testing the code on our new PCB, but its not doing anything :(
* We decided to check each signal coming out of our micro using an oscilloscope to see if everything was behaving correctly.
  * Found that GCLK was not producing the PWM signal we expected.
  * After looking at ATmega pinouts, we found that the pin assigned to GCLK on our board didn't have PWM capability...
  * Solved this by scratching out the GCLK trace and rerouting it to a test point on the board that DID have PWM capability.
* IT WORKS!

## 11/29/2021: Faulty Lighting and Wire Braiding
* Testing our code and PCB with the actual dome, but it doesn't seem to work with the LED's on the dome even though it works fine with our test LED.
* Found out our problem was because Jack sucks at crimping. LED's functioned correctly when tested with correct crimping.
* Started the tedious task of braiding all the LED wires and crimping them.

## 11/30/2021: D-Day
* About half of our dome's LEDs were crimped by the time demo came around. 
* Murphy's Law in full effect as we tried changing the code to trigger our camera, but the upload messed with our serial connection, so the dome didn't work on the first try during the demo
* After some tinkering, we reinstalled the bootloader, uploaded the previous code and the dome worked!

## Further work:
* We finished up wiring the dome, ziptied the wires to make it look a little nicer, reuploaded the code to trigger the camera, and I figured out how to package our application into a single executable using PyInstaller, an app packaging package.
* We delivered our completed project to the Spurlock Museum and it worked NEARLY perfectly on the first try.
* After tweaking some timings to match up with the speed of their camera, we were able to successfully imaage all 32 lighting angles and were left with a satisfied customer. EZ money.















