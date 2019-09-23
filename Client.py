import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:10000")
accepted = 0
while(1):
	print ("Masukkan nama user anda:")
	nama = input()
	accepted = c.cekNama(nama)
	if accepted == 1:
		break
	else:
		print("User tidak ditemukan, mohon coba lagi")

amount = 0
while(1):
	print ("Masukkan Nilai TopUp (Minimal 10000)")
	amount = input()
	if int(amount) >= 10000:
		break
	else:
		print ("Minimal TopUp sebesar 10000, mohon coba lagi")
print (c.topUp(nama, int(amount)))