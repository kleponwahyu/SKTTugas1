import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:10000")

def login():
	print ("Masukkan Nilai TopUp (Minimal 10000)")
	amount = input()
	if int(amount) >= 10000:
		print (c.topUp(nama, int(amount)))
	else:
		print ("Minimal TopUp sebesar 10000, mohon coba lagi")

print ("Masukkan nama user anda:")
nama = input()
accepted = c.cekNama(nama)	# Mengecek apakah nama ada di database Marketplace.py
if accepted == 1:
	login();
else:
	print("User tidak ditemukan, mohon coba lagi")
