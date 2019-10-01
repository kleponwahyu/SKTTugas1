import zerorpc
import paho.mqtt.client as mqtt

Marketplace = zerorpc.Client()
Marketplace.connect("tcp://127.0.0.1:8081")
nomorhp = 0

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("topic/pulsa")

def on_message(client, userdata, msg):
	print("Message: " + msg.payload.decode())
	client.disconnect()

def login():
	print ("Masukkan Nilai TopUp (Minimal 10000)")
	amount = int(input())
	if amount >= 10000:
		print (Marketplace.topUp(nama, int(amount)))
	else:
		print ("Minimal TopUp sebesar 10000, mohon coba lagi")

def beliPulsa():
	global nomorhp
	print ("Masukkan jumlah pulsa")
	jumlahPulsa = int(input())
	if jumlahPulsa >= 10000:
		#print(Marketplace.beliPulsa(nama, nomorhp, jumlahPulsa))
		Marketplace.beliPulsa(nama, nomorhp, jumlahPulsa)
		client.loop_forever()
	else:
		print ("Minimal beli pulsa sebessar 10000, mohon coba lagi")


def cekNomor():
	print ("Masukkan nomor hp")
	global nomorhp
	nomorhp = input()
	verified = Marketplace.cekNomor(nomorhp)
	if verified == 1:
		print ("Nomor ada")
		print(beliPulsa())
	else:
		print ("Nomor tidak ada")

def menu():
	print ("1. Top Up saldo Bukapedia")
	print ("2. Beli Pulsa Indosel")
	print ("Masukkan pilihan: ")
	pilihan = int(input())
	if pilihan == 1:
		login()
	elif pilihan == 2:
		cekNomor()
	else:
		print ("Opsi tidak ada")

while(1):
	client = mqtt.Client()
	client.connect("localhost",1883,60)
	client.on_connect = on_connect
	client.on_message = on_message
	print ("Masukkan nama user anda:")
	nama = input()
	accepted = Marketplace.cekNama(nama)	# Mengecek apakah nama ada di database Marketplace.py
	if accepted == 1:
		menu()
	else:
		print("User tidak ditemukan, mohon coba lagi")
