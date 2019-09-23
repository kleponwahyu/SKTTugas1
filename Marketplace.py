import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:9999")

namaClientMarketplace =  ["Joko", "Bambang"]
saldoClientMarketplace = [0, 0]

class Marketplace(object):
    def topUp(self, namaclient, amount):
    	accepted = 0
    	accepted = c.pindahSaldo(namaclient, "Bukapedia", amount)
    	if accepted == 1:
    		index = 0
    		for x in namaClientMarketplace:
    			if namaclient == x:
    				break
    			else:
    				index = index + 1
    		saldoClientMarketplace[index] = saldoClientMarketplace[index] + amount
    		print (namaClientMarketplace[index], "berhasil TopUp sebesar", saldoClientMarketplace[index])
    		return "Berhasil bro! Saldo e-money mu = %s" % saldoClientMarketplace[index]
    	elif accepted == 2:
    		return "Gagal TopUp karena saldo di bank tidak mencukupi"
    	elif accepted == 0:
    		return "Gagal TopUp karena nasabah tidak terdaftar di bank"
        # global saldoBambang
        # saldoBambang = saldoBambang + amount
        # return "Berhasil bro! Saldo OpO mu = %s" % saldoBambang

    def cekNama(self, namaclient):
    	global namaClientMarketplace
    	accepted = 0
    	for x in namaClientMarketplace:
        	if namaclient == x:
        		return 1
        		break

s = zerorpc.Server(Marketplace())
s.bind("tcp://0.0.0.0:10000")
s.run()
# print (Marketplace.hello("Wahyu!"))
# print (Marketplace.jumlah(4, 6))