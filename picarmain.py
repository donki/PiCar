import hcsr04controller
import hbridgecontroller
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#hcsr04Frontal = hcsr04controller.hcsr04controller(14,15,10)
EnableA = 26
ActivarPin1MotorA = 13
ActivarPin2MotorA = 19
EnableB = 21
ActivarPin1MotorB = 20
ActivarPin2MotorB = 16

#GPIO.setup(26,GPIO.OUT)
#MA = GPIO.PWM(26,100)
#MA.start(0)
#MA.ChangeDutyCycle(0)
#MA.ChangeDutyCycle(40)
#GPIO.setup(19,GPIO.OUT)
#GPIO.setup(13,GPIO.OUT)
#GPIO.output(19,True)
#GPIO.output(13,False)
#time.sleep(5)
#GPIO.output(19,False)
#GPIO.output(13,True)
#time.sleep(5)

#GPIO.setup(13,GPIO.OUT)
#GPIO.output(13,False)
#GPIO.setup(26,GPIO.OUT)
#EnAPWM = GPIO.PWM(26,100)
#EnAPWM.start(0)
#EnAPWM.ChangeDutyCycle(0)
controlMotores = hbridgecontroller.hbridgecontroller(ActivarPin1MotorA,ActivarPin2MotorA,ActivarPin1MotorB,ActivarPin2MotorB,EnableA,EnableB)
#hcsr04Frontal.IniciarPines()
controlMotores.PararMotorA()
controlMotores.PararMotorB()
print 'Activar pin 1 A'
controlMotores.ActivarPin1MotorA()
time.sleep(1)
print 'Activar pin 2 A'
controlMotores.ActivarPin2MotorA()
time.sleep(1)
controlMotores.PararMotorA()
print 'Activar pin 1 B'
controlMotores.ActivarPin1MotorB()
time.sleep(1)
print 'Activar pin 2 B'
controlMotores.ActivarPin2MotorB()
time.sleep(2)
controlMotores.PararMotorA()
controlMotores.PararMotorB()
print 'Motores parados...'
time.sleep(1)
#try:
	
#	while True:

		#hcsr04Frontal.PotColisionar()
#		controlMotores.ActivarPin1MotorA()
#		print 'Activando pin 1 Motor A'
#		time.sleep(10)
#		controlMotores.PararMotorA()
#		time.sleep(1)
#		controlMotores.ActivarPin2MotorA()
#		print 'Activando pin 2 Motor A'	
#		time.sleep(10)
#		controlMotores.PararMotorA()
#		time.sleep(1)
#		controlMotores.ActivarPin1MotorB()
#		print 'Activando pin 1 Motor B'			
#		time.sleep(10)
#		controlMotores.PararMotorB()
#		time.sleep(10)
#		controlMotores.ActivarPin2MotorB()
#		print 'Activando pin 2 Motor B'					
#		time.sleep(10)
#		controlMotores.PararMotorB()
#		time.sleep(10)
	
#except KeyboardInterrupt:	
#GPIO.cleanup()
