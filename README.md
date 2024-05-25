# serialport
Python Serial Port

## Hardware 
USB to TTL FTDI cable TTL-232RG-VSW5V-WE
https://ftdichip.com/product-category/products/cables/usb-ttl-serial-cable-series/

## USB to TTL Cable Signals and Connections
Color | Signal | Arduino Pin
--- | --- | ---
Black | GND | GND
Brown | CTS (Clear to send) | 7
Red | VCC (Power supply output) | 5V
Orange | Tx (Transmit) | 0
Yellow | Rx (Receive) | 1
Green | RTS (Request to send) | 8

## Install requirements:
```
python3 -m pip install pyserial
```
