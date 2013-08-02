import serial
from serial.tools import list_ports
import os
from optparse import OptionParser
import io
import time
import random
import sys
import string


def open_port(dev,baudrate):
    ser = serial.Serial(dev, 19200, timeout=1000, parity=serial.PARITY_NONE)
    return ser

def list_serial_ports():
    # Windows
    if os.name == 'nt':
        # Scan for available ports.
        available = []
        for i in range(256):
            try:
                s = serial.Serial(i)
                available.append('COM'+str(i + 1))
                s.close()
            except serial.SerialException:
                pass
        return available
    else:
        # Mac / Linux
        return [port[0] for port in list_ports.comports()]

def send_data(source,data,io_keeper):
    #print "Source: ",source
    
    #figure out what type of i/o we are
    if source < len(io_keeper):
        io_port = io_keeper[source - 1]
        if io_port[0] == "serial":
            io_port[1].write("".join(chr(i) for i in data) )
  
'''   if source == 2:
            print data
            time.sleep(0.05)
'''
def main():
    
    parser = OptionParser()
    parser.add_option("-d", "--dev", dest="dev", action="store", help="tty dev(ex. '/dev/ttyUSB0'", metavar="DEV")
    parser.add_option("-f", "--filename", dest="filename", action="store", help="Filename", metavar="FILENAME")
    parser.add_option("-s","--speedup",dest="speedup",action="store",help="Fast forward factor - speed up outputs.",type="float",metavar="FF")
    parser.add_option("-c","--configfile",dest="configfile",action="store",help="Point to i/o config file",type="string",metavar="CONFIGFILE")


    (options, args) = parser.parse_args()
    
    dev = options.dev
    filename = options.filename
    speedup = options.speedup
    config_file = options.configfile
    
    #get i/o configuration
    f = open(config_file, 'r')
    config_array = f.readlines()
    
    io_keeper = []
    
    #parse i/o configuratio and setup i/o
    for i in range(len(config_array)):
        parameters =  config_array[i]
        parameters = parameters.split(',')
        if parameters[1] == "serial":
            sub_param = parameters[2].split(":")
            try:
                ser = open_port(sub_param[0],19200)
                print "Opened: %s at %s baud" % (sub_param[0],sub_param[1])
            except:
                print "Could not open serial port.  Exiting."
                print "Unexpected error:", sys.exc_info()[0]
                raise
                #print list_serial_ports()
            io_port = ["serial",ser]
        else:
            print "NULL or unsupported i/o type"
            io_port = ["NULL",0]
        io_keeper.append(io_port)
        
            
    f = open(filename, "rb")   
    b =  f.read()
    iterations = len(b) - 10                   

    buf = []
    a = []
    
    for i in range(len(b)):
        a.append(ord(b[i]))
    
    i = 0
    
    first_through = True
    
    min_time = 0
    max_time = 0
    
    while i < iterations:  
        source = a[i]
        i += 1   
        timestamp = a[i] * 2**24 + a[i + 1] * 2**16 + a[i + 2] * 2**8 + a[i + 3]
        time_value = timestamp * .001
        i += 4
        length = a[i] * 2**24 + a[i + 1] * 2**16 + a[i + 2] * 2**8 + a[i + 3]
        i += 4
        data = a[i:i+length]
        i += length
    
        if first_through:
            last_time = time_value
            min_time = time_value
            first_through = False
        else:
            time_delta = time_value - last_time
            time.sleep(time_delta/speedup)
            last_time = time_value
            max_time = time_value
        
        send_data(source,data,io_keeper)
    
    print min_time,max_time
    
        
if __name__ == '__main__':
    main()
