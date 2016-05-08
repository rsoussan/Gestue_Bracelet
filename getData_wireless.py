import serial, os
import numpy as np
import sys
from serial.tools import list_ports
from time import clock, time

def list_serial_ports():
    # Windows
    if os.name == 'nt':
        # Scan for available ports.
        available = []
        for i in range(256):
            try:
                s = serial.Serial(i)
                available.append(i)
                s.close()
            except serial.SerialException:
                pass
        return available
    else:
        # Mac / Linux
        return [port[0] for port in list_ports.comports()]

	
def getData_wireless():	
	x =[]
	y =[]
 	z =[]
 	lookfordata = True
 	savedata = True
	comms = list_serial_ports()
	com = -1
	baud_rate = 19200
	for com in comms:
		print com
		print(com=="/dev/tty.usbserial-FTELPQB5")
		if(com=="/dev/tty.usbserial-FTELPQB5"):	# wireless coms
			try:
				ser = serial.Serial(com,baud_rate)
				print ser.portstr
				while lookfordata:
					data = ser.readline()
					#print(str(data) == "start\r\n")
					#print(str(data) == "-1")
					#print data
					#print type(data)
					#if (int(data) == -1):
					if (str(data) == "start\r\n"):
						while savedata:
							data = ser.readline()
							if (str(data) == "end\r\n"):
								savedata = False
								lookfordata = False
								break
							else:
								nums = [int(n) for n in data.split()]
								if (len(nums) != 3):
									1;
								else:
									print("read data: " + data)
									if any( [nums[0] > 1000, nums[0] < 100, nums[1] > 1000, nums[1] < 100,nums[2] > 1000, nums[2] < 100,] ):
										1;
									else:
										x.append(nums[0])
										y.append(nums[1])
										z.append(nums[2])
						ser.close()   
			except serial.SerialException:
				print('serial port not found')
	return(x,y,z)
	#np.savez(sys.argv[1], x, y,z)