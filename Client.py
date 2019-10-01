import zerorpc

Marketplace = zerorpc.Client()
Marketplace.connect("tcp://127.0.0.1:8081")
nomorhp = 0

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
		print(Marketplace.beliPulsa(nama, nomorhp, jumlahPulsa))
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

print ("Masukkan nama user anda:")
nama = input()
accepted = Marketplace.cekNama(nama)	# Mengecek apakah nama ada di database Marketplace.py
if accepted == 1:
	menu()
else:
	print("User tidak ditemukan, mohon coba lagi")
