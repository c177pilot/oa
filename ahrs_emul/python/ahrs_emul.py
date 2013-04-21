import serial
from serial.tools import list_ports
import os
from optparse import OptionParser
import io
import time
import random
import sys


SEARCHING_HEADER = 0 
HEADER_MSB_FOUND = 1
HEADER_LSB_FOUND = 2
ID_FOUND = 3
GET_DATA = 4
GET_CHECKSUM = 5

number_bytes_to_get = 0 

HEADER_MSB = 0x7F
HEADER_LSB = 0xFF

OUTPUT_SENTENCE_1_ID = 0xFE
OUTPUT_SENTENCE_2_ID = 0xFD
OUTPUT_SENTENCE_3_ID = 0xFC
OUTPUT_SENTENCE_4_ID = 0xFB
OUTPUT_SENTENCE_5_ID = 0xFA

sentence_size = [23,21,25,40,99]

def open_port(dev,baudrate):
    ser = serial.Serial(dev, 19200, timeout=1000, parity=serial.PARITY_NONE)
    return ser
    
def if_negative(char):
    if ( ( char >> 7 ) & 1 ) == 1:
        return True
    else:
        return False
    
def process_sentence_1(buf):
    
    char = buf[0]
    if not char == 4:
        print char
    align_mode_in_progress = char & 1
    air_align =  ( char >> 1 ) & 1
    mx_sentence_active = ( char >> 2) & 1
    factory_cal_in_progress = ( char >> 3 ) & 1
    gyro_bias_averaged = ( char >> 4 ) & 1
    fine_mag_cal_in_progress = ( char >> 5 ) & 1
    ahrs_invalid = ( char >> 6 ) & 1
     
    
    #calc roll angle
    msb = buf[1]
    lsb = buf[2]
    value = msb * 256 + lsb
    if value < 0x8000:
        value = value / 32768.0 * 180.0
    else:
        value = value - 0x8000
        value = -( value / 32768.0 * -180.0 + 180.0 )
    roll = value
    print msb,lsb,value
    
    
    
    #calc pitch angle
    msb = buf[3]
    lsb = buf[4]
    value = msb * 256 + lsb
    #print msb,lsb
    if value < 0x8000:
        value = value / 32768.0 * 180.0
    else:
        value = value - 0x8000
        value = -( value / 32768.0 * -180.0 + 180.0 )
    pitch = value
    #print msb,lsb,value
    
    #calc yaw angle 
    msb = buf[5]
    lsb = buf[6]
    value = msb * 256 + lsb
    if value < 0x8000:
        value = value / 32768.0 * 180.0
    else:
        value = value - 0x8000
        value = -( value / 32768.0 * -180.0 + 180.0)
    #print msb,lsb,value    
    yaw = value    
    
    #calc altitude
    msb = buf[7]
    lsb = buf[8]
    value = msb * 256 + lsb
    if value == 0:
        data_invalid = 1
    else:
        data_invalid = 0
        value = value - 5000.0
    #print msb,lsb,value
    altitude = value
    
    #calc altitude rate
    msb = buf[9]
    lsb = buf[10]
    value = msb * 256 + lsb
    if value < 0x8000:
        value = value * 1.0
    else:
        value = value - 0x8000
        value = value * -1.0
    vertical_speed = value
    #print msb,lsb,value    
       
    #calc indicated airspeed
    msb = buf[11]
    lsb = buf[12]
    value = msb * 256 + lsb
    if value < 0x8000:
        value = value * 1.0
    else:
        value = value - 0x8000
        value = value * -1.0
    value = value / 10 * .592483 # conversion from .1 ft/s units to kts
    airspeed = value
    dont_use_airspeed = 1
    #print msb,lsb,value 
    
        
    #calc ias rate
    msb = buf[13]
    lsb = buf[14]
    value = msb * 256 + lsb
    if value < 0x8000:
        value = value * 1.0
    else:
        value = value - 0x8000
        value = value * -1.0
    value = value / 10 * .592483 # conversion from .1 ft/s units to kts
    airspeed = value
    dont_use_airspeed = 1
    #print msb,lsb,value 
    
    #calc accel roll angle
    msb = buf[15]
    lsb = buf[16]
    value = msb * 256 + lsb
    #print msb,lsb
    if value < 0x8000:
        value = value / 32768.0 * 180.0
    else:
        value = value - 0x8000
        value = value / 32768.0 * -180.0
    accel_roll = value
    #print value
    
    
    #calc normal accel
    msb = buf[17]
    lsb = buf[18]
    value = msb * 256 + lsb
    if value < 0x8000:
        value = value  * 0.001
    else:
        value = value - 0x8000
        value = value * -0.001
    normal_accel = value
    #print msb,lsb,value 
    #print value    


def process_sentence_2(buf):
    
    #calculate oat
    msb = buf[0]
    value = msb
    if value >= 0x80:
        value = value - 0x80
    value = value * 1.0
    #print msb, value
    
    #calc voltage 1
    msb = buf[1]
    lsb = buf[2]
    value = msb * 256 + lsb
    if value < 0x8000:
        value = value  * 0.01
    else:
        value = value - 0x8000
        value = value * -0.01
    voltage1 = value
    #print msb,lsb,value 
    #print value    

    #calc voltage 2
    msb = buf[3]
    lsb = buf[4]
    value = msb * 256 + lsb
    if value < 0x8000:
        value = value  * 0.01
    else:
        value = value - 0x8000
        value = value * -0.01
    voltage2 = value
    #print msb,lsb,value 
    #print value
    
    #calc voltage 3
    msb = buf[5]
    lsb = buf[6]
    value = msb * 256 + lsb
    if value < 0x8000:
        value = value  * 0.01
    else:
        value = value - 0x8000
        value = value * -0.01
    voltage3 = value
    #print msb,lsb,value 
    #print value
    
    #status_word_1
    msb = buf[7]
    coarse_mag_invalid = msb & 1
    fine_mag_invalid = ( msb >> 1 ) & 1
    cal_fialed_heading = ( msb >> 2 ) & 1
    mag_fail = ( msb >> 3 ) & 1
    voltage_fail = ( msb >> 4 ) & 1
    gyro_max_rate = ( msb >> 5 ) & 1
    roll_max_rate = ( msb >> 6 ) & 1
    yaw_max_rate = ( msb >> 7 ) & 1
    
    #status_word_2
    msb = buf[8]
    movement_during_alignment = msb & 1
    mag_x_fail = ( msb >> 1 ) & 1
    mag_y_fail = ( msb >> 2 ) & 1
    mag_z_fail = ( msb >> 3 ) & 1
    gyro_x_fail = ( msb >> 4 ) & 1
    gyrp_y_fail = ( msb >> 5 ) & 1
    gyro_z_fail = ( msb >> 6 ) & 1
    
    #status_word_3
    msb = buf[9]
    acc_x_fail = msb & 1
    acc_y_fail = ( msb >> 1 ) & 1
    acc_z_fail = ( msb >> 2 ) & 1
    altimeter_fail = ( msb >> 3 ) & 1
    airspeed_fail = ( msb >> 4 ) & 1
    internal_temp_fail= ( msb >> 5 ) & 1   
    
    #internal temp
    msb = buf[10]
    value = msb
    if value >= 0x80:
        value = value - 0x80
    value = value * 1.0
    internal_temp = value
    #print msb, value
    
    #version
    msb = buf[11]
    lsb = buf[12]
    software = "%d,%d" % (msb,lsb)
    #print msb,lsb,software
    
def process(buf,sentence_id):
        
    if sentence_id == 1:
        process_sentence_1(buf)
    elif sentence_id == 2:
        process_sentence_2(buf)
    elif sentence_id == 3:
        o = 2
    elif sentence_id == 4:
        o = 2
    elif sentence_id == 5:
        o = 3
    
    
    
def main():
    
    parser = OptionParser()
    parser.add_option("-d", "--dev", dest="dev", action="store", help="tty dev(ex. '/dev/ttyUSB0'", metavar="DEV")
    parser.add_option("-p", "--filename", dest="filename", action="store", help="Filename", metavar="FILENAME")

    (options, args) = parser.parse_args()
    
    dev = options.dev
    filename = options.filename
    
    try:
        ser = open_port(options.dev,19200)
    except:
        print "Could not open serial port.  Exiting."
        print "FYI - Here's a list of ports on your system."
        print list_serial_ports()
        sys.exit()
             
    f = open(filename, "rb")   
    a =  f.read()
    iterations = len(a) - 50                   
    i = 0 
    state = SEARCHING_HEADER
    
    bytes_got = 0
    running_checksum = 0

    sentence_count = 0 
    
    buf = []
    
    while i < iterations:  
        char = ord(a[i])
        
        if state == SEARCHING_HEADER:
            bytes_got = 0
            if char == HEADER_MSB:
                state = HEADER_MSB_FOUND

        elif state == HEADER_MSB_FOUND:
            if char == HEADER_LSB:
                state = HEADER_LSB_FOUND
                #print 'header found'
            else:
                state == SEARCHING_HEADER
        elif state == HEADER_LSB_FOUND:
            if char <= 0xFE and char > 0xFA: #ignore eeprom msgs for now
                sentence = abs(char - 0xFA - 5) 
                num_of_bytes_to_get = sentence_size[sentence - 1]
                running_checksum = (running_checksum + char )
                state = GET_DATA
            else: 
                state = SEARCHING_HEADER
        elif state == GET_DATA:
            buf.append(char)
            running_checksum = (running_checksum + char)
            bytes_got += 1
            if bytes_got == num_of_bytes_to_get - 4:
                state = GET_CHECKSUM
        elif state == GET_CHECKSUM:
            #print char, 256 - abs(~(running_checksum % 256))
            if char == 256 - abs(~(running_checksum % 256)):
                ab = 0
                #print "Good checksum", sentence
                process(buf,sentence)
            else:
                b = 0
                #print "Bad checksum", sentence
    
            buf = []
            sentence_count += 1
            running_checksum = 0
            state = SEARCHING_HEADER
            
        i += 1    
                
                
    print "Total sentences: ",sentence_count
    
if __name__ == '__main__':
    main()
