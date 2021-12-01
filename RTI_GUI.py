import tkinter as tk
import serial as ser
import serial.tools.list_ports as st
plist = list(st.comports())
port = None
for i in plist:
    print(i)
    if i.vid == 9025:
        port = i.device
        device = "Connected!"
        print(device)

if port == None:
    device = "Not Found :("

cereal = ser.Serial(port, 9600, timeout=1)
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(Home)
        self.title('RTI Controller')

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class Home(tk.Frame): #Home page
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="RTI Controller Home", font = ("Roboto", 20)).pack(side="top", fill="x", pady=30)
        if device == "Device Not Found :(":
            tk.Label(self, text="Automatic Imaging", height = 3, width = 20, fg = 'black', bg = 'gray', relief = 'ridge').pack(padx = 100)
        else:
            tk.Button(self, text="Automatic Imaging", height = 3, width = 20,
                  command=lambda: master.switch_frame(Auto)).pack(padx = 100)
        tk.Button(self, text="Manual Imaging", height = 3, width = 20,
                  command=lambda: master.switch_frame(Manual)).pack(padx = 100)
        #tk.Button(self, text="Configuration", height = 3, width = 20,
                  #command=lambda: master.switch_frame(Config)).pack(padx = 100,pady=(0,100))
        botFrame = tk.Frame(self, bg = "white" , borderwidth = 2, relief = 'sunken')
        botFrame.pack(padx = 10, pady = 10)
        tk.Label(botFrame, text= "Device: %s"%device, fg = 'black', bg = 'white' ,font = ("Roboto", 8)).pack(side="top", fill="x", pady=30)

class Auto(tk.Frame): #Automatic Imaging page
    def __init__(self, master):
        byte = None
        tk.Frame.__init__(self, master)
        topFrame = tk.Frame(self)
        topFrame.pack()
        botAFrame = tk.Frame(self)
        botAFrame.pack(side = 'bottom')
        tk.Label(topFrame, text="Automatic Imaging", font = ('', 20)).pack(side="top", fill="x", pady=10)
        tk.Button(topFrame, text="Start", font = ('',30), height = 3, width = 10,
                command=lambda:[cereal.write("A".encode()), master.switch_frame(Wait)]).pack(side = 'left',padx = 100,pady=50)
        tk.Button(botAFrame, text="Back", height = 2, width = 10,
                command=lambda: master.switch_frame(Home)).pack(side = 'bottom')
#[cereal.write("A".encode()), master.switch_frame(Wait)])#

class Manual(tk.Frame): #Manual page
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        topFrame = tk.Frame(self, bg = "white" , borderwidth = 2,relief = 'sunken')
        topFrame.pack(pady = (10,0))
        self.midFrame = tk.Frame(self, bg = "white")
        self.midFrame.pack(padx= 50, pady = (0,10))
        botMFrame = tk.Frame(self)
        botMFrame.pack(side = 'bottom')
        tk.Label(topFrame, text="Manual Imaging", font = ('Georgia', 20), bg = "white", fg = "black").grid(row = 0,column=0, padx = 10, pady = 10)
        for i in range(8):
            for j in range(4):
                rc = i*4+j
                self.makeButton(rc)
        tk.Button(botMFrame, text="Back", height = 2, width=10,
                  command=lambda: master.switch_frame(Home)).pack()
    def makeButton(self,num):
        Int2Char = ["0","1","2","3","4","5","6","7","8","9"]
        tens = int(num / 10)
        ones = int(num%10)
        if tens !=0:
            tk.Button(self.midFrame, text= "LED %s" % (num+1), height = 2,width = 10, command = lambda: cereal.write(("M"+Int2Char[tens]+Int2Char[ones]).encode())).grid(row=int(num/4),column=int(num%4), padx = 5, pady = 5)
        else:
            tk.Button(self.midFrame, text= "LED %s" % (num+1), height = 2,width = 10, command = lambda: cereal.write(("M"+Int2Char[tens]+Int2Char[ones]).encode())).grid(row=int(num/4),column=int(num%4), padx = 5, pady = 5)
class Config(tk.Frame): #Config page @NOT USED RIGHT NOW@
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Configuration", font = ('Georgia', 20), bg = "white", fg = "black").pack(padx = 10, pady = 10)
        tk.Button(self, text="Back",
                  command=lambda: master.switch_frame(Home)).pack()
class Wait(tk.Frame): #Wait page
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        botWFrame = tk.Frame(self)
        botWFrame.pack(side = 'bottom')
        tk.Label(self, text="Imaging in Progress...", font = ("Roboto", 30)).pack(side="top", fill="x", pady=30)
        tk.Button(botWFrame, text="Back", height = 2, width=10,
                  command=lambda: master.switch_frame(Home)).pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
