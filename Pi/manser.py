import socket
import time
import RPi.GPIO as GPIO

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("192.168.31.54", 6102))                          #add ip
server_socket.listen(5)

while True:
	client_socket, address = server_socket.accept()
	
	query = client_socket.recv(1024)
	if(query[0:2] == "ON"):
		import RPi.GPIO as gpio
		left = [10,9]          # GPIO pin numbers of sensors
		right = [24, 25]               # GPIO pin numbers of sensors
			   # watering time

		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)

		for pin in left:
			GPIO.setup(pin,GPIO.OUT)

		for pin in right:
			GPIO.setup(pin,GPIO.OUT)


		
		GPIO.output(left[0],GPIO.HIGH)
		GPIO.output(left[1],GPIO.HIGH)
		GPIO.output(right[0],GPIO.HIGH)
		GPIO.output(right[1],GPIO.HIGH)
		client_socket.send('Flow')
		client_socket.close()
			
		print 'FLow'
		
		GPIO.output(left[0],GPIO.LOW)
		GPIO.output(left[1],GPIO.LOW)
		GPIO.output(right[0],GPIO.LOW)
		GPIO.output(right[1],GPIO.LOW)
		
	
	
