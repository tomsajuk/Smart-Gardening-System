import socket
import RPi.GPIO as GPIO
import time

import pygame
import subprocess as sp
import pygame.camera
import os

left = [10,9]          # GPIO pin numbers of sensors
right = [24, 25]         # GPIO pin numbers of sensors
       # watering time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

for pin in left:
    GPIO.setup(pin,GPIO.OUT)

for pin in right:
    GPIO.setup(pin,GPIO.OUT)


def switchOn(idList):
    GPIO.output(idList[0],GPIO.HIGH)
    GPIO.output(idList[1],GPIO.HIGH)

def switchOff(idList):
    GPIO.output(idList[0],GPIO.LOW)
    GPIO.output(idList[1],GPIO.LOW)

''''
import httplib as http
conn = http.HTTPConnection("192.168.31.199:3000")       #add ip
conn.request("GET","/connect")
res = conn.getresponse()
data = res.read()
conn.close()
'''
data = "NO";
if data=="YES":
    exit()
else:
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect(('192.168.31.199', 39009))                               # add ip address

	sp.call(["fswebcam","captured.jpg"])

	img = open("captured.jpg",'rb')
	size = len(img.read())
	print(size)
	img.close()

	client_socket.send(str(size))

	client_socket.recv(1024);

	img = open("captured.jpg",'rb')
	while True:
		strng = img.readline(512)
		if not strng:
			break
		client_socket.send(strng)
		#print(len(strng))
	img.close()
	print ("hello")
	#client_socket.close()

	data = ""
	sides = 0

	data = client_socket.recv(1024)
	print(data)
	if data[0:2] == "ON":
		sides = int(data[3])
		waterDuration = float(data[5:])

		if(sides == 0):
			swichOn(left)
			switchOn(right)
		elif(sides == 1):
			switchOn(right)
		elif(sides == 2):
			switchOn(left)
	
		time.sleep(waterDuration)
		switchOff(left)
		switchOff(right)
	
		print ('hi')	    
	elif data == "OFF":
		switchOff(left)
		switchOff(right)    
		print ('off')
	client_socket.close()    

GPIO.cleanup()
    
    
