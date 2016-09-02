from flask import Flask, render_template, request, jsonify
import hcsr04controller
import hbridgecontroller
import RPi.GPIO as GPIO	

app = Flask(__name__)

# return index page when IP address of RPi is typed in the browser
@app.route("/")
def Index():
	return render_template("index.html", uptime=GetUptime())

# ajax GET call this function to set led state
# depeding on the GET parameter sent
@app.route("/_Adelante")
def _Adelante():
	controlMotores.ActivarPin1MotorA()
	return ""
@app.route("/_Stop")
def _Stop():
	controlMotores.PararMotorA()
	return ""
@app.route("/_Atras")
def _Atras():
	controlMotores.ActivarPin2MotorA()
	return ""
@app.route("/_Izquierda")
def _Izquierda():
	controlMotores.ActivarPin1MotorB()
	return ""
@app.route("/_Derecha")
def _Derecha():
	controlMotores.ActivarPin2MotorB()
	return ""
@app.route("/_Recto")
def _Recto():
	controlMotores.PararMotorB()
	return ""

def GetUptime():
    # get uptime from the linux terminal command
    from subprocess import check_output
    output = check_output(["uptime"])
    # return only uptime info
    uptime = output[output.find("up"):output.find("user")-5]
    return uptime
    
# run the webserver on standard port 80, requires sudo
if __name__ == "__main__":
	GPIO.setmode(GPIO.BCM)

#hcsr04Frontal = hcsr04controller.hcsr04controller(14,15,10)
	EnableA = 26
	ActivarPin1MotorA = 13
	ActivarPin2MotorA = 19
	EnableB = 21
	ActivarPin1MotorB = 20
	ActivarPin2MotorB = 16
	controlMotores = hbridgecontroller.hbridgecontroller(ActivarPin1MotorA,ActivarPin2MotorA,ActivarPin1MotorB,ActivarPin2MotorB,EnableA,EnableB)
	#hcsr04Frontal.IniciarPines()
	controlMotores.PararMotorA()
	controlMotores.PararMotorB()
	
	app.run(host='0.0.0.0', port=80, debug=True)
