#!/usr/bin/env python3
# Created by Antonio X Cerruto 25 May 2024
from serialport import SerialPort
import argparse
import sys
import os
import csv
from datetime import datetime
import time

def get_filename(filename):
	'''
	Arguments:
		opt -- command line input filename (optional).
		'out.csv' is default if no filename given. 
	Returns:
		filename -- string with timestamp in yyyymmdd_hhmmss format
		and '.csv' extension.
		'out_yyyymmdd_hhmmss.csv' (Default)
	'''
	filename = filename.split('.csv')[0]
	dt = datetime.now()
	year = str(dt.year)
	month = str(dt.month).zfill(2)
	day = str(dt.day).zfill(2)
	hour = str(dt.hour).zfill(2)
	minute = str(dt.minute).zfill(2)
	second = str(dt.second).zfill(2)
	timestamp = year + month + day + '_' + hour + minute + second
	filename = filename + '_' + timestamp + '.csv'
	return filename

def _timestamp():
	'''
	Returns system time in milliseconds
	'''
	return int(time.time()*1000)


def main(args):
	t_start = _timestamp()
	t = _timestamp()
	triggertime = args.triggertime
	filename = get_filename(args.filename)
	ser = SerialPort(baud=9600)
	header = 'DS18B20 (mist),front (mist),inside,back,'
	file = open(filename, 'w', newline='')

	try:
		file.write(header)
		while True:
			if((_timestamp() - t) > triggertime):
				line = ser.readline()
				if line:
					# line = str(_timestamp()-t_start) + ',' + line
					print(line)
					file.write(line)
					file.flush()
				t = _timestamp()
	finally:
		file.close()



if __name__ == "__main__":
    # execute only if run as a script
    parser = argparse.ArgumentParser(description="record serial data to csv file")
    parser.add_argument('-f', '--filename', type=str, required=False,
    					default='out',
    					help='output filename')
    parser.add_argument('-t', '--triggertime', type=int, required=False,
    					default='250',
    					help='time between data collections in milliseconds')
    args = parser.parse_args()
    main(args)

    



