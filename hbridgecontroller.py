import RPi.GPIO as GPIO

class hbridgecontroller (object):
	def __init__(self,pin1MotorA,pin2MotorA,pin1MotorB,pin2MotorB,pinEnableA,pinEnableB):
		self.pin1MotorA = pin1MotorA
		self.pin1MotorB = pin1MotorB
		self.pin2MotorA = pin2MotorA
		self.pin2MotorB = pin2MotorB
		self.pinEnableA = pinEnableA
		self.pinEnableB = pinEnableB
		GPIO.setup(self.pin1MotorA, GPIO.OUT)
		GPIO.setup(self.pin2MotorA, GPIO.OUT)
		GPIO.setup(self.pin1MotorB, GPIO.OUT)
		GPIO.setup(self.pin2MotorB, GPIO.OUT)
		GPIO.setup(self.pinEnableA, GPIO.OUT)
		GPIO.setup(self.pinEnableB, GPIO.OUT)
		GPIO.output(self.pin1MotorA, 0)
		GPIO.output(self.pin2MotorA, 0)
		GPIO.output(self.pin1MotorB, 0)
		GPIO.output(self.pin2MotorB, 0)
		self.MotorA = GPIO.PWM(self.pinEnableA,100);
		self.MotorA.start(0);
		self.MotorA.ChangeDutyCycle(100);
		self.MotorB = GPIO.PWM(self.pinEnableB,100);
		self.MotorB.start(0);
		self.MotorB.ChangeDutyCycle(100);
		
	def PararMotorA(self):
		GPIO.output(self.pin1MotorA, GPIO.LOW)
		GPIO.output(self.pin2MotorA, GPIO.LOW)
		#self.MotorA.ChangeDutyCycle(0);

	def PararMotorB(self):
		GPIO.output(self.pin1MotorB, GPIO.LOW)
		GPIO.output(self.pin2MotorB, GPIO.LOW)
		#self.MotorB.ChangeDutyCycle(0);

	def ActivarPin1MotorA(self):
		self.PararMotorA()
		GPIO.output(self.pin1MotorA, GPIO.HIGH)
		#self.MotorA.ChangeDutyCycle(100);

	def ActivarPin2MotorA(self):
		self.PararMotorA()
		GPIO.output(self.pin2MotorA, GPIO.HIGH)
		#self.MotorA.ChangeDutyCycle(100);

	def ActivarPin1MotorB(self):
		self.PararMotorB()
		GPIO.output(self.pin1MotorB, GPIO.HIGH)
		#self.MotorB.ChangeDutyCycle(100);

	def ActivarPin2MotorB(self):
		self.PararMotorB()
		GPIO.output(self.pin2MotorB, GPIO.HIGH)
		#self.MotorB.ChangeDutyCycle(100);
