import time
import serial
import serial.tools.list_ports as AvailablePorts


ser = 0

def list_ports():   #Lists all the available ports
    print "Available ports are" + AvailablePorts
    return None

def init_serialport_linux(num):     #initialization function running on linux
        #COMNUM = 1 Enter Your COM Port Number Here.
    global ser          #Must be declared in Each Function
    ser = serial.Serial()
    ser.baudrate = 9600
        #ser.port = COMNUM - 1   #COM Port Name Start from 0
    if num == 0:
        ser.port = '/dev/ttyUSB0'
    elif num == 1:
        ser.port = '/dev/ttyUSB1'
    elif num == 2:
        ser.port = '/dev/ttyUSB2'
    elif num == 3:
        ser.port = '/dev/ttyUSB3'
    else:
        print "unacceptable port number please give a right one"

        #Specify the TimeOut in seconds, so that SerialPort
        #Doesn't hangs
    ser.timeout = 4
    ser.open()          #Opens SerialPort

    # print port open or closed
    if ser.isOpen():
        print 'Initialized port: ' + ser.portstr
        print 'Open: ' + ser.portstr
        return None
#Function Ends Here

def init_serialport_windows(num):  #initialization function running on windows

    COMNUM = num # Enter Your COM Port Number Here.
    global ser          #Must be declared in Each Function
    ser = serial.Serial()
    ser.baudrate = 9600

    if num == 0:
        ser.port = 'COM0'   #COM Port Name Start from 0
    elif num == 1:
        ser.port = 'COM1'
    elif num == 2:
        ser.port = 'COM2'
    elif num == 3:
        ser.port = 'COM3'
    else:
        print "unacceptable port number please give a right one"

        #Specify the TimeOut in seconds, so that SerialPort
        #Doesn't hangs
    ser.timeout = 4
    ser.open()          #Opens SerialPort

    # print port open or closed
    if ser.isOpen():
        print 'Initialized port: ' + ser.portstr
        print 'Open: ' + ser.portstr
        return None


def close_serialport():   #Closes SerialPort
    ser.close()
    if ser.isClose():
        print 'Closed: ' + ser.portstr
    return None

def read_port(data):        #Reads the ports whisper until the \n character
    data = ser.readline()
    print "the data I received is " + data
    return data

def write_port(info):   #Whispers the information
    ser.write(info)
    print "I tried to send that data via " + ser.name
    return None


#Call the Serial Initilization Function, Main Program Starts from here
#init_serialport(num)

    
#Ctrl+C to Close Python Window
