#!/usr/bin/env python3
# Created by Antonio X Cerruto 24 Feb 2022
import glob
import serial
from sys import platform
from time import sleep

class SerialPort:
	'''
	SerialPort class opens a serial port on MacOS or Linux.
	Read strings from port or write strings to port.
	'''

	def __init__(self,
				baud=250000,
				rtscts=False,
				timeout=0,
				write_timeout=0):
		self.ser = None
		self.port = None
		try:
			# list arduino ports: /dev/tty.usbmodem*
			if platform == 'darwin':	# MACOS
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

	def readline():
		line = self.ser.readline()
		return line.decode('utf-8')

	def readbytes(nbytes):
		return self.ser.read(nbytes)

	def writestring(s):
		self.ser.write(s.encode('utf-8'))

	def writesbytes(b):
		''' 
		input in format b'\x01\x02\x03\x04'
		'''
		self.ser.write(b)

	def close()
		self.ser.close()


if __name__ == "__main__":
    # execute only if run as a script
    ser = SerialPort(baud=9600)
    # for i in range(50):
    	# ser.writestring(str(i))
    while True:
    	line = ser.readline()
    	if line:
    		print(line)
    ser.close()



