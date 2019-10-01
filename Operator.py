import zerorpc
import threading
import time
import paho.mqtt.client as mqtt

dataNomorHp = ["14045", "08132456", "0123456"]
pulsa = [0, 0, 0]
verified = 0

def publish():
	threading.Timer(5.0, publish).start()
	global verified
	if verified == 1:
		print("publish...")
		client = mqtt.Client()
		client.connect("localhost",1883,60)
		client.publish("topic/pulsa", "Anda berhasil mengisi pulsa")
		client.disconnect()
		verified = 0

class Operator(object):
    def cekNomor(self, nomorhp):
    	accepted = 0
    	for x in dataNomorHp:
    		if nomorhp == x:
    			accepted = 1
    	if accepted == 1:
    		return 1
    	else:
    		return 0

    def beliPulsa(self, nomorhp, jumlahpulsa):
    	index = 0
    	for x in dataNomorHp:
    		if nomorhp == x:
    			break
    		else:
    			index = index + 1
    	pulsa[index] = pulsa[index] + jumlahpulsa
    	global verified
    	verified = 1
    	return pulsa[index]

publish()

Server = zerorpc.Server(Operator())
Server.bind("tcp://0.0.0.0:8082")
Server.run()
