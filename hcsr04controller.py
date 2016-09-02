import datetime
import time
import RPi.GPIO as GPIO

class hcsr04controller (object):
    def __init__(self,pinEcho,pintTrig,limitdistanciacm):
        self.FEcho = pinEcho
        self.FTrig = pintTrig
        self.FLimitDistanciacm = limitdistanciacm

    def IniciarPines(self):
        GPIO.setup(self.FTrig, GPIO.OUT)
        GPIO.output(self.FTrig, False)
	time.sleep(2)		
        GPIO.setup(self.FEcho, GPIO.IN)

    def calcular_distancia(self):
        GPIO.output(self.FTrig, False)
        time.sleep(2*10**-6)
        GPIO.output(self.FTrig,True)   #Enviamos un pulso de ultrasonidos
        time.sleep(10*10**-6)              #Una pausa
        GPIO.output(self.FTrig,False)  #Apagamos el pulso
        #start = time.time()              #Guarda el tiempo actual mediante time.time()

        while GPIO.input(self.FEcho)==0:  #Mientras el sensor no reciba seal...
            start = time.time()          #Mantenemos el tiempo actual mediante time.time()
        while GPIO.input(self.FEcho)==1:  #Si el sensor recibe seal...
            stop = time.time()
        elapsed = stop-start             #Obtenemos el tiempo transcurrido entre envo y recepcin
        distance = elapsed * 34300/2      #Distancia es igual a tiempo por velocidad partido por 2   D = (T x V)/2
	distance = round(distance,2)
        print distance                   #Devolvemos la distancia (en centmetros) por pantalla
        time.sleep(1) 
        return distance

    def PotColisionar(self):
        return self.calcular_distancia()<self.FLimitDistanciacm
