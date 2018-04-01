import socket
import os
from datetime import date, datetime
from pymongo import MongoClient
import json
import math


print ('hi')

client = MongoClient()
db = client.esiot
collection = db.lastData

def dataStore():

	currentDT = datetime.now()
	data = str(currentDT)
	print data
	data = data[:16]

	collection.save({"_id" : "ObjectId('5abe9d4201d9a734afcbdb0b')","lastWatered":data})

def humanDetection():
    import numpy as np
    import cv2 as cv
    face_cascade = cv.CascadeClassifier('facedata.xml')

    img = cv.imread("phot.jpg")
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    l=0
    r=0
    for (x,y,w,h) in faces:
	    if x+w<320:
	        l=1
	    elif x>320:
	        r=1
	    elif x<320 and x+w>=320:
	        l=1
	        r=1
	
	
	
	#cv.imshow('img',img)
	
	#cv.destroyAllWindows()
    
    if l==0 and r==0:
    	print 'no face'
        return 0
    elif l==0 and r==1:
        return 1
    elif l==1 and r==0:
        return 2
    else:
        return 3

def calcMM():

	client = MongoClient()
	db = client['esiot']
	cursor = db.weathers.find().sort('_id',-1).limit(1)
	
	preciptation = 0
	temperature = 0
	hrs = 0
	currentDT = datetime.now()
	cursor2 = db.lastData.find()

	for i in cursor2[0:1]:
		hrs = datetime.strptime(str(i['lastWatered']), '%Y-%m-%d %H:%M')
	
	hrs =  currentDT - hrs
	
	hrs = int(str(hrs)[0])
	
	for i in cursor[0:1]:
		temperature =  float(i['temp'])
		preciptation = float(i['precipitation'])

	print preciptation
	print temperature



	init = 10;
	rdc1 = init - (init * preciptation) / 100;
	rdc2 = (temperature / 20);
	newLevel = math.floor(init - hrs*((rdc1+rdc2) / 2));
	return newLevel;


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("192.168.31.199", 35239))                          #add ip
server_socket.listen(1)
client_socket, address = server_socket.accept()

strng = client_socket.recv(1024)
#print(type(strng))
#size = strng.decode("utf-8")
client_socket.send('ok')

size = int(strng)
#print(size)
var = 0
fp = open("phot.jpg",'wb')
while True:
    strng = client_socket.recv(512)
    var+=len(strng)  
    fp.write(strng)
    if var == size:
         break;
    
fp.close()

dataStore()
detect = humanDetection()
print 'cal'
mm = calcMM()
print 'sent'

client_socket.send("ON "+ str(detect) + " " + str(mm))
client_socket.close()



