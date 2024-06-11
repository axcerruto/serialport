#!/usr/bin/env python3
# Created by Antonio X Cerruto 25 May 2024
import glob
import serial
from sys import platform

class SerialPort:
	'''
	SerialPort class opens a serial port on MacOS or Linux.
	Read strings from port or write strings to port.
	'''

	def __init__(self,
				baud=115200,
				rtscts=False,
				timeout=0,
				write_timeout=0,
				modem=False):
		self.ser = None
		self.port = None
		try:
			# list arduino ports: /dev/tty.usbmodem*
			if platform == 'darwin':	# MACOS
				if(modem):
					self.port = glob.glob('/dev/tty.usbmodem*')[0]
				else:
					self.port = glob.glob('/dev/tty.usbserial*')[0]
			else:
				self.port = '/dev/ttyUSB0'

			# open serial port
			self.ser = serial.Serial(self.port,
									baudrate=baud,
									rtscts=rtscts,
									timeout=timeout,
									write_timeout=write_timeout)
			print(self.ser.name) 	# check which port was really used
			self.ser.reset_input_buffer()
			self.ser.reset_output_buffer()
		except:
			print("ERROR: no port found")

	def readline(self):
		line = self.ser.readline()
		return line.decode('utf-8')

	def readbytes(self, nbytes):
		return self.ser.read(nbytes)

	def writestring(self, s):
		self.ser.write(s.encode('utf-8'))

	def writesbytes(self, b):
		''' 
		input in format b'\x01\x02\x03\x04'
		'''
		self.ser.write(b)

	def close(self):
		self.ser.close()


if __name__ == "__main__":
    # execute only if run as a script
    ser = SerialPort(baud=115200, modem=True)
    # for i in range(50):
    	# ser.writestring(str(i))
    while True:
    	line = ser.readline()
    	if line:
    		print(line)
    ser.close()



